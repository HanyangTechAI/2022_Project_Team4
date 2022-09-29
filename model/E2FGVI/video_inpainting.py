import torch
import numpy as np
from tqdm import tqdm

from core.utils import to_tensors
from core.utils2 import *
from model.e2fgvi_hq import InpaintGenerator

class VideoInpaintingModel:

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = InpaintGenerator().to(device)
    video_path, mask_path = None, None
    
    def __init__(self, w=432, h=240, ref_length=10, num_ref=-1, neighbor_stride=5):

        self.w, self.h = w, h
        self.ref_length = ref_length
        self.num_ref = num_ref
        self.neighbor_stride = neighbor_stride

    def setting(self, ckpt_path, input_path):

        weight = torch.load(ckpt_path, map_location=self.device)
        self.model.load_state_dict(weight)
        self.video_path = input_path + "/video"
        self.mask_path = input_path + "/mask"

    def inference(self):

        frames = read_frame_from_videos(self.video_path, self.w, self.h)
        video_length = len(frames)
        imgs = to_tensors()(frames).unsqueeze(0) * 2 - 1
        frames = [np.array(f).astype(np.uint8) for f in frames]
        masks = read_mask(self.mask_path, self.w, self.h)
        binary_masks = [np.expand_dims((np.array(m) != 0).astype(np.uint8), 2) for m in masks]
        masks = to_tensors()(masks).unsqueeze(0)
        imgs, masks = imgs.to(self.device), masks.to(self.device)
        comp_frames = [None] * video_length
        
        self.model.eval()

        for f in tqdm(range(0, video_length, self.neighbor_stride)):
            neighbor_ids = [i for i in range(max(0, f-self.neighbor_stride), min(video_length, f+self.neighbor_stride+1))]
            ref_ids = get_ref_index(f, neighbor_ids, video_length, self.ref_length, self.num_ref)
            selected_imgs = imgs[:1, neighbor_ids+ref_ids, :, :, :]
            selected_masks = masks[:1, neighbor_ids+ref_ids, :, :, :]
            with torch.no_grad():
                masked_imgs = selected_imgs*(1-selected_masks)
                pred_img, _ = self.model(masked_imgs, len(neighbor_ids))

                pred_img = (pred_img + 1) / 2
                pred_img = pred_img.cpu().permute(0, 2, 3, 1).numpy() * 255
                for i in range(len(neighbor_ids)):
                    idx = neighbor_ids[i]
                    img = np.array(pred_img[i]).astype(
                        np.uint8)*binary_masks[idx] + frames[idx] * (1-binary_masks[idx])
                    if comp_frames[idx] is None:
                        comp_frames[idx] = img
                    else:
                        comp_frames[idx] = comp_frames[idx].astype(
                            np.float32)*0.5 + img.astype(np.float32)*0.5

        return comp_frames
