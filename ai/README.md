# 인공지능(영상) CNN



클래스 10개 → 이유는 직접 데이터를 모아야했기 때문에 축소함

→ 어느정도 모델 성능이 나온 이후에는 크롤링한 이미지 대상으로 분류해서나온 이미지로 다시 학습

아래 3개는 에포크 100개로 동일


<img src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/94d9e97c-7448-41c8-afbd-fd6445657d0a/pingo_32_100_0.672_1.613.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20211008%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20211008T004003Z&X-Amz-Expires=86400&X-Amz-Signature=29e72a223c216b00474c1e9edd8a8ca120157cf7f4fa54b065289f68d1e54a01&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22pingo_32_100_0.672_1.613.png%22" width="500" height="500">


클래스당 100개의 데이터와 초기 모델

- accuracy = 0.672
- loss = 1.613


![Untitled](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/5263535e-2f45-4e37-b95c-60727ad5d07c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20211008%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20211008T004032Z&X-Amz-Expires=86400&X-Amz-Signature=b4a3c181b00b49cbc5f1f5798f6cf52db28fe9cbcbc0344ff6eeaca00bd93b6f&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22)

---

<img src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/5f3e8839-95aa-4f30-9eb0-becd3643e4cd/pingo_128_100_0.803_0.723.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20211008%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20211008T004148Z&X-Amz-Expires=86400&X-Amz-Signature=043c082d2ac6f0d593de943b02359a2c3e6df1524a7d2c54be62b931feabfb96&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22pingo_128_100_0.803_0.723.png%22" width="500" height="500">

클래스당 600개의 데이터와 기존 모델


- accuracy = 0.80
- loss = 0.722



![Untitled](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/9e6cd1d5-afb5-46c5-8b79-5b144c5b04a5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20211008%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20211008T004156Z&X-Amz-Expires=86400&X-Amz-Signature=79c33ae6f0e3ae61e52d9ac82a32056b146cf464f272701eedeebe667029f3e6&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22)

---

<img src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/cd4be447-077e-4f88-802b-8ac31feaeb2f/pingo_256_100_0.967_0.111.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20211008%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20211008T004204Z&X-Amz-Expires=86400&X-Amz-Signature=3f0581b2a0122d1e8bf67d853cbf952829573b126b3193c0df3ffd0acfa74da8&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22pingo_256_100_0.967_0.111.png%22" width="500" height="500">



클래스당 약 1000개의 데이터와 개선된 모델

- accuracy = 0.967
- loss = 0.111

![Untitled](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/75a866d7-c6f9-4390-8ef4-709d0c3401d3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20211008%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20211008T004242Z&X-Amz-Expires=86400&X-Amz-Signature=3a555ed5e85cc74a0279a5b6e098c0e21f33076fce9581af3b1c11749d067d38&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22)



---


### 용어 정리

지도 학습 : 정답을 주고 학습시키는 머신러닝의 방법론

- 입력데이터에 라벨링이 되어 있고 출력값으로 사상되는 함수(활성화함수)를 학습하여 성
능을 향상시키는 방향
- 분류 (Classification)
- 회귀 (Regression)
- 비지도학습

비지도 학습 : 정답없는 데이터를 어떻게 구성되었는지를 알아내는 머신러닝의 학습 방법론

- 입력데이터는 라벨링이 되어있지 않고 입력된 패턴의 공통적인 특성을 파악하는 것이 목적
- **군집** : 그룹핑 (비슷한 데이터들끼리 묶어주는 기능)
- **특징** : 특징 도출

과적합 (Overfitting) : 학습 데이터에 너무 최적화를 하다보니, 실제 데이터와 차이가 많이 발생하는 모델 생성

---

경사하강법

1. 정의
    - 손실 함수가 정의되었을 때, 손실 함수의 값이 최소가 되는 지점
    - MSE(평균제곱오차/손실함수)를 가중치(weight)에 대한 미분 값이 감소하는 방향으로 가중치를 업데이트하여 손실 함수의 최소값을 찾음
2. 배치 (Batch)
    - Total Trainning Dataset
    - 단일 반복에서 기울기를 계산하는 데 사용하는 예의 총 개수
    - 전체 데이터 셋에 대해 에러를 구한 뒤 기울기를 한번만 계산하여 모델의 파라미터를 업데이트 하는 방식
    - 배치가 너무 커지면 단일 반복으로 계산하는데 오랜 시간 걸림

