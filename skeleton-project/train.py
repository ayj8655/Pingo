
from data import preprocess
from utils import utils
import config

# config 저장
img_path, captions_path, train_split, do_traning = utils.save_config(
    config.args)

train_dataset_path = './datasets/train_val.csv'
val_dataset_path = './datasets/test_val.csv'

# 이미지 경로 및 캡션 불러오기
img_paths, captions = preprocess.get_path_caption(
    img_path, captions_path)

print(len(img_paths), len(captions))

# 전체 데이터셋을 분리해 저장하기
train_dataset_path, val_dataset_path = preprocess.dataset_split_save(
    img_paths, captions, train_split)


# 저장된 데이터셋 불러오기 -> do_traning이 참이면 트레이닝데이터 불러오기 거짓이면 테스트데이터
img_paths, caption = preprocess.get_data_file(
    do_traning, train_dataset_path, val_dataset_path)


# 데이터 샘플링
if config.do_sampling:
    img_paths, caption = preprocess.sampling_data(train_split)


image_input = './datasets/images/10002456.jpg'
caption_input = 'Two young guys with shaggy hair look at their hands while hanging out in the yard'

# 이미지와 캡션 시각화 하기
utils.visualize_img_caption(image_input, caption_input)
