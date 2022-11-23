from propagation import propagation
from argparse import ArgumentParser
import os
from os import path
from PIL import Image
import torch
import cv2

#basic setup
parser = ArgumentParser()
parser.add_argument('--second', default=3)#동영상 index에서 동영상 second로 변경
parser.add_argument('--file', default='./testVideos/videoplayback_Trim.mp4')
parser.add_argument('--output', default='output')
args = parser.parse_args()

os.makedirs(args.output, exist_ok=True)
palette = Image.open(path.expanduser('./palette/00000.png')).getpalette()

torch.autograd.set_grad_enabled(False)

cap = cv2.VideoCapture(args.file)#front에서 받은 mp4파일을 array로 변환.

outList = []

if(not(cap.isOpened())):
    print("cant open file")
    quit()



while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        outList.append(torch.tensor(frame))
    else: 
        break
(major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
if int(major_ver)  < 3 :
    fps = int(cap.get(cv2.cv.CV_CAP_PROP_FPS))
    print ("Frames per second using video.get(cv2.cv.CV_CAP_PROP_FPS): {0}".format(fps))
else :
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    print ("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))
 

cap.release()

#도현이 형이 outList가져다가 쓰면 됨. torch.stack(self.frames, 0)참고.

#get mask frame
propa = propagation(outList,int(args.second)*fps)#front에서 mp4파일과 second를 받아서 모델을 만듦


XYCoordinates = []
def getXYCoordinates(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        XYCoordinates.append([x,y])



cv2.namedWindow("images")
cv2.setMouseCallback("images", getXYCoordinates)
cv2.imshow("images", cv2.resize(propa.getMaskImage(),propa.getSize()))#front에 mask가 씌워진 이미지를 보냄

while True:
            key = cv2.waitKey(1) & 0xFF
            if key == ord("q"):
                break
cv2.destroyAllWindows()

cv2.namedWindow("images")
cv2.imshow("images", cv2.resize(propa.getSelectedMask(XYCoordinates),propa.getSize()))#front에서 이미지 위에 사용자가 클릭한 xy좌표를 받아 선택된 마스크 이미지를 보냄. 
cv2.waitKey(5000)

del XYCoordinates

out_masks = propa.process()#propagaton을 통하여 나머지 프레임에서 mask를 땀-> 도현이 형에게 보냄

del propa

#save out_mask as a file
os.makedirs(args.output, exist_ok=True)
for f in range(out_masks.shape[0]):
    img_E = Image.fromarray(out_masks[f])
    img_E.putpalette(palette)
    img_E.save(os.path.join(args.output, '{:05d}.png'.format(f)))#mask를 이미지 파일로 저장

print("done")









