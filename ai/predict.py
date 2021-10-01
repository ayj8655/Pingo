import os
import glob
from PIL import Image
import tensorflow as tf
import numpy as np

model = tf.keras.models.load_model("pingo_96_28.h5")
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

test_path = "./datasets/pingo/crescent_test.png"
img = tf.keras.preprocessing.image.load_img(
    test_path, target_size=IMG_SIZE, color_mode="grayscale"
)

img_array = tf.keras.preprocessing.image.img_to_array(img)
img_array = tf.expand_dims(img_array, 0)

predictions = model.predict(img_array)
score = tf.nn.softmax(predictions[0])

print(predictions)
print(predictions[0])
print(score)


print(
    "원본은 banana 추측은 {} with a {:.2f} percent confidence.".format(
        class_names[np.argmax(score)], 100 * np.max(score)
    )
)
