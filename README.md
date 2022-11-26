
# mask propagation 쓰는 법

#### python path에 2022_Project_Team4/Model, 2022_Project_Team4/Model/detectron2-windows,2022_Project_Team4/Model/Mask-Propagation 경로 추가 필요. https://pybasall.tistory.com/201 참고.

1. input videos에 videoId.mp4로 video저장

2. api.createClass(videoId,int(second))실행하면 class 생성

3. api.GetMaskImage(videoId)실행하면 모든 마스크가 씌워진 이미지 생성. (front로 보냄) ->x,y를 받음

4. XYCoordinates = [x,y] 생성.

5. api.GetSelectedMask(videoId,XYCoordinates)실행하면 선택된 마스크만 보여주는 이미지 생성. (front로 보냄)

6. api.Process(videoId)를 실행하면 outputVideos에 videoId.mp4 생성(미완)

*maintest.py 참고