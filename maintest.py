import sys
import os

sys.path.insert(0,"/home/hai/2022_Project_Team4/Model/detectron2")
sys.path.insert(0,"/home/hai/2022_Project_Team4/Model/Mask-Propagation")

from Model import api
import cv2
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
        api.createClass(videoId,float(second))
        print("done")

    elif(execute == "select"): #다시 반복 가능.
        videoId = input()
        '''cv2.namedWindow("images")
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
        cv2.destroyAllWindows()'''
        aa = api.GetSelectedMask(videoId,[320,180])
        print("done")

    elif(execute == "process"):
        videoId = input()
        api.Process(videoId)#지금은 output이 mask array임. 도현이 형이 완성 후 파일로 저장.
        print("done")
    elif(execute == "quit"):
        return False

    return True

while(process()):
    pass

