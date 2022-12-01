import cv2
import numpy as np

# save video
def save_video(frames,fps,video_id):
    h, w = frames[0].shape[:-1]
    fourcc = cv2.VideoWriter_fourcc(*'DIVX')
    video = cv2.VideoWriter(f"{video_id}.mp4",fourcc,fps,(w,h))
    for f in frames:
        video.write(f[:,:,::-1].astype(np.uint8))
    video.release()
