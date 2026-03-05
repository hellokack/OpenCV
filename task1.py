import cv2 as cv # OpenCV 라이브러리를 cv라는 이름으로 불러옵니다.
import numpy as np # 행열 및 배열 처리 라이브러리인 numpy를 np라는 이름으로 불러옵니다.

# 1. 이미지 불러오기 (OpenCV는 이미지를 BGR 형식으로 읽습니다) [cite: 21, 25]
img = cv.imread('soccer.jpg') # 'soccer.jpg' 파일을 BGR 형식으로 읽어 img 변수에 저장합니다.

# 2. 이미지를 그레이스케일로 변환 [cite: 22]
# cv.COLOR_BGR2GRAY 옵션을 사용하여 BGR 이미지를 흑백으로 변환합니다[cite: 26].
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) 

# 3. 원본과 병합하기 위한 차원 맞추기
# np.hstack을 하려면 두 이미지의 채널 수가 같아야 하므로, 흑백 이미지를 3채널로 임시 변환합니다.
gray_3c = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)

# 4. 두 이미지를 가로로 연결하여 출력 [cite: 23]
# np.hstack을 사용하여 원본(img)과 흑백(gray_3c) 이미지를 가로 방향으로 이어 붙입니다.
result = np.hstack((img, gray_3c))

# 5. 결과를 화면에 표시 [cite: 24]
cv.imshow('Result', result) # 'Result'라는 이름의 창에 결과 이미지를 띄웁니다.

# 6. 아무 키나 누르면 창 닫기 [cite: 24]
cv.waitKey(0) # 키보드 입력이 있을 때까지 무한정 대기합니다.
cv.destroyAllWindows() # 열려있는 모든 OpenCV 창을 닫습니다.