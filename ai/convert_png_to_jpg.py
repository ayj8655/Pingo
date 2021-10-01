import os
import glob
from PIL import Image
import tensorflow as tf
import numpy as np


def classfication_image(path, target):
    img = tf.keras.preprocessing.image.load_img(
        path, target_size=IMG_SIZE, color_mode="rgb"
    )

    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)

    predictions = new_model.predict(img_array)
    score = tf.nn.softmax(predictions[0])

    print(predictions)
    print("-------------------------------------")
    print(predictions[0])
    print("-------------------------------------")
    print(score)
    print("-------------------------------------")

    print(
        "원본은 banana 추측은 {} with a {:.2f} percent confidence.".format(
            class_names[np.argmax(score)], 100 * np.max(score)
        )
    )

    if target == class_names[np.argmax(score)]:
        return 1
    else:
        return 222222


def convert_png_to_jpg_save(path):
    # jpg파일을 저장하기 위한 디렉토리의 생성

    file_list = os.listdir(path)

    print(file_list)

    for folder_path in file_list:

        if not os.path.exists("./datas/" + folder_path + "_jpg"):
            os.mkdir("./datas/" + folder_path + "_jpg")

        # 모든 png 파일의 절대경로를 저장
        # all_image_files = glob.glob(path + "/*.png")
        all_image_files = glob.glob("./datas/" + folder_path + "/*.png")
        print("---------------------모든이미지파일--------------------------")
        print(all_image_files)

        for file_path in all_image_files:  # 모든 png파일 경로에 대하여

            # result = classfication_image(file_path, "t-shirt")
            result = 1
            if result == 1:
                img = Image.open(file_path).convert("RGB")  # 이미지를 불러온다.

                directories = file_path.split("/")  # 절대경로상의 모든 디렉토리를 얻어낸다.\
                directories = file_path.split("\\")  # 절대경로상의 모든 디렉토리를 얻어낸다.\
                print(directories)

                directories[-2] += "_jpg"  # 저장될 디렉토리의 이름 지정

                print(directories)
                temp = directories[-1].split(".")
                print(temp)

                directories[-1] = temp[0] + ".jpg"  # 저장될 파일의 이름 지정
                print("-----------아래가 -0 -----------------------")
                print(directories[-1])

                print(directories)

                save_filepath = "/".join(directories)  # 절대경로명으로 바꾸기

                print(save_filepath)

                img.save(save_filepath, quality=100)  # jpg파일로 저장한다.


def convert_png_to_jpg(path, class_name):
    # jpg파일을 저장하기 위한 디렉토리의 생성
    if not os.path.exists(path + "/" + class_name + "_ai"):
        os.mkdir(path + "/" + class_name + "_ai")

    # 모든 png 파일의 절대경로를 저장
    # all_image_files = glob.glob(path + "/*.png")
    all_image_files = glob.glob(path + "/" + class_name + "/*.jpg")

    for file_path in all_image_files:  # 모든 png파일 경로에 대하여

        result = classfication_image(file_path, class_name)

        if result == 1:
            img = Image.open(file_path).convert("RGB")  # 이미지를 불러온다.

            directories = file_path.split("/")  # 절대경로상의 모든 디렉토리를 얻어낸다.\
            directories = file_path.split("\\")  # 절대경로상의 모든 디렉토리를 얻어낸다.\
            print(directories)

            directories[-2] += "_ai"  # 저장될 디렉토리의 이름 지정

            print(directories)
            temp = directories[-1].split(".")
            print(temp)

            directories[-1] = temp[0] + ".jpg"  # 저장될 파일의 이름 지정
            print("-----------아래가 -0 -----------------------")
            print(directories[-1])

            print(directories)

            save_filepath = "/".join(directories)  # 절대경로명으로 바꾸기

            print(save_filepath)

            img.save(save_filepath, quality=100)  # jpg파일로 저장한다.


# new_model = tf.keras.models.load_model("pingo_0.948_0.366.h5")
new_model = tf.keras.models.load_model("pingo_0.955_0.236.h5")

IMG_SIZE = (100, 100)
class_names = [
    "banana",
    "bulb",
    "calculator",
    "carrot",
    "clock",
    "crescent",
    "diamond",
    "icecream",
    "strawberry",
    "t-shirt",
]


path = "./datas"

# for class_name in class_names:
# convert_png_to_jpg(path, class_name)


# path = "./datas"
# convert_png_to_jpg_save(path)
# --------------------------------------------------------