---

신경망 (Neural Network) → 사람의 두뇌 모양을 흉내내서 만든 모델

- 수많은 노드들과 각 노드들간의 가중치로 이루어져 있습니다
- 학습 데이터를 이용해 학습하면서 그 결과값에 따라 각 노드들간의 가중치를 조금 변경하며 학습

epoch → 학습 데이터를 한번씩 모두 학습시킨 횟수

활성화 함수 (Activation Function)

- 출력값을 활성화를 일으키게 할 것이냐를 결정하고, 그 값을 부여하는 함수
- 시그모이드 함수 (Sigmoid)
- ReLU 함수 (Rectified Linear Unit)
- Step Function

손실 함수 (Loss Function) 

- 예측값과 정답 사이의 오차를 정의하는 함수
- 머신러닝의 목적은 오차의 합을 최소화하여 최적의 결과 값을 도출하는 것
- 비용 함수 (cost function) 또는 목적 함수 (object function)

최적화 함수 (optimization)

![optimization](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/d379b2fc-3c6b-4487-bece-54476a825b98/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20211008%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20211008T003418Z&X-Amz-Expires=86400&X-Amz-Signature=5203b5342fe791ade9c5c139a48fdc5a7758796cd9d9ee1709c91371b88417db&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22)

---

# 종류

### CNN (합성곱 신경망, Convolutional Neural Network)

인간의 시신경구조 모방한 vision처리 수행모델
이미지 인식, 컴퓨터비젼

여러 이미지 데이터 불러오기

### RNN (Recurrent Neural Network)

은닉층에서 출력층간 데이터의 저장 및 흐름 가능한 신경망
언어모델링, 기계번역, 이미지캡션생성

---

# 개발환경

### 로컬

아나콘다 3.7

- conda create -n ai python=3.7

- conda activate ai

- ~~conda install git matplotlib scikit-learn tqdm scipy numpy tensorflow-gpu==2.3.0~~

- conda install git matplotlib scikit-learn tqdm scipy numpy=1.19 tensorflow-gpu==2.4.1

### 개발서버

- conda install git matplotlib scikit-learn tqdm scipy numpy=1.19 tensorflow-gpu==2.4.1

- 모델 학습할 때 데이터증강하는데 해당 에러 발생시 (NotImplementedError: Cannot convert a symbolic Tensor to a numpy array) -> 이 에러는 numpy 1.20 버전일 때 발생한다고 한다. → pip install numpy==1.19.5

---

텐서플로우 (Tensorflow 2.1 or 최신버전) GPU 사용하기-설치

