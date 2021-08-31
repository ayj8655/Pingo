from datetime import datetime
import os
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf


# Req. 2-2	세팅 값 저장
def save_config(args):

 #   print(args.images_folder_path)
 #   print(args.caption_file_path)

    img_path = args.images_folder_path
    captions_path = args.caption_file_path
    train_split = args.train_split
    return img_path, captions_path, train_split


# Req. 4-1	이미지와 캡션 시각화
def visualize_img_caption():
    pass
