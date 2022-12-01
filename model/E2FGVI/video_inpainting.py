import torch
import numpy as np
from tqdm import tqdm

from .model.e2fgvi_hq import InpaintGenerator


# sample reference frames from the whole video 
def get_ref_index(f, neighbor_ids, length, ref_length, num_ref):
    ref_index = []
    if num_ref == -1:
        for i in range(0, length, ref_length):
            if i not in neighbor_ids:
                ref_index.append(i)
    else:
        start_idx = max(0, f - ref_length * (num_ref//2))
        end_idx = min(length, f + ref_length * (num_ref//2))
        for i in range(start_idx, end_idx+1, ref_length):
            if i not in neighbor_ids:
                if len(ref_index) > num_ref:
                    break
                ref_index.append(i)
    return ref_index


class VideoInpaintingModel:
    
    def __init__(self, ref_length=10, num_ref=-1, neighbor_stride=5):

        self.ref_length = ref_length
        self.num_ref = num_ref
        self.neighbor_stride = neighbor_stride

        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model = InpaintGenerator().to(self.device)
        self.model.load_state_dict(torch.load('E2FGVI/model_zoo/E2FGVI-HQ-CVPR22.pth', map_location=self.device))

    def inference(self, frames, masks):

        t, h, w = masks.shape

        imgs = torch.from_numpy(np.array(frames)).permute(0,3,1,2).contiguous().float().div(255)
        imgs = imgs.unsqueeze(0) * 2 - 1

        masks = np.expand_dims(masks,-1)
        binary_masks = [m.astype(np.uint8) for m in masks]
        masks = torch.from_numpy(masks).permute(0,3,1,2).contiguous().float()
        masks = masks.unsqueeze(0)

        comp_frames = [None] * t
        
        self.model.eval()
        for f in tqdm(range(0, t, self.neighbor_stride)):
            neighbor_ids = [i for i in range(max(0, f-self.neighbor_stride), min(t, f+self.neighbor_stride+1))]
            ref_ids = get_ref_index(f, neighbor_ids, t, self.ref_length, self.num_ref)
            selected_imgs = imgs[:1, neighbor_ids+ref_ids, :, :, :]
            selected_masks = masks[:1, neighbor_ids+ref_ids, :, :, :]
            with torch.no_grad():
                masked_imgs = selected_imgs * (1 - selected_masks)
                masked_imgs = masked_imgs.to(self.device)
                mod_size_h = 60
                mod_size_w = 108
                h_pad = (mod_size_h - h % mod_size_h) % mod_size_h
                w_pad = (mod_size_w - w % mod_size_w) % mod_size_w
                masked_imgs = torch.cat([masked_imgs, torch.flip(masked_imgs, [3])],3)[:, :, :, :h + h_pad, :]
                masked_imgs = torch.cat([masked_imgs, torch.flip(masked_imgs, [4])],4)[:, :, :, :, :w + w_pad]
                pred_imgs = self.model(masked_imgs, len(neighbor_ids))
                del masked_imgs
                torch.cuda.empty_cache()
                pred_imgs = pred_imgs[:, :, :h, :w]
                pred_imgs = (pred_imgs + 1) / 2
                pred_imgs = pred_imgs.cpu().permute(0, 2, 3, 1).numpy() * 255
                torch.cuda.empty_cache()
                for i in range(len(neighbor_ids)):
                    idx = neighbor_ids[i]
                    img = np.array(pred_imgs[i]).astype(np.uint8)*binary_masks[idx] + frames[idx] * (1-binary_masks[idx])
                    if comp_frames[idx] is None:
                        comp_frames[idx] = img
                    else:
                        comp_frames[idx] = comp_frames[idx].astype(np.float32)*0.5 + img.astype(np.float32)*0.5

        return comp_frames
