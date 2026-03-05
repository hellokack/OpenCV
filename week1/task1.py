import cv2 as cv # OpenCV 라이브러리를 cv라는 이름으로 불러옵니다.
import numpy as np # 배열 처리를 위해 numpy를 np라는 이름으로 불러옵니다.

# 1. 이미지 불러오기 (OpenCV는 이미지를 BGR 형식으로 읽습니다)
img = cv.imread('soccer.jpg') 

# 원본 이미지의 해상도가 높아 화면을 벗어나는 것을 방지하기 위해 크기를 조정합니다.
# cv.resize 함수를 사용하여 이미지의 가로(fx)와 세로(fy) 비율을 각각 50%로 축소합니다.
img = cv.resize(img, None, fx=0.5, fy=0.5, interpolation=cv.INTER_AREA)

# 2. 이미지를 그레이스케일로 변환cd week1
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) 

# 3. 원본과 병합하기 위한 차원 맞추기
# np.hstack을 하려면 채널 수가 같아야 하므로, 흑백 이미지를 3채널로 임시 변환합니다.
gray_3c = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)

# 4. 두 이미지를 가로로 연결하여 출력
result = np.hstack((img, gray_3c))

# 5. 결과를 화면에 표시
cv.imshow('Result', result) 

# 6. 아무 키나 누르면 창 닫기
cv.waitKey(0) 
cv.destroyAllWindows()