import cv2
import numpy as np
import matplotlib.pyplot as plt

# 이미지 경로 설정
mirror_image_path = '../img/noah-buscher-0WFUP_y4tds-unsplash.jpg'  # 거울 이미지
cat_image_path = '../img/kari-shea-FilM6ng7VGQ-unsplash.jpg'         # 고양이 이미지

# 이미지 불러오기
mirror_img = cv2.imread(mirror_image_path)
cat_img = cv2.imread(cat_image_path)

# BGR → RGB
mirror_img_rgb = cv2.cvtColor(mirror_img, cv2.COLOR_BGR2RGB)
cat_img_rgb = cv2.cvtColor(cat_img, cv2.COLOR_BGR2RGB)

# 거울 중심 좌표와 반지름 (앞서 검출한 값 사용)
x, y, r = 1090, 1480, 330
diameter = 2 * r

# 고양이 이미지 리사이즈
cat_resized = cv2.resize(cat_img_rgb, (diameter, diameter))

# 원형 마스크 생성
mask = np.zeros((diameter, diameter), dtype=np.uint8)
cv2.circle(mask, (r, r), r, 255, -1)

# ROI 설정 (거울 부분)
roi = mirror_img_rgb[y - r:y + r, x - r:x + r]

# 고양이 이미지와 배경 합성
masked_cat = cv2.bitwise_and(cat_resized, cat_resized, mask=mask)
masked_bg = cv2.bitwise_and(roi, roi, mask=cv2.bitwise_not(mask))
combined = cv2.add(masked_cat, masked_bg)

# 최종 이미지에 삽입
result = mirror_img_rgb.copy()
result[y - r:y + r, x - r:x + r] = combined
def onclick(event):
    x, y = int(event.xdata), int(event.ydata)
    print(f"클릭한 좌표: ({x}, {y}) - RGB: {result[y, x]}")

fig, ax = plt.subplots(figsize=(8, 10))
ax.imshow(result)
cid = fig.canvas.mpl_connect('button_press_event', onclick)
plt.title("Click on the mirror")
plt.show()

# 출력
plt.figure(figsize=(8, 10))
plt.imshow(result)
plt.axis("off")
plt.title("Cat Inserted into Mirror")
plt.show()