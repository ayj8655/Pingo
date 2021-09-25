import matplotlib.pylab as plt
import tensorflow as tf
import os
import numpy as np
import PIL.Image as Image

import tensorflow as tf
import os

# def validate_image(file_name):
#     tf.py_function(tf.print, inp=[file_name], Tout=[])
#     image = tf.io.read_file(file_name)
#     image = tf.io.decode_image(image, channels=3)
#     return image

# os.chdir(r'./datasets/pingo/banana')

# accepted_extensions = ('jpg', 'png', 'bmp', 'gif')

# files = list(filter(lambda x: x.lower().endswith(accepted_extensions), os.listdir()))

# ds = tf.data.Dataset.from_tensor_slices(files).map(validate_image)

# for i in ds:
#     pass

from tensorflow.python.client import device_lib

print(device_lib.list_local_devices())


os.environ["CUDA_VISIBLE_DEVICES"] = "0"
print(tf.__version__)

data_dir = "./datasets/pingo"
IMG_SIZE = (150, 150)
BATCH_SIZE = 16


train_dataset = tf.keras.preprocessing.image_dataset_from_directory(
    data_dir,
    validation_split=0.2,
    subset="training",
    seed=333,
    image_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    color_mode="grayscale",
)

validation_dataset = tf.keras.preprocessing.image_dataset_from_directory(
    data_dir,
    validation_split=0.2,
    subset="validation",
    seed=333,
    image_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    color_mode="grayscale",
)

class_names = train_dataset.class_names
print(class_names)

for image_batch, labels_batch in train_dataset:
    print(image_batch.shape)
    print(labels_batch.shape)
    break

AUTOTUNE = tf.data.experimental.AUTOTUNE

train_dataset = train_dataset.cache().shuffle(1000).prefetch(buffer_size=AUTOTUNE)
validation_dataset = validation_dataset.cache().prefetch(buffer_size=AUTOTUNE)

plt.figure(figsize=(10, 10))
for images, labels in train_dataset.take(1):
    for i in range(9):
        ax = plt.subplot(3, 3, i + 1)
        plt.imshow(images[i].numpy().astype("uint8"))
        plt.title(class_names[labels[i]])
        plt.axis("off")

# plt.show()


data_augmentation = tf.keras.Sequential(
    [
        tf.keras.layers.experimental.preprocessing.RandomFlip("horizontal"),
        tf.keras.layers.experimental.preprocessing.RandomRotation(0.2),
    ]
)

for image, _ in train_dataset.take(1):
    plt.figure(figsize=(10, 10))
    first_image = image[0]
    for i in range(9):
        ax = plt.subplot(3, 3, i + 1)
        augmented_image = data_augmentation(tf.expand_dims(first_image, 0))
        plt.imshow(augmented_image[0] / 255)
        plt.axis("off")
# plt.show()

preprocess_input = tf.keras.layers.experimental.preprocessing.Rescaling(scale=1.0 / 255)


model = tf.keras.models.Sequential(
    [
        tf.keras.layers.Conv2D(
            16, (3, 3), activation="relu", input_shape=(150, 150, 1)
        ),
        tf.keras.layers.MaxPooling2D(2, 2),
        tf.keras.layers.Dropout(0.25),
        tf.keras.layers.Conv2D(32, (3, 3), activation="relu"),
        tf.keras.layers.MaxPooling2D(2, 2),
        tf.keras.layers.Conv2D(64, (3, 3), activation="relu"),
        tf.keras.layers.MaxPooling2D(2, 2),
        tf.keras.layers.Conv2D(128, (3, 3), activation="relu"),
        tf.keras.layers.MaxPooling2D(2, 2),
        tf.keras.layers.Dropout(0.25),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(512, activation="relu"),
        tf.keras.layers.Dropout(0.5),
        tf.keras.layers.Dense(10, activation="softmax"),
    ]
)

model.summary()


model.compile(
    optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"]
)

initial_epochs = 10000
history = model.fit(
    train_dataset, validation_data=validation_dataset, epochs=initial_epochs
)

score = model.evaluate(validation_dataset)
print("loss=", score[0])  # loss
print("accuracy=", score[1])  # acc


predictions = model.predict(validation_dataset)


score = tf.nn.softmax(predictions[0])
print(
    "This image most likely belongs to {} with a {:.2f} percent confidence.".format(
        class_names[np.argmax(score)], 100 * np.max(score)
    )
)


test_path = "./datasets/pingo/banana_test.png"
img = tf.keras.preprocessing.image.load_img(
    test_path, target_size=(150, 150), color_mode="grayscale"
)

img_array = tf.keras.preprocessing.image.img_to_array(img)
img_array = tf.expand_dims(img_array, 0)

predictions = model.predict(img_array)
score = tf.nn.softmax(predictions[0])

print(
    "원본은 banana 추측은 {} with a {:.2f} percent confidence.".format(
        class_names[np.argmax(score)], 100 * np.max(score)
    )
)
test_path = "./datasets/pingo/bulb_test.png"
img = tf.keras.preprocessing.image.load_img(
    test_path, target_size=(150, 150), color_mode="grayscale"
)

img_array = tf.keras.preprocessing.image.img_to_array(img)
img_array = tf.expand_dims(img_array, 0)

predictions = model.predict(img_array)
score = tf.nn.softmax(predictions[0])

