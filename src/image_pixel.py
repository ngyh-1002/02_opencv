import cv2

# 이미지 로드
img = cv2.imread('../img/noah-buscher-0WFUP_y4tds-unsplash.jpg')
  

# 클릭 이벤트 함수
def get_pixel(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        b, g, r = img[y, x]
        print(f'Clicked at ({x}, {y}) - R: {r}, G: {g}, B: {b}')

# 윈도우 생성
cv2.namedWindow('Image')
cv2.setMouseCallback('Image', get_pixel)

while True:
    cv2.imshow('Image', img)
    if cv2.waitKey(1) & 0xFF == 27:  # ESC 키 종료
        break

cv2.destroyAllWindows()