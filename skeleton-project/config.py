import argparse as parser

# Req. 2-1	Config.py 파일 생성

# 데이터샘플링 할까 말까
do_sampling = True
#do_sampling = False


parser = parser.ArgumentParser()
# 캡션 데이터가 있는 파일 경로 (예시)
parser.add_argument('--caption_file_path', type=str,
                    default='./datasets/captions.csv')
parser.add_argument('--images_folder_path', type=str,
                    default='./datasets/images/')
parser.add_argument('-train_split', type=float,
                    default=80.0)
parser.add_argument('-do_traning', type=bool,
                    default=True)
parser.add_argument('-sampling_split', type=float,
                    default=0.02)

# --는 풀네임 -는 축약어
# -가 없이 ab 일 경우 콘솔에 무조건 써야함


args = parser.parse_args()

# print(args)
