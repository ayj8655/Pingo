import os
import csv
import numpy as np
import pandas as pd
import random  # 나중에 데이터셋 섞어야되면 이거 쓸라고
from sklearn.model_selection import train_test_split


# Req. 3-1	이미지 경로 및 캡션 불러오기


def get_path_caption(img_path, captions_path):
    img_DIR = img_path
    cap_DIR = captions_path

    # 판다스 이용해서 파일 읽어오고 잘라버림
    # 한글인코딩, csv파일의 구분자, 맨윗줄 제거
    csv = pd.read_csv(cap_DIR, encoding="cp949",
                      sep="|", skiprows=1,
                      names=['image_name', 'comment_number', 'comment'])

    img_paths = csv['image_name'].values.tolist()  # names에서 뽑아온 csv를 리스트로 변경
    captions = csv['comment'].values.tolist()
    # print(img_paths.values.tolist())
    # print(captions.values.tolist())

    return img_paths, captions


# Req. 3-2	전체 데이터셋을 분리해 저장하기


def dataset_split_save(img_paths, captions, train_split):

    print('입력된 트레이닝데이터셋 % : ' + str(train_split) + "%")

    #list3 = list(map(list.__add__, img_paths, captions))
    list3 = list(zip(img_paths, captions))
    # print(list3[:3])

    train_set, test_set = train_test_split(
        list3, test_size=0.2, shuffle=True, random_state=1)
    #print("train_set:", len(train_set))
    #print("test_set:", len(test_set))

    #print("test_set:", test_set[:3])

    df = pd.DataFrame(train_set)
    df.to_csv('./datasets/train_val.csv', sep=",")
    df = pd.DataFrame(test_set)
    df.to_csv('./datasets/test_val.csv', sep=",")

    train_dataset_path = './datasets/train_val.csv'
    val_dataset_path = './datasets/test_val.csv'
    return train_dataset_path, val_dataset_path


# Req. 3-3	저장된 데이터셋 불러오기
def get_data_file(do_traning, train_dataset_path, val_dataset_path):

    if do_traning:
        print("학습용데이터에요")

        csv = pd.read_csv(train_dataset_path,
                          sep=",", skiprows=1,
                          names=['0', '1'])

        img_paths = []
        captions = []
        img_paths = csv['0'].values.tolist()
        captions = csv['1'].values.tolist()
        print(img_paths[:5])
        print(captions[:5])

        print("이미지만나와야함 : " + str(img_paths[0]))
        print("캡션만나와야함 : " + str(captions[0]))

        return img_paths, captions

    else:
        print("테스트용 데이터입니당")
        csv = pd.read_csv(val_dataset_path,
                          sep=",", skiprows=1,
                          names=['0', '1'])

        img_paths = []
        captions = []
        img_paths = csv['0'].values.tolist()
        captions = csv['1'].values.tolist()
        # print(img_paths.values.tolist())
        # print(captions.values.tolist())

#        print("이미지만나와야함 : " + str(img_paths[0]))
#        print("캡션만나와야함 : " + str(captions[0]))
        return img_paths, captions


# Req. 3-4	데이터 샘플링
def sampling_data(img_paths, caption, sampling_split):

    print('입력된 트레이닝데이터셋 % : ' + str(sampling_split) + "%")

    print("전체 데이터 개수 : " + str(len(img_paths)))
    split_size = len(img_paths) * (sampling_split/100)
    #print('나눈 크기는 : ' + str(split_size))

    img_paths = img_paths[:int(split_size)]
    caption = caption[:int(split_size)]

    print("샘플링된 데이터 개수 : " + str(len(img_paths)))
    print("샘플링된 데이터 퍼센트 : " + str(sampling_split))
    return img_paths, caption
