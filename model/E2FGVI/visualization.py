import sys
import matplotlib.pyplot as plt
from matplotlib import animation
from IPython.display import HTML

from core.utils2 import read_frame_from_videos

%matplotlib inline

video_path = str(sys.argv[1])
fps = int(sys.argv[2])
frames = read_frame_from_videos(video_path)

def update(idx):
    imdata.set_data(frames[idx])
    
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.axis("off")
imdata = ax.imshow(frames[0])

fig.tight_layout()
anim = animation.FuncAnimation(fig, update, frames=len(frames),
                               interval=1000/fps)
HTML(anim.to_html5_video())
