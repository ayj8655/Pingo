from datetime import datetime
import os
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from PIL import Image

# Req. 2-2	세팅 값 저장


def save_config(args):

 #   print(args.images_folder_path)
 #   print(args.caption_file_path)

    img_path = args.images_folder_path
    captions_path = args.caption_file_path
    train_split = args.train_split
    do_traning = args.do_traning
    sampling_split = args.sampling_split
    return img_path, captions_path, train_split, do_traning, sampling_split


# Req. 4-1	이미지와 캡션 시각화
def visualize_img_caption(img_paths, caption):

    #   print(caption[0])
    s = (caption[0])[2:-1]
#   print("S출력 : "+s)
    S = s.split('\',')
#   print("스플리한거 : " + S[0])
    print("<start> " + S[0] + " <end>")

    image = Image.open("./datasets/images/"+img_paths[0])

    plt.figure(figsize=(10, 8))  # 보여지는 크기 조정
    plt.title("<start> " + S[0] + " <end>")  # 타이틀 설정
    plt.imshow(np.asarray(image))  # 이미지 지정
    plt.show()
