# 관심영역 표시 (roi.py)

import cv2
import numpy as np

img = cv2.imread('../img/like_lenna.png')

x=320; y=150; w=50; h=50        # roi 좌표
roi = img[y:y+h, x:x+w]         # roi 지정        ---①
img2 = roi.copy()

img[y:y+h, x+w:x+w+w] = roi # 새로운 좌표에 roi추가

print(roi.shape)                # roi shape, (50,50,3)
#cv2.rectangle(roi, (0,0), (h-1, w-1), (0,255,0)) # roi 전체에 사각형 그리기 ---②
cv2.rectangle(img, (x,y), (x+w+w, y+h), (0,255,0))
cv2.imshow("img", img)
cv2.imshow("roi", img2)
key = cv2.waitKey(0)
print(key)
cv2.destroyAllWindows()