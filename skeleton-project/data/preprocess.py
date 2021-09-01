import os
import csv
import numpy as np
import pandas as pd
import random  # 나중에 데이터셋 섞어야되면 이거 쓸라고

# img_DIR = './datasets/images'
# cap_DIR = './datasets/captions.csv'

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

# 리스트를 원하는 간격으로 나누는 메소드 -> https://jsikim1.tistory.com/141


def list_chunk(lst, n):
    return [lst[i:i+n] for i in range(0, len(lst), n)]

# Req. 3-2	전체 데이터셋을 분리해 저장하기


def dataset_split_save(img_paths, captions, train_split):

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
    # 위는 리스트로 하는건데 아래부터 딕셔너리로 다시 할 예정

    print('입력된 트레이닝데이터셋 % : ' + str(train_split) + "% 입니당 ㅎㅎ")

    print("기본 캡션 : " + str(captions[:5]))
    list_chunked = list_chunk(captions, 5)
    print("5개씩 나눈 캡션 " + str(list_chunked[:5]))

    # for문으로 하니까 너무 느려서 아래 방법으로함
    # new_list = []
    # for v in img_paths:
    #     if v not in new_list:
    #         new_list.append(v)

    result1 = dict.fromkeys(img_paths)  # 리스트 값들을 key 로 변경 -> 중복 제거
    result2 = list(result1)  # list(dict.fromkeys(arr)) -> 리스트로 변경

    dic = dict(zip(result2, list_chunked))  # 중복이 제거된 리스트들로 다시 딕셔너리 생성

    # 만든 딕셔너리를 셔플 -> 셔플하면 리스트로 바뀜
    dic = sorted(dic.items(), key=lambda x: random.random())

    split_size = len(dic) * (train_split/100)
    print('나눈 크기는 : ' + str(split_size))

    # 섞인 딕셔너리를 스플릿사이즈에 맞게 나누어 트레이닝과 테스트로 나눔
    train_tt = dic[:int(split_size)]
    test_tt = dic[int(split_size):]

    print("트레이닝 : " + str(train_tt[:5]))
    print("테스트 : " + str(test_tt[:5]))

    # 나누어진 데이터를 csv 파일로 저장
    # https://www.delftstack.com/ko/howto/python/write-list-to-csv-python/
    df = pd.DataFrame(train_tt)
    df.to_csv('./datasets/train_val.csv', sep=",")

    df = pd.DataFrame(test_tt)
    df.to_csv('./datasets/test_val.csv', sep=",")

    train_dataset_path = './datasets/train_val.csv'
    val_dataset_path = './datasets/test_val.csv'
    return train_dataset_path, val_dataset_path


# Req. 3-3	저장된 데이터셋 불러오기
def get_data_file(do_traning, train_dataset_path, val_dataset_path):

    if do_traning:
        print("참입니당")

        csv = pd.read_csv(train_dataset_path,
                          sep=",", skiprows=1,
                          names=['0', '1'])

        img_paths = []
        captions = []
        img_paths = csv['0'].values.tolist()
        captions = csv['1'].values.tolist()
        # print(img_paths.values.tolist())
        # print(captions.values.tolist())

        print("이미지만나와야함 : " + str(img_paths[0]))
        print("캡션만나와야함 : " + str(captions[0]))

        return img_paths, captions

    else:
        print("거짓입니당")
        csv = pd.read_csv(val_dataset_path,
                          sep=",", skiprows=1,
                          names=['0', '1'])

        img_paths = []
        captions = []
        img_paths = csv['0'].values.tolist()
        captions = csv['1'].values.tolist()
        # print(img_paths.values.tolist())
        # print(captions.values.tolist())

        print("이미지만나와야함 : " + str(img_paths[0]))
        print("캡션만나와야함 : " + str(captions[0]))
        return img_paths, captions


# Req. 3-4	데이터 샘플링
def sampling_data(train_split):

    pass
