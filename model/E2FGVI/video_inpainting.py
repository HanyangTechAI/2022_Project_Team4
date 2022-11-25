import torch
import numpy as np
from tqdm import tqdm

from .utils import get_ref_index
from .model.e2fgvi_hq import InpaintGenerator

class VideoInpaintingModel:
    
    def __init__(self, device="cpu", ref_length=10, num_ref=-1, neighbor_stride=5):

        self.ref_length = ref_length
        self.num_ref = num_ref
        self.neighbor_stride = neighbor_stride

        self.device = device
        self.model = InpaintGenerator().to(device)
        self.model.load_state_dict(torch.load('model/E2FGVI-HQ-CVPR22.pth', map_location=device))

    def inference(self, frames, masks):

        t = len(frames)
        h, w = frames[0].shape[:-1]

        imgs = torch.from_numpy(np.array(frames)).permute(0,3,1,2).contiguous().float().div(255)
        imgs = imgs.unsqueeze(0) * 2 - 1

        masks = np.expand_dims(masks,-1)
        binary_masks = [m.astype(np.uint8) for m in masks]
        masks = torch.from_numpy(masks).permute(0,3,1,2).contiguous().float()
        masks = masks.unsqueeze(0)

        imgs, masks = imgs.to(self.device), masks.to(self.device)
        comp_frames = [None] * t
        
        self.model.eval()
        for f in tqdm(range(0, t, self.neighbor_stride)):
            neighbor_ids = [i for i in range(max(0, f-self.neighbor_stride), min(t, f+self.neighbor_stride+1))]
            ref_ids = get_ref_index(f, neighbor_ids, t, self.ref_length, self.num_ref)
            selected_imgs = imgs[:1, neighbor_ids+ref_ids, :, :, :]
            selected_masks = masks[:1, neighbor_ids+ref_ids, :, :, :]
            with torch.no_grad():
                masked_imgs = selected_imgs * (1 - selected_masks)
                mod_size_h = 60
                mod_size_w = 108
                h_pad = (mod_size_h - h % mod_size_h) % mod_size_h
                w_pad = (mod_size_w - w % mod_size_w) % mod_size_w
                masked_imgs = torch.cat([masked_imgs, torch.flip(masked_imgs, [3])],3)[:, :, :, :h + h_pad, :]
                masked_imgs = torch.cat([masked_imgs, torch.flip(masked_imgs, [4])],4)[:, :, :, :, :w + w_pad]
                pred_imgs, _ = self.model(masked_imgs, len(neighbor_ids))
                pred_imgs = pred_imgs[:, :, :h, :w]
                pred_imgs = (pred_imgs + 1) / 2
                pred_imgs = pred_imgs.cpu().permute(0, 2, 3, 1).numpy() * 255
                for i in range(len(neighbor_ids)):
                    idx = neighbor_ids[i]
                    img = np.array(pred_imgs[i]).astype(np.uint8)*binary_masks[idx] + frames[idx] * (1-binary_masks[idx])
                    if comp_frames[idx] is None:
                        comp_frames[idx] = img
                    else:
                        comp_frames[idx] = comp_frames[idx].astype(np.float32)*0.5 + img.astype(np.float32)*0.5

        return comp_frames
