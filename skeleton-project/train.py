
import pickle
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing import image
from data import preprocess
from utils import utils
import config


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#import keras
import os
import tensorflow as tf
# ----------------------------------------------------------------------------------------


# config 저장
img_path, captions_path, train_split, do_traning, sampling_split = utils.save_config(
    config.args)

train_dataset_path = './datasets/train_val.csv'
val_dataset_path = './datasets/test_val.csv'

# 이미지 경로 및 캡션 불러오기

img_paths, captions = preprocess.get_path_caption(img_path, captions_path)

print(len(img_paths), len(captions))

# 전체 데이터셋을 분리해 저장하기

train_dataset_path, val_dataset_path = preprocess.dataset_split_save(
    img_paths, captions, train_split)


# 저장된 데이터셋 불러오기 -> do_traning이 참이면 트레이닝데이터 불러오기 거짓이면 테스트데이터

img_paths, caption = preprocess.get_data_file(
    do_traning, train_dataset_path, val_dataset_path)


# 데이터 샘플링

if config.do_sampling:
    img_paths, caption = preprocess.sampling_data(
        img_paths, caption, sampling_split)

# 이미지와 캡션 시각화 하기

#utils.visualize_img_caption(img_paths, caption)

# 이미지 파일 로드

img_dir = './datasets/images/'
# print(len(os.listdir(img_dir)))
# print(os.listdir(img_dir)[:10])

img_name = '36979.jpg'
img_path = os.path.join(img_dir, img_name)
img = image.load_img(img_path, target_size=(250, 250))
img_tensor = image.img_to_array(img)
img_tensor = np.expand_dims(img_tensor, axis=0)
# scaling into [0, 1]
img_tensor /= 255.
# print(img_tensor[0])
# plt.rcParams['figure.figsize'] = (10, 10)  # set figure size
# plt.imshow(img_tensor[0])
# plt.show()


# 이미지 정규화 -> 방법을 못찾겠어서 일단 넘어감


# 텍스트 데이터 토큰화

# start랑 end 넣으라는데 왜 넣어야하는지 모르겠어서 일단 넘어감

tokenizer = Tokenizer(num_words=10000, oov_token="<UNK>")
tokenizer.fit_on_texts(caption)
word_dic = tokenizer.word_index

# print(word_dic)
print("--------------------------------")


sequences = tokenizer.texts_to_sequences(caption)  # 각 단어를 이미 정해진 인덱스로 변환
# print(sequences)
print("--------------------------------")
#padded = pad_sequences(sequences)
# print(padded)
print("--------------------------------")


# Tokenizer 저장 및 불러오기

# Tokenizer 저장
with open("./datasets/Tokenizer.pickle", "wb") as fw:
    pickle.dump(word_dic, fw)
# Tokenizer 불러오기
with open("./datasets/Tokenizer.pickle", "rb") as fr:
    word_index = pickle.load(fr)
    tokenizer.word_index = word_index
print(len(tokenizer.word_index))


# tf.data.Dataset 생성
dataset = tf.data.Dataset.from_tensor_slices((img_paths, caption))
print(dataset)

for i in dataset:
    print(i)
# Image Data Augmentation


# 손실함수 구현

# 1-batch train step 구현
