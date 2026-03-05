import cv2 as cv # OpenCV 라이브러리를 불러옵니다.

drawing = False # 드래그 상태를 확인하는 변수입니다.
ix, iy = -1, -1 # 드래그 시작 좌표(x, y)를 초기화합니다.
fx, fy = -1, -1 # 드래그 종료 좌표(x, y)를 초기화합니다.

img = cv.imread('girl_laughing.jpg') # 작업할 이미지를 불러옵니다[cite: 57].
clone = img.copy() # 원본 이미지를 훼손하지 않기 위해 복사본을 만듭니다.

# 마우스 이벤트 처리 함수 [cite: 58]
def select_roi(event, x, y, flags, param):
    global ix, iy, fx, fy, drawing, img, clone # 전역 변수 사용을 선언합니다.
    
    if event == cv.EVENT_LBUTTONDOWN: # 마우스 왼쪽 버튼을 누르면 시작
        drawing = True # 드래그 상태 활성화
        ix, iy = x, y # 시작점 좌표 저장 [cite: 59]
        
    elif event == cv.EVENT_MOUSEMOVE: # 마우스를 이동할 때
        if drawing: # 드래그 중이라면
            img = clone.copy() # 화면 갱신을 위해 복사본 이미지를 가져옵니다.
            cv.rectangle(img, (ix, iy), (x, y), (0, 255, 0), 2) # 드래그 중인 영역을 녹색 사각형으로 시각화합니다[cite: 63].
            
    elif event == cv.EVENT_LBUTTONUP: # 마우스 왼쪽 버튼을 떼면 종료
        drawing = False # 드래그 상태 비활성화
        fx, fy = x, y # 종료점 좌표 저장
        cv.rectangle(img, (ix, iy), (fx, fy), (0, 255, 0), 2) # 최종 사각형을 그립니다.
        
        # 좌상단, 우하단 좌표 정렬 (드래그 방향에 상관없이 ROI를 추출하기 위함)
        x1, x2 = min(ix, fx), max(ix, fx)
        y1, y2 = min(iy, fy), max(iy, fy)
        
        # 유효한 영역이 선택되었는지 확인
        if x2 - x1 > 0 and y2 - y1 > 0:
            roi = clone[y1:y2, x1:x2] # numpy 슬라이싱으로 선택 영역(ROI)만 잘라냅니다[cite: 60, 64].
            cv.imshow('ROI', roi) # 잘라낸 ROI를 'ROI'라는 새 창에 출력합니다[cite: 60].

cv.namedWindow('Image') # 'Image'라는 이름의 메인 창을 만듭니다.
cv.setMouseCallback('Image', select_roi) # 메인 창에 마우스 이벤트를 연결합니다[cite: 58].

while True:
    cv.imshow('Image', img) # 메인 이미지를 계속 업데이트하여 보여줍니다[cite: 57].
    key = cv.waitKey(1) & 0xFF # 키 입력을 대기합니다.
    
    if key == ord('r'): # 'r' 키를 누르면 리셋 [cite: 61]
        img = clone.copy() # 이미지를 원본 복사본으로 되돌립니다.
        ix, iy, fx, fy = -1, -1, -1, -1 # 좌표를 초기화합니다.
        if cv.getWindowProperty('ROI', cv.WND_PROP_VISIBLE) >= 0: # ROI 창이 열려있다면
            cv.destroyWindow('ROI') # ROI 창을 닫습니다.
            
    elif key == ord('s'): # 's' 키를 누르면 저장 [cite: 62]
        x1, x2 = min(ix, fx), max(ix, fx)
        y1, y2 = min(iy, fy), max(iy, fy)
        if x2 - x1 > 0 and y2 - y1 > 0: # 유효한 영역이 있다면
            roi = clone[y1:y2, x1:x2] # ROI를 다시 추출하여
            cv.imwrite('saved_roi.jpg', roi) # 'saved_roi.jpg' 파일명으로 저장합니다[cite: 65].
            print("ROI가 성공적으로 저장되었습니다.")
            
    elif key == ord('q'): # 'q' 키를 누르면 전체 종료
        break # 루프를 탈출합니다.

cv.destroyAllWindows() # 모든 창을 닫습니다.git push origin main