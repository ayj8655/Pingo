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
    return img_path, captions_path, train_split, do_traning


# Req. 4-1	이미지와 캡션 시각화
def visualize_img_caption(image_input, caption_input):

    print("<start> " + caption_input + " <end>")
    image = Image.open(image_input)
    plt.title("<start> " + caption_input + " <end>")
    plt.imshow(np.asarray(image))
    plt.show()

    pass


def load_image(image_path):
    image = Image.open(image_path).convert('RGB')
    image = image.resize([224, 224], Image.LANCZOS)

    return image
