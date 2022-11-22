# How to Use

## Create the Model and Inference
<pre>
<code>
import torch
from video_inpainting import VideoInpaintingModel

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu"
model = VideoInpaintingModel(device=device)
output = model.inference(frames,masks)

"""
VideoInpaintingModel's arguments are device, ref_index, num_ref, neighbor_stride.
You can adjust the arguments' value.
Variable 'frames' and 'masks' are both 'np.ndarray'. [frames's shape: (T,H,W,3) / masks's shape: (T,H,W)]
"""
</code>
</pre>

## Save Inpainted Video
<pre>
<code>
from utils import save_video

save_video(output,fps)

"""
Variable 'output' is VideoInpaintingModel's output. 
Inpainted video is saved in the directory under the name "Inpainting_Video.mp4". 
"""
</code>
</pre>
