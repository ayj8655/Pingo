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

test_path = "./datasets/pingo/banana_test.png"
img = tf.keras.preprocessing.image.load_img(
    test_path, target_size=IMG_SIZE, color_mode="rgb"
)

img_array = tf.keras.preprocessing.image.img_to_array(img)
img_array = tf.expand_dims(img_array, 0)

predictions = model.predict(img_array)

print(
    "원본은 banana 추측은 {} with a {:.2f} percent confidence.".format(
        class_names[np.argmax(predictions[0])], 100 * np.max(predictions[0])
    )
)
test_path = "./datasets/pingo/bulb_test.png"
img = tf.keras.preprocessing.image.load_img(
    test_path, target_size=IMG_SIZE, color_mode="rgb"
)

img_array = tf.keras.preprocessing.image.img_to_array(img)
img_array = tf.expand_dims(img_array, 0)

predictions = model.predict(img_array)

print(
    "원본은 bulb 추측은 {} with a {:.2f} percent confidence.".format(
        class_names[np.argmax(predictions[0])], 100 * np.max(predictions[0])
    )
)
test_path = "./datasets/pingo/calculator_test.png"
img = tf.keras.preprocessing.image.load_img(
    test_path, target_size=IMG_SIZE, color_mode="rgb"
)

img_array = tf.keras.preprocessing.image.img_to_array(img)
img_array = tf.expand_dims(img_array, 0)

predictions = model.predict(img_array)

print(
    "원본은 calculator 추측은 {} with a {:.2f} percent confidence.".format(
        class_names[np.argmax(predictions[0])], 100 * np.max(predictions[0])
    )
)
test_path = "./datasets/pingo/carrot_test.png"
img = tf.keras.preprocessing.image.load_img(
    test_path, target_size=IMG_SIZE, color_mode="rgb"
)

img_array = tf.keras.preprocessing.image.img_to_array(img)
img_array = tf.expand_dims(img_array, 0)

predictions = model.predict(img_array)

print(
    "원본은 carrot 추측은 {} with a {:.2f} percent confidence.".format(
        class_names[np.argmax(predictions[0])], 100 * np.max(predictions[0])
    )
)
test_path = "./datasets/pingo/clock_test.png"
img = tf.keras.preprocessing.image.load_img(
    test_path, target_size=IMG_SIZE, color_mode="rgb"
)

img_array = tf.keras.preprocessing.image.img_to_array(img)
img_array = tf.expand_dims(img_array, 0)

predictions = model.predict(img_array)

print(
    "원본은 clock 추측은 {} with a {:.2f} percent confidence.".format(
        class_names[np.argmax(predictions[0])], 100 * np.max(predictions[0])
    )
)
test_path = "./datasets/pingo/crescent_test.png"
img = tf.keras.preprocessing.image.load_img(
    test_path, target_size=IMG_SIZE, color_mode="rgb"
)

img_array = tf.keras.preprocessing.image.img_to_array(img)
img_array = tf.expand_dims(img_array, 0)

predictions = model.predict(img_array)

print(
    "원본은 crescent 추측은 {} with a {:.2f} percent confidence.".format(
        class_names[np.argmax(predictions[0])], 100 * np.max(predictions[0])
    )
)
test_path = "./datasets/pingo/diamond_test.png"
img = tf.keras.preprocessing.image.load_img(
    test_path, target_size=IMG_SIZE, color_mode="rgb"
)

img_array = tf.keras.preprocessing.image.img_to_array(img)
img_array = tf.expand_dims(img_array, 0)

predictions = model.predict(img_array)

print(
    "원본은 diamond 추측은 {} with a {:.2f} percent confidence.".format(
        class_names[np.argmax(predictions[0])], 100 * np.max(predictions[0])
    )
)
test_path = "./datasets/pingo/icecream_test.png"
img = tf.keras.preprocessing.image.load_img(
    test_path, target_size=IMG_SIZE, color_mode="rgb"
)

img_array = tf.keras.preprocessing.image.img_to_array(img)
img_array = tf.expand_dims(img_array, 0)

predictions = model.predict(img_array)

print(
    "원본은 icecream 추측은 {} with a {:.2f} percent confidence.".format(
        class_names[np.argmax(predictions[0])], 100 * np.max(predictions[0])
    )
)
test_path = "./datasets/pingo/strawberry_test.png"
img = tf.keras.preprocessing.image.load_img(
    test_path, target_size=IMG_SIZE, color_mode="rgb"
)

img_array = tf.keras.preprocessing.image.img_to_array(img)
img_array = tf.expand_dims(img_array, 0)

predictions = model.predict(img_array)

print(
    "원본은 strawberry 추측은 {} with a {:.2f} percent confidence.".format(
        class_names[np.argmax(predictions[0])], 100 * np.max(predictions[0])
    )
)


test_path = "./datasets/pingo/t-shirt_test.png"
img = tf.keras.preprocessing.image.load_img(
    test_path, target_size=IMG_SIZE, color_mode="rgb"
)

img_array = tf.keras.preprocessing.image.img_to_array(img)
img_array = tf.expand_dims(img_array, 0)

predictions = model.predict(img_array)

print(
    "원본은 t-shirt 추측은 {} with a {:.2f} percent confidence.".format(
        class_names[np.argmax(predictions[0])], 100 * np.max(predictions[0])
    )
)
# print(predictions)
