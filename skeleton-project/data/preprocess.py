import os
import csv
import numpy as np
import pandas as pd
import random  # 나중에 데이터셋 섞어야되면 이거 쓸라고

#img_DIR = './datasets/images'
#cap_DIR = './datasets/captions.csv'

# Req. 3-1	이미지 경로 및 캡션 불러오기


def get_path_caption(img_path, captions_path):
    img_DIR = img_path
    cap_DIR = captions_path

    # 아래는 기본적인 csv 파일 읽기로 했던건데 자르는게 힘들어서 패스
    # file = open(cap_DIR, 'r')
    # csvfile = csv.reader(file)
    # lists = []
    # for item in csvfile:
    #     lists.append(item)
    # print(lists)
    # file.close()

    # 판다스 이용해서 파일 읽어오고 잘라버림
    # 한글인코딩, csv파일의 구분자, 맨윗줄 제거
    csv = pd.read_csv(cap_DIR, encoding="cp949",
                      sep="|", skiprows=1,
                      names=['image_name', 'comment_number', 'comment'])

    img_paths = csv['image_name'].values.tolist()
    captions = csv['comment'].values.tolist()
    # print(img_paths.values.tolist())
    # print(captions.values.tolist())

    return img_paths, captions


# Req. 3-2	전체 데이터셋을 분리해 저장하기
def dataset_split_save(img_paths, captions, train_split):
    print('입력된 트레이닝데이터셋 % : ' + str(train_split) + "% 입니당 ㅎㅎ")
    split_size = len(img_paths) * (train_split/100)
    print('나눈 크기는 : ' + str(split_size))

    #  나중에 섞어야되면 여기서 섞는게 좋을거같기도하고
    # random.shuffle(img_paths)
    # random.shuffle(captions)
    #  각각 퍼센트기준으로 나뉜 트레이닝,테스트 데이터 리스트들
    # train_img = img_paths[:int(split_size)]
    # test_img = img_paths[int(split_size):]
    # train_captions = captions[:int(split_size)]
    # test_captions = captions[int(split_size):]

    # print(len(train_img))
    # print(len(test_img))
    # 이제 얘들을 저장해야함.

    train_dataset_path = ''
    val_dataset_path = ''
    return train_dataset_path, val_dataset_path


# Req. 3-3	저장된 데이터셋 불러오기
def get_data_file():
    pass


# Req. 3-4	데이터 샘플링
def sampling_data():
    pass
