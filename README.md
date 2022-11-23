# 2022_Project_Team4
This is a repository for 2022 project of team 4

## mask propagation 쓰는 법


1.from propagation import propagation로 propagation class 를 불러옴

2.front로 부터 mp4 file과 frame index를 받아서 propa = propagation(args.file,int(args.index))와 같이 model을 만들어 넣음

3.propa.getMaskImage()이 마스크가 얹혀진 이미지를 반환(jpg). 이를 front로 보냄.

4.사용자가 클릭한 이미지 위 픽셀의 좌표를 front로부터 받아 propa.getSelectedMask(XYCoordinates)와 같이 넣음. 그러면 
  propa.getSelectedMask(XYCoordinates)가 선택된 마스크만 얹혀진 이미지를 반환함(jpg). 이를 front로 보냄.

5.선택한 마스크가 맘에 안들면 propa.getSelectedMask(XYCoordinates)를 다시 호출 가능

6.propa.process()를 실행하면 모든 프레임에서 누끼 마스크 반환(frames,w,c)


*사용자가 클릭한 이미지를 위 좌표는 픽셀 단위임. front에서 필요하다면 propa.getSize()를 통하여 pixel의 w,c를 받을 수 있음

*main.py를 돌려보는게 이해가 빠를지도...

*실행 예시 python main.py --index 100 --output output_folder --file ./testVideos/videoplayback_Trim.mp4

*귀찮으면 python main.py