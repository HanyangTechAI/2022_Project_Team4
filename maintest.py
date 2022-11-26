from Model import api
import cv2
import os 
from PIL import Image
from os import path

XYCoordinates = []

def getXYCoordinates(event, x, y, flags, param):
    global XYCoordinates
    if event == cv2.EVENT_LBUTTONDOWN:
        XYCoordinates= [x,y]

def process():
    execute = input()# create / select / process

    if(execute == "create"):
        videoId,second = input().split()
        api.createClass(videoId,int(second))
        print("done")

    elif(execute == "select"): #다시 반복 가능.
        videoId = input()
        cv2.namedWindow("images")
        cv2.setMouseCallback("images", getXYCoordinates)
        cv2.imshow("images", cv2.resize(api.GetMaskImage(videoId),api.GetSize(videoId)))#front에 mask가 씌워진 이미지를 보냄
        while True:
                    key = cv2.waitKey(1) & 0xFF
                    if key == ord("q"):
                        break
        cv2.destroyAllWindows()#api.GetMaskImage(videoId)를 front로 보내고 x,y좌표를 받음.

        cv2.namedWindow("images")
        cv2.imshow("images", cv2.resize(api.GetSelectedMask(videoId,XYCoordinates),api.GetSize(videoId)))#front에서 이미지 위에 사용자가 클릭한 xy좌표를 받아 선택된 마스크 이미지를 보냄. 
        cv2.waitKey(1000)#api.GetSelectedMask(videoId,XYCoordinates)를 front로 보내줌.
        cv2.destroyAllWindows()
        print("done")

    elif(execute == "process"):
        videoId = input()
        output = api.Process(videoId)#지금은 output이 mask array임. 도현이 형이 완성 후 파일로 저장.

        palette = Image.open(path.expanduser('./Model/palette/00000.png')).getpalette()
        os.makedirs("outputVideos", exist_ok=True)
        this_out_path = path.join("outputVideos", videoId)
        os.makedirs(this_out_path, exist_ok=True)
        for f in range(output.shape[0]):
            img_E = Image.fromarray(output[f])
            img_E.putpalette(palette)
            img_E.save(os.path.join(this_out_path, '{:05d}.png'.format(f)))
            #img_E.save(os.path.join(videoId, '{:05d}.png'.format(f)))#mask를 이미지 파일로 저장
        print("done")
    elif(execute == "quit"):
        return False

    return True

while(process()):
    pass

