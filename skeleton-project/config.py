import argparse as parser

# Req. 2-1	Config.py 파일 생성

# 데이터샘플링 할까 말까
do_sampling = False


parser = parser.ArgumentParser()
# 캡션 데이터가 있는 파일 경로 (예시)
parser.add_argument('--caption_file_path', type=str,
                    default='.\\datasets\\captions.csv')
parser.add_argument('--images_folder_path', type=str,
                    default='.\\datasets\\images\\')
parser.add_argument('-train_split', type=float,
                    default='80')
parser.add_argument('-do_traning', type=bool,
                    default=True)
args = parser.parse_args()

# print(args)