print(
    "원본은 bulb 추측은 {} with a {:.2f} percent confidence.".format(
        class_names[np.argmax(score)], 100 * np.max(score)
    )
)
test_path = "./datasets/pingo/calculator_test.png"
img = tf.keras.preprocessing.image.load_img(
    test_path, target_size=(150, 150), color_mode="grayscale"
)

img_array = tf.keras.preprocessing.image.img_to_array(img)
img_array = tf.expand_dims(img_array, 0)

predictions = model.predict(img_array)
score = tf.nn.softmax(predictions[0])

print(
    "원본은 calculator 추측은 {} with a {:.2f} percent confidence.".format(
        class_names[np.argmax(score)], 100 * np.max(score)
    )
)
test_path = "./datasets/pingo/carrot_test.png"
img = tf.keras.preprocessing.image.load_img(
    test_path, target_size=(150, 150), color_mode="grayscale"
)

img_array = tf.keras.preprocessing.image.img_to_array(img)
img_array = tf.expand_dims(img_array, 0)

predictions = model.predict(img_array)
score = tf.nn.softmax(predictions[0])

print(
    "원본은 carrot 추측은 {} with a {:.2f} percent confidence.".format(
        class_names[np.argmax(score)], 100 * np.max(score)
    )
)
test_path = "./datasets/pingo/clock_test.png"
img = tf.keras.preprocessing.image.load_img(
    test_path, target_size=(150, 150), color_mode="grayscale"
)

img_array = tf.keras.preprocessing.image.img_to_array(img)
img_array = tf.expand_dims(img_array, 0)

predictions = model.predict(img_array)
score = tf.nn.softmax(predictions[0])

print(
    "원본은 clock 추측은 {} with a {:.2f} percent confidence.".format(
        class_names[np.argmax(score)], 100 * np.max(score)
    )
)
test_path = "./datasets/pingo/crescent_test.png"
img = tf.keras.preprocessing.image.load_img(
    test_path, target_size=(150, 150), color_mode="grayscale"
)

img_array = tf.keras.preprocessing.image.img_to_array(img)
img_array = tf.expand_dims(img_array, 0)

predictions = model.predict(img_array)
score = tf.nn.softmax(predictions[0])

print(
    "원본은 crescent 추측은 {} with a {:.2f} percent confidence.".format(
        class_names[np.argmax(score)], 100 * np.max(score)
    )
)
test_path = "./datasets/pingo/diamond_test.png"
img = tf.keras.preprocessing.image.load_img(
    test_path, target_size=(150, 150), color_mode="grayscale"
)

img_array = tf.keras.preprocessing.image.img_to_array(img)
img_array = tf.expand_dims(img_array, 0)

predictions = model.predict(img_array)
score = tf.nn.softmax(predictions[0])

print(
    "원본은 diamond 추측은 {} with a {:.2f} percent confidence.".format(
        class_names[np.argmax(score)], 100 * np.max(score)
    )
)
test_path = "./datasets/pingo/icecream_test.png"
img = tf.keras.preprocessing.image.load_img(
    test_path, target_size=(150, 150), color_mode="grayscale"
)

img_array = tf.keras.preprocessing.image.img_to_array(img)
img_array = tf.expand_dims(img_array, 0)

predictions = model.predict(img_array)
score = tf.nn.softmax(predictions[0])

print(
    "원본은 icecream 추측은 {} with a {:.2f} percent confidence.".format(
        class_names[np.argmax(score)], 100 * np.max(score)
    )
)
test_path = "./datasets/pingo/strawberry_test.png"
img = tf.keras.preprocessing.image.load_img(
    test_path, target_size=(150, 150), color_mode="grayscale"
)

img_array = tf.keras.preprocessing.image.img_to_array(img)
img_array = tf.expand_dims(img_array, 0)

predictions = model.predict(img_array)
score = tf.nn.softmax(predictions[0])

print(
    "원본은 strawberry 추측은 {} with a {:.2f} percent confidence.".format(
        class_names[np.argmax(score)], 100 * np.max(score)
    )
)
test_path = "./datasets/pingo/t-shirt_test.png"
img = tf.keras.preprocessing.image.load_img(
    test_path, target_size=(150, 150), color_mode="grayscale"
)

img_array = tf.keras.preprocessing.image.img_to_array(img)
img_array = tf.expand_dims(img_array, 0)

predictions = model.predict(img_array)
score = tf.nn.softmax(predictions[0])

print(
    "원본은 t-shirt 추측은 {} with a {:.2f} percent confidence.".format(
        class_names[np.argmax(score)], 100 * np.max(score)
    )
)


acc = history.history["accuracy"]
val_acc = history.history["val_accuracy"]

loss = history.history["loss"]
val_loss = history.history["val_loss"]

plt.figure(figsize=(8, 8))
plt.subplot(2, 1, 1)
plt.plot(acc, label="Training Accuracy")
plt.plot(val_acc, label="Validation Accuracy")
plt.legend(loc="lower right")
plt.ylabel("Accuracy")
plt.ylim([min(plt.ylim()), 1])
plt.title("Training and Validation Accuracy")

plt.subplot(2, 1, 2)
plt.plot(loss, label="Training Loss")
plt.plot(val_loss, label="Validation Loss")
plt.legend(loc="upper right")
plt.ylabel("Cross Entropy")
plt.ylim([0, 1.0])
plt.title("Training and Validation Loss")
plt.xlabel("epoch")


# plt.show()

