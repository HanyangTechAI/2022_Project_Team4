from .propagation import propagation
import torch
import cv2
from os import path

videoId_to_class = {}
videoId_to_video = {}

#도현이 형이 outList가져다가 쓰면 됨. torch.stack(self.frames, 0)참고.

#get mask frame
def createClass(videoId,second):
    global videoId_to_video
    global videoId_to_class
    inputPath = path.join("inputVideos", videoId + ".mp4")
    cap = cv2.VideoCapture(inputPath)#front에서 받은 mp4파일을 array로 변환.

    outList = []

    if(not(cap.isOpened())):
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
        #print ("Frames per second using video.get(cv2.cv.CV_CAP_PROP_FPS): {0}".format(fps))
    else :
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        #print ("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))
    

    cap.release()
    videoId_to_video[videoId] = outList
    videoId_to_class[videoId] = propagation(outList,int(float(second)*fps))

def GetMaskImage(videoId):
    if(videoId in videoId_to_class):
        return videoId_to_class[videoId].getMaskImage()#jpg

def GetSize(videoId):
    if(videoId in videoId_to_class):
        return videoId_to_class[videoId].getSize()
    else:
        print("no")

def GetSelectedMask(videoId,XYCoordinates):#XYCoordinates :[x,y] format
    if(videoId in videoId_to_class):
        return videoId_to_class[videoId].getSelectedMask(XYCoordinates)#jpg

def Process(videoId):
    if(videoId in videoId_to_class):
        out_masks = videoId_to_class[videoId].process()
        #여기서 형이 작업
        #videoId_to_video[videoId] 와 out_masks 이용
        del videoId_to_class[videoId]
        return out_masks











