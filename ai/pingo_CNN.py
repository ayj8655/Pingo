import matplotlib.pylab as plt
import tensorflow as tf
import os
import numpy as np
import glob


# 시간측정
import time
import datetime

# 시간측정끝

# gpu 확인을 위해 추가
# from tensorflow.python.client import device_lib
# print(device_lib.list_local_devices())
# gpu 확인을 위해 추가 끝

# gpu 사용하려고 입력
os.environ["CUDA_VISIBLE_DEVICES"] = "0"
# 텐서플로우 버전 확인
print(tf.__version__)

start = time.time()  # 시작 시간 저장


# 이미지 저장 위치
data_dir = "./datasets/pingo"
# 이미지 사이즈
IMG_SIZE = (300, 300)
# 배치 사이즈
BATCH_SIZE = 256
# 에포크 횟수
initial_epochs = 5


# image_dataset_from_directory를 이용해서 해당 폴더에서 이미지 가져오기
train_dataset = tf.keras.preprocessing.image_dataset_from_directory(
    data_dir,
    validation_split=0.2,
    subset="training",
    seed=456,
    image_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    color_mode="rgb",
    # color_mode="grayscale",
    # label_mode="categorical",
)

validation_dataset = tf.keras.preprocessing.image_dataset_from_directory(
    data_dir,
    validation_split=0.2,
    subset="validation",
    seed=456,
    image_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    color_mode="rgb",
    # color_mode="grayscale",
    # label_mode="categorical",
)

# 클래스 이름 가져오기
class_names = train_dataset.class_names

# 이미지 shape 알아보기위해
for image_batch, labels_batch in train_dataset:
    print(image_batch.shape)
    print(labels_batch.shape)
    break

# 캐싱, 셔플, 프리페치
AUTOTUNE = tf.data.experimental.AUTOTUNE
train_dataset = train_dataset.cache().shuffle(1000).prefetch(buffer_size=AUTOTUNE)
validation_dataset = validation_dataset.cache().prefetch(buffer_size=AUTOTUNE)


# 데이터셋에서 이미지 미리보기
plt.figure(figsize=(10, 10))
for images, labels in train_dataset.take(1):
    for i in range(9):
        ax = plt.subplot(3, 3, i + 1)
        plt.imshow(images[i].numpy().astype("uint8"))
        plt.title(class_names[labels[i]])
        plt.axis("off")
plt.show()

# 전처리 -> 픽셀값 조정
rescale = tf.keras.Sequential(
    [tf.keras.layers.experimental.preprocessing.Rescaling(1.0 / 255)]
)
# 전처리 -> 데이터 증강
data_augmentation = tf.keras.Sequential(
    [
        tf.keras.layers.experimental.preprocessing.RandomFlip("horizontal"),
        tf.keras.layers.experimental.preprocessing.RandomRotation(0.2),
    ]
)

# 데이터 증강된 이미지 미리보기
for image, _ in train_dataset.take(1):
    plt.figure(figsize=(10, 10))
    first_image = image[0]
    for i in range(9):
        ax = plt.subplot(3, 3, i + 1)
        augmented_image = data_augmentation(tf.expand_dims(first_image, 0))
        plt.imshow(augmented_image[0] / 255)
        plt.axis("off")
plt.show()


# 모델 정의
model = tf.keras.models.Sequential(
    [
        rescale,
        data_augmentation,
        tf.keras.layers.Conv2D(
            16, (3, 3), activation="relu", input_shape=(300, 300, 3)
        ),
        tf.keras.layers.MaxPooling2D(2, 2),
        tf.keras.layers.Conv2D(32, (3, 3), activation="relu"),
        tf.keras.layers.MaxPooling2D(2, 2),
        tf.keras.layers.Conv2D(64, (3, 3), activation="relu"),
        tf.keras.layers.MaxPooling2D(2, 2),
        tf.keras.layers.Conv2D(128, (3, 3), activation="relu"),
        tf.keras.layers.MaxPooling2D(2, 2),
        tf.keras.layers.Dropout(0.5),
        tf.keras.layers.Conv2D(256, (3, 3), activation="relu"),
        tf.keras.layers.MaxPooling2D(2, 2),
        tf.keras.layers.Dropout(0.5),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(1024, activation="relu"),
        tf.keras.layers.Dropout(0.5),
        tf.keras.layers.Dense(10, activation="softmax"),
    ]
)


# 모델 컴파일
model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
    # optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"]
)
print("-----------아래는 카테고리별 이름--------------------")
print(class_names)
print("---------------아래는 데이터셋 쉐이프 확인------------------")
print(train_dataset)
print("-----------------------------------------")


# 학습 시작
history = model.fit(
    train_dataset, validation_data=validation_dataset, epochs=initial_epochs
)

# 모델 정확도 측정
score = model.evaluate(validation_dataset)

# 모델 요약 출력
model.summary()


print("loss=", score[0])  # loss
print("accuracy=", score[1])  # acc

# 파일에 저장용 변수들
save_accuracy = str(round(score[1], 3))
save_loss = str(round(score[0], 3))
save_BATCH_SIZE = str(BATCH_SIZE)
save_initial_epochs = str(initial_epochs)
# 파일에 저장용 변수들 끝

model.save(
    "./models/pingo_"
    + save_BATCH_SIZE
    + "_"
    + save_initial_epochs
    + "_"
    + save_accuracy
    + "_"
    + save_loss
    + ".h5"
)
# model.save("./models/pingo.h5")


predictions = model.predict(validation_dataset)

print(
    "This image most likely belongs to {} with a {:.2f} percent confidence.".format(
        class_names[np.argmax(predictions[0])], 100 * np.max(predictions[0])
    )
)

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


# 시간측정
end = time.time()
sec = end - start
# 시간측정 끝

# 시간 출력 2가지 방법
result = datetime.timedelta(seconds=sec)
print(result)
# result_list = str(datetime.timedelta(seconds=sec)).split(".")
# print(result_list[0])

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


plt.show()
plt.savefig(
    "./models/pingo_"
    + save_BATCH_SIZE
    + "_"
    + save_initial_epochs
    + "_"
    + save_accuracy
    + "_"
    + save_loss
    + ".png"
)

