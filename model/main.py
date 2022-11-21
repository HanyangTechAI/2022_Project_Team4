from propagation import propagation
from argparse import ArgumentParser
import os
from os import path
from PIL import Image
import torch
import cv2

#basic setup
parser = ArgumentParser()
parser.add_argument('--index', default=1)
parser.add_argument('--file', default='./testVideos/videoplayback_Trim.mp4')
parser.add_argument('--output', default='output')
args = parser.parse_args()

out_path = args.output


os.makedirs(out_path, exist_ok=True)
palette = Image.open(path.expanduser('./palette/00000.png')).getpalette()

torch.autograd.set_grad_enabled(False)

#get mask frame
propa = propagation(args.file,int(args.index))#front에서 mp4파일과 index를 받아서 모델을 만듦


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

out_masks = propa.process()#propagaton을 통하여 나머지 프레임에서 mask를 땀-> 도현이 형에게 보냄


os.makedirs(out_path, exist_ok=True)
for f in range(out_masks.shape[0]):
    img_E = Image.fromarray(out_masks[f])
    img_E.putpalette(palette)
    img_E.save(os.path.join(out_path, '{:05d}.png'.format(f)))#mask를 이미지 파일로 저장

print("done")









