import os
import cv2
import numpy as np
from PIL import Image

import matplotlib.pyplot as plt
from matplotlib import animation
from IPython.display import HTML

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

# read frame-wise masks
def read_mask(mpath, w, h):
    masks = []
    mnames = os.listdir(mpath)
    mnames.sort()
    for mp in mnames:
        m = Image.open(os.path.join(mpath, mp))
        m = m.resize((w, h), Image.NEAREST)
        m = np.array(m.convert('L'))
        m = np.array(m > 0).astype(np.uint8)
        m = cv2.dilate(m, cv2.getStructuringElement(
            cv2.MORPH_CROSS, (3, 3)), iterations=4)
        masks.append(Image.fromarray(m*255))
    return masks

# read frames from video
def read_frame_from_videos(video_path, w, h):
    vname = video_path
    frames = []
    lst = os.listdir(vname)
    lst.sort()
    fr_lst = [vname+'/'+name for name in lst]
    for fr in fr_lst:
        image = cv2.imread(fr)
        image = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        frames.append(image.resize((w, h)))
    return frames

# save inpainting results from model
def save_result(results,opath):
    os.makedirs(opath)
    length = len(results)
    for i in range(length):
        cv2.imwrite(f"opath/{i:0>5}.png",results[i])
        
# visualize
def play_video(frames, interval):

    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.axis("off")
    imdata = ax.imshow(frames[0].astype(np.uint8))

    def update(idx):
        imdata.set_data(frames[idx].astype(np.uint8))

    fig.tight_layout()
    anim = animation.FuncAnimation(fig, update, frames=len(frames), interval=interval)

    return HTML(anim.to_html5_video())

