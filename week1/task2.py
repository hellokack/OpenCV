import cv2 as cv 

brush_size = 5 # 초기 붓 크기를 5로 설정합니다.
drawing = False # 마우스 드래그 상태를 확인하기 위한 플래그 변수입니다.
color = (0, 0, 0) # 초기 그리기 색상을 검은색으로 설정합니다.

# 마우스 이벤트 처리 콜백 함수 정의
def paint(event, x, y, flags, param):
    global drawing, color, brush_size, img 
    
    # 좌클릭 시 파란색 설정 및 그리기 시작
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True 
        color = (255, 0, 0) # 파란색 (B,G,R)
        cv.circle(img, (x, y), brush_size, color, -1) 
        
    # 우클릭 시 빨간색 설정 및 그리기 시작
    elif event == cv.EVENT_RBUTTONDOWN:
        drawing = True 
        color = (0, 0, 255) # 빨간색 (B,G,R)
        cv.circle(img, (x, y), brush_size, color, -1) 
        
    # 마우스 이동 시 연속 그리기
    elif event == cv.EVENT_MOUSEMOVE:
        if drawing: 
            cv.circle(img, (x, y), brush_size, color, -1) 
            
    # 마우스 클릭 해제 시 그리기 종료
    elif event == cv.EVENT_LBUTTONUP or event == cv.EVENT_RBUTTONUP:
        drawing = False 

# -------------------------------------------------------------------
# [수정된 부분] 흰 도화지 대신 soccer.jpg를 불러오고 크기를 조정합니다.
# -------------------------------------------------------------------
img = cv.imread('soccer.jpg') 
img = cv.resize(img, None, fx=0.5, fy=0.5, interpolation=cv.INTER_AREA)

cv.namedWindow('Paint') 
cv.setMouseCallback('Paint', paint) # 마우스 이벤트 연결

while True: 
    cv.imshow('Paint', img) 
    
    key = cv.waitKey(1) & 0xFF 
    
    # 'X' 버튼으로 정상 종료 가능하도록 처리
    if cv.getWindowProperty('Paint', cv.WND_PROP_VISIBLE) < 1:
        break
        
    if key == ord('q'): # 'q' 키 누르면 종료
        break 
    elif key == ord('+') or key == ord('='): 
        brush_size = min(15, brush_size + 1) # 붓 크기 증가 (최대 15)
    elif key == ord('-'): 
        brush_size = max(1, brush_size - 1) # 붓 크기 감소 (최소 1)

cv.destroyAllWindows()