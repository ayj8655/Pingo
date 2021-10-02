import os
import glob
from PIL import Image
import tensorflow as tf
import numpy as np

model = tf.keras.models.load_model("./models/pingo_0.76_0.752.h5")
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

test_path = "./datasets/pingo/crescent_test.png"
img = tf.keras.preprocessing.image.load_img(
    test_path, target_size=IMG_SIZE, color_mode="rgb"
)

img_array = tf.keras.preprocessing.image.img_to_array(img)
img_array = tf.expand_dims(img_array, 0)

predictions = model.predict(img_array)
score = tf.nn.softmax(predictions[0])

print(
    "원본은 banana 추측은 {} with a {:.2f} percent confidence.".format(
        class_names[np.argmax(predictions[0])], 100 * np.max(predictions[0])
    )
)

print(predictions[0])