[https://neosla.tistory.com/57](https://neosla.tistory.com/57)

[https://itkmj.blogspot.com/2019/12/tensorflow-gpu.html](https://itkmj.blogspot.com/2019/12/tensorflow-gpu.html)

[https://m.blog.naver.com/haanoon/221811007221](https://m.blog.naver.com/haanoon/221811007221)

[https://www.tensorflow.org/install/source#gpu_support_3](https://www.tensorflow.org/install/source#gpu_support_3)

아나콘다 가상환경을 이용해 딥러닝 개발 환경 만들기 (gpu용)

[https://sincerechloe.tistory.com/44](https://sincerechloe.tistory.com/44)

Could not load 'cudart64_110.dll';

[https://deep-deep-deep.tistory.com/71](https://deep-deep-deep.tistory.com/71)

아나콘다 가상환경 삭제

[https://leebaro.tistory.com/entry/anaconda에서-가상환경-삭제하기](https://leebaro.tistory.com/entry/anaconda%EC%97%90%EC%84%9C-%EA%B0%80%EC%83%81%ED%99%98%EA%B2%BD-%EC%82%AD%EC%A0%9C%ED%95%98%EA%B8%B0)

---

케라스 Fashion-Mnist 분류

[https://sdc-james.gitbook.io/onebook/4.-and/5.4.-tensorflow/5.4.3.-fashion-mnist-with-keras](https://sdc-james.gitbook.io/onebook/4.-and/5.4.-tensorflow/5.4.3.-fashion-mnist-with-keras)

2개 클래스 분류

[https://codetorial.net/tensorflow/classifying_the_cats_and_dogs.html](https://codetorial.net/tensorflow/classifying_the_cats_and_dogs.html)

다중 클래스 분류

[https://codetorial.net/tensorflow/multiclass_classification.html](https://codetorial.net/tensorflow/multiclass_classification.html)

케라스 문서 번역 프로젝트

[https://github.com/KerasKorea/KEKOxTutorial](https://github.com/KerasKorea/KEKOxTutorial)

### **다중 클래스 이미지분류 베이스코드**

[https://wiserloner.tistory.com/1244](https://wiserloner.tistory.com/1244)

image_dataset_from_directory

[https://keras.io/api/preprocessing/image/](https://keras.io/api/preprocessing/image/)

초기 신뢰도 표시하는 방법

[https://www.tensorflow.org/tutorials/images/classification?hl=ko#새로운_데이터로_예측하기](https://www.tensorflow.org/tutorials/images/classification?hl=ko#%EC%83%88%EB%A1%9C%EC%9A%B4_%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%A1%9C_%EC%98%88%EC%B8%A1%ED%95%98%EA%B8%B0)



남자여자분류 

[https://crystalcube.co.kr/192](https://crystalcube.co.kr/192)

---

## 데이터 증강 (augmentation)

데이터 증강 - 케라스 전처리 레이어 사용

[https://www.tensorflow.org/tutorials/images/data_augmentation?hl=ko#keras_전처리_레이어_사용하기](https://www.tensorflow.org/tutorials/images/data_augmentation?hl=ko#keras_%EC%A0%84%EC%B2%98%EB%A6%AC_%EB%A0%88%EC%9D%B4%EC%96%B4_%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0)

텐서플로우 data api로 성능 향상시키기

[https://www.tensorflow.org/guide/data_performance?hl=ko](https://www.tensorflow.org/guide/data_performance?hl=ko)

- (1) cache = preprocessing 시간이 너무 길어서 줄이고 싶을때 사용

- (2) shuffle = 데이터 셔플링, 숫자를 데이터 갯수만큼 설정하면 완전히 랜덤하게 셔플링, 그 이상 설정해도 똑같음. 다만 적게 설정할경우 셔플링이 완전하게 잘 되지 않은 특징

- (3) prefetch = 학습중일때, 데이터 로드시간을 줄이기 위해 미리 메모리에 적재시킴 이때, 괄호안의 숫자는 얼마만큼 적재시킬지에 대한 숫자

- (4) tf.data.experimental.AUTOTUNE = 네트워크가 알아서 설정해라

작은 데이터셋으로 강력한 이미지 분류 모델 설계하기 → 데이터 증강 관련

[https://keraskorea.github.io/posts/2018-10-24-little_data_powerful_model/](https://keraskorea.github.io/posts/2018-10-24-little_data_powerful_model/)

---

## Loss 함수 비교

Keras에서 Loss 함수 - sparse_categorical_crossentropy / categorical_crossentropy / binary_crossentropy 비교 → [https://hororolol.tistory.com/375](https://hororolol.tistory.com/375)

[tf.keras] loss function sparse_categorical_crossentropy categorical_crossentropy 차이

[https://ehdrn463.tistory.com/13](https://ehdrn463.tistory.com/13)

[https://ahnjg.tistory.com/88](https://ahnjg.tistory.com/88)

[https://welcome-to-dewy-world.tistory.com/96](https://welcome-to-dewy-world.tistory.com/96)

[https://crazyj.tistory.com/153](https://crazyj.tistory.com/153)

---

## 아래는 이미지 크롤링 관련

셀레니움 설치하기

[https://chancoding.tistory.com/136](https://chancoding.tistory.com/136)

셀레니움 이용 이미지 크롤링

[https://yobbicorgi.tistory.com/31?category=478264](https://yobbicorgi.tistory.com/31?category=478264)

리눅스 압축파일 관리

[https://araikuma.tistory.com/120](https://araikuma.tistory.com/120)

.py 백그라운드 실행

[https://suyeoniii.tistory.com/80](https://suyeoniii.tistory.com/80)
