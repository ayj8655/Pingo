import os
import glob
from PIL import Image
import tensorflow as tf
import numpy as np

model = tf.keras.models.load_model("./models/pingo_256_500_0.981_0.099.h5")
IMG_SIZE = (300, 300)
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
path = "./datasets/pingo_test"


all_image_files = glob.glob(path + "/*.png")
print("---------------------모든이미지파일--------------------------")
print(all_image_files)

for file_path in all_image_files:  # 모든 png파일 경로에 대하여
    img = tf.keras.preprocessing.image.load_img(
        file_path, target_size=IMG_SIZE, color_mode="rgb"
    )
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)

    predictions = model(img_array)
    directories = file_path.split("\\")

    print(
        "{:.10}를 예상한 결과 => {} 신뢰도 {:.2f}%".format(
            directories[1],
            class_names[np.argmax(predictions[0])],
            100 * np.max(predictions[0]),
        )
    )
