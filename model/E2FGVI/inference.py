import sys
import torch
from tqdm import tqdm

from core.utils import to_tensors
from core.utils2 import *
from model.e2fgvi import InpaintGenerator

# global variables
w, h = 432, 240
ref_length = 10
num_ref = -1
neighbor_stride = 5

# set up models
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = InpaintGenerator().to(device)
ckpt_path = "release_model/E2FGVI-CVPR22.pth"
data = torch.load(ckpt_path, map_location=device)
model.load_state_dict(data)

# prepare dataset
input_path = str(sys.argv[1])
video_path = input_path + "/video"
maks_path = input_path + "/mask"
frames = read_frame_from_videos(video_path)
video_length = len(frames)
imgs = to_tensors()(frames).unsqueeze(0) * 2 - 1
frames = [np.array(f).astype(np.uint8) for f in frames]
masks = read_mask(mask_path)
binary_masks = [np.expand_dims((np.array(m) != 0).astype(np.uint8), 2)
                for m in masks]
masks = to_tensors()(masks).unsqueeze(0)
imgs, masks = imgs.to(device), masks.to(device)
comp_frames = [None] * video_length

# run E2FGVI model
model.eval()
for f in tqdm(range(0, video_length, neighbor_stride)):
    neighbor_ids = [i for i in range(max(0, f-neighbor_stride), min(video_length, f+neighbor_stride+1))]
    ref_ids = get_ref_index(f, neighbor_ids, video_length)
    selected_imgs = imgs[:1, neighbor_ids+ref_ids, :, :, :]
    selected_masks = masks[:1, neighbor_ids+ref_ids, :, :, :]
    with torch.no_grad():
        masked_imgs = selected_imgs*(1-selected_masks)
        pred_img, _ = model(masked_imgs, len(neighbor_ids))

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

# save inpainting result
output_path = str(sys.argv[2])
save_result(comp_frames, output_path)
