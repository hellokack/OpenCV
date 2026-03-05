import cv2 as cv # OpenCV 라이브러리를 불러옵니다.
import numpy as np # 배열(도화지)을 만들기 위해 numpy 라이브러리를 불러옵니다.

brush_size = 5 # 초기 붓 크기를 5로 설정합니다.
drawing = False # 마우스 드래그 상태를 확인하기 위한 플래그 변수입니다.
color = (0, 0, 0) # 초기 그리기 색상을 검은색으로 설정합니다.

# 마우스 이벤트 처리 콜백 함수 정의
def paint(event, x, y, flags, param):
    global drawing, color, brush_size, img # 전역 변수들을 함수 내에서 사용하겠다고 선언합니다.
    
    # 좌클릭 시 파란색 설정 및 그리기 시작
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True # 그리기 상태를 켜줍니다.
        color = (255, 0, 0) # 색상을 파란색(B,G,R)으로 변경합니다.
        cv.circle(img, (x, y), brush_size, color, -1) # 현재 위치에 원을 그립니다.
        
    # 우클릭 시 빨간색 설정 및 그리기 시작
    elif event == cv.EVENT_RBUTTONDOWN:
        drawing = True # 그리기 상태를 켜줍니다.
        color = (0, 0, 255) # 색상을 빨간색(B,G,R)으로 변경합니다.
        cv.circle(img, (x, y), brush_size, color, -1) # 현재 위치에 원을 그립니다.
        
    # 마우스 이동 시 연속 그리기
    elif event == cv.EVENT_MOUSEMOVE:
        if drawing: # 그리기 상태일 때만 동작합니다.
            cv.circle(img, (x, y), brush_size, color, -1) # 마우스 궤적을 따라 원을 그립니다.
            
    # 마우스 클릭 해제 시 그리기 종료
    elif event == cv.EVENT_LBUTTONUP or event == cv.EVENT_RBUTTONUP:
        drawing = False # 그리기 상태를 끕니다.

# [수정된 부분] 이미지 로드 대신 세로 600, 가로 800 크기의 하얀색 배경 캔버스 생성
img = np.ones((600, 800, 3), dtype=np.uint8) * 255 

cv.namedWindow('Paint') # 'Paint'라는 이름의 창을 생성합니다.
cv.setMouseCallback('Paint', paint) # 'Paint' 창에 마우스 이벤트 콜백 함수를 연결합니다.

while True: # 무한 루프를 돌며 창을 갱신합니다.
    cv.imshow('Paint', img) # 이미지를 화면에 보여줍니다.
    
    key = cv.waitKey(1) & 0xFF # 1ms 동안 키보드 입력을 대기하고 값을 받습니다.
    
    if key == ord('q'): # 'q' 키를 누르면 종료합니다.
        break # 무한 루프를 빠져나갑니다.
    elif key == ord('+') or key == ord('='): # '+' 키를 누르면 (Shift 없이 눌리는 '='도 포함)
        brush_size = min(15, brush_size + 1) # 붓 크기를 1 증가시키되, 최대 15로 제한합니다.
    elif key == ord('-'): # '-' 키를 누르면
        brush_size = max(1, brush_size - 1) # 붓 크기를 1 감소시키되, 최소 1로 제한합니다.

cv.destroyAllWindows() # 모든 창을 닫고 프로그램을 종료합니다.