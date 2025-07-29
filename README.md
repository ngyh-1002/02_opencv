### 거울 속 고양이 🐱🖼️
이 프로젝트는 OpenCV와 Matplotlib을 활용하여 고양이 이미지를 거울 이미지의 원형 부분에 합성하는 파이썬 스크립트입니다.

## ✨ 주요 기능
* 이미지 불러오기 및 전처리: 거울 이미지와 고양이 이미지를 불러와 Matplotlib에서 올바르게 표시되도록 RGB 형식으로 변환합니다.

* 고양이 이미지 크기 조절: 고양이 이미지를 거울의 크기에 맞춰 조절하여 자연스러운 합성을 가능하게 합니다.

* 원형 마스킹 및 합성: 거울 영역에 대한 정확한 원형 마스크를 생성하고, 이를 이용해 고양이 이미지를 거울 배경에 부드럽게 합성합니다.

* 대화형 표시: 최종 합성된 이미지를 Matplotlib 창에 표시하며, 사용자가 이미지의 아무 곳이나 클릭하면 해당 픽셀의 **좌표 (x, y)**와 RGB 값을 실시간으로 출력합니다.

## 🚀 스크립트 설명
이 스크립트는 거울의 **중심 좌표 (x, y)**와 **반지름 (r)**을 기반으로 고양이 이미지를 합성합니다. 현재 이 값들은 스크립트 내에 하드코딩되어 있습니다. 사용하시는 이미지에 맞춰 이 값들을 조정해야 할 수 있습니다. 이미지 표시 창에서 직접 클릭하여 픽셀 정보를 확인하고, 이를 통해 정확한 좌표를 찾는 데 도움을 받을 수 있습니다.

### opencv 정리노트
## OpenCV 색상/채널 요약:

* 기본: BGR

* 투명도: BGRA (알파 채널)

* 변환:

  1. cv2.imread(): 이미지 읽기 (BGR, BGRA, Gray)
  2. cv2.cvtColor(): 색상 공간 변환 (BGR↔Gray, BGR↔HSV, BGR↔YUV 등)
  3. cv2.split(): 채널 분리

* 목적:

  1. Gray: 속도/효율, 특징 추출
  2. HSV: 색상 식별/추적
  3. YUV: 밝기 처리/압축

## OpenCV ROI (관심 영역) 요약

* 정의: 이미지/영상 내 사용자가 집중하는 특정 부분.

* 지정 방식:

  1. 수동: NumPy 슬라이싱 (img[y:y+h, x:x+w])으로 좌표/크기 직접 입력.

  2. 자동: cv2.selectROI() 함수 사용, 마우스 드래그로 시각적 선택 (마우스 이벤트 자동 처리).

* 주요 특징:

  1. 슬라이싱 ROI: 원본 이미지의 '뷰' (변경 시 원본 반영), 복사본 필요시 .copy() 사용.

  2. cv2.selectROI(): 대화형 선택 (Space/Enter 완료, 'c' 취소), (x, y, 너비, 높이) 반환.

* 활용: 특정 객체 추출/분석, 도형/효과 적용, 부분 복사/저장.

## OpenCV 스레시홀딩/오츠의 알고리즘/적응형 스레시홀딩 요약

*스레시홀딩(Thresholding): 이미지를 흑백(바이너리)으로 변환하는 대표적인 방법. 임계값을 기준으로 픽셀 값을 0 또는 value로 변경.

  1. 전역 스레시홀딩: 이미지 전체에 하나의 고정된 임계값 적용.

    - 메소드: cv2.threshold(img, threshold, value, type_flag)

    - type_flag: THRESH_BINARY, THRESH_BINARY_INV, THRESH_TRUNC, THRESH_TOZERO, THRESH_TOZERO_INV 등.

  2. 오츠의 알고리즘(Otsu's Method): 최적의 전역 임계값을 자동으로 찾아주는 방법. 명암 분포가 가장 균일할 때의 임계값 선택.

    -메소드: cv2.threshold(img, -1, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    -특징: threshold 값은 무시됨. 속도 느릴 수 있음.

  3. 적응형 스레시홀딩(Adaptive Thresholding): 이미지의 조명 불균형 등을 해결하기 위해, 이미지를 여러 영역으로 나누어 각 영역별로 임계값을 다르게 적용.

    -메소드: cv2.adaptiveThreshold(img, value, method, type_flag, block_size, C)

    -method: ADAPTIVE_THRESH_MEAN_C (이웃 평균), ADAPTIVE_THRESH_GAUSSIAN_C (가우시안 가중치 합).

    -특징: 전역 스레시홀딩보다 선명하고 잡티 적은 결과, 불균일한 조명에 강함 (일반적으로 더 많이 사용됨).

## OpenCV 비트와이즈 연산 요약

* 목적: 두 이미지 합성 시 특정 영역 선택/제외 등 선별적 연산.

* 원리: 픽셀 값을 비트(0=False, 0 외=True)로 변환하여 논리 연산 수행.

* 주요 함수:

  1. cv2.bitwise_and(img1, img2, mask=None): AND 연산 (두 이미지 겹치는 부분)

  2. cv2.bitwise_or(img1, img2, mask=None): OR 연산

  3. cv2.bitwise_xor(img1, img2, mask=None): XOR 연산

  4. cv2.bitwise_not(img1, mask=None): NOT 연산 (이미지 반전)

* 특징:

  1. img1, img2는 동일 shape 필수.

  2. mask 파라미터: 마스크의 0이 아닌 픽셀만 연산 적용.

  3. 활용: 이미지 마스킹(특정 모양 영역 추출 등).

## OpenCV 히스토그램, 정규화, 평탄화, CLAHE 요약

* 히스토그램: 이미지 픽셀 값 분포를 그래프로 나타낸 것 (색상/명암 분포 파악).

  - 메소드: cv2.calcHist(img, channel, mask, histSize, ranges)

  - 활용: 이미지 분석 (회색조 1채널, 컬러 3채널 등).

* 정규화(Normalization): 픽셀 값을 특정 구간으로 재조정하여 화질 개선 또는 이미지 간 조건 통일.

  - 메소드: cv2.normalize(src, dst, alpha, beta, type_flag)

  - type_flag: NORM_MINMAX, NORM_L1, NORM_L2, NORM_INF.

  - 목적: 픽셀 값 분포를 고르게 펴서 대비 개선.

* 평탄화(Equalization): 명암 대비가 낮은 이미지를 개선하기 위해 픽셀 분포를 전체 영역에 고르게 재분배.

  - 메소드: cv2.equalizeHist(src, dst)

  - 특징: 8비트 1채널 이미지에 적용. 컬러 이미지의 경우 YUV/HSV 밝기 채널에 적용 (예: img_yuv[:,:,0] = cv2.equalizeHist(img_yuv[:,:,0])).

  - 단점: 너무 밝은 부분이 날아갈 수 있음.

* CLAHE (Contrast Limited Adaptive Histogram Equalization): 일반 평탄화의 단점(밝은 부분 날아감, 노이즈)을 보완한 적응형 평탄화. 이미지를 영역으로 나누고 각 영역에 대비 제한(clipLimit)을 적용하여 평탄화.

  - 메소드: cv2.createCLAHE(clipLimit, tileGridSize) 객체 생성 후 clahe.apply(src).

  - 특징: 영역별 평탄화로 불균일한 조명에 강하며, 대비 제한으로 노이즈 및 밝은 부분 손실 완화.
 
