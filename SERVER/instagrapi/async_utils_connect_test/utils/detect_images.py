# TODO : image를 download 한 후, Canary_YOLOv5 에서 detect.py 돌리기
# 처리 완료 했으면 이미지 삭제하기
<<<<<<< HEAD
=======
from tqdm import tqdm

# from utils.image_path import *
from image_path import Roots

>>>>>>> 937933f30225b55376fe82b6fef17cddd233ed96
import os

from tqdm import tqdm
# from async_utils_connect_test.utils.image_path import *

class detectArgs:
    input_image_path = ''
    output_image_path = ''
    weight_path = ''
    blur = False
    output_warning_path = ''
    strength = 1
    user_id = 1234
    output_log_path = ''

if __name__ == '__main__':
    if __package__ is None:
        import sys
        from os import path
        print(path.dirname(path.dirname(path.dirname(path.dirname( path.dirname( path.abspath(__file__) ) )) )))
        sys.path.append(path.dirname(path.dirname(path.dirname(path.dirname( path.dirname( path.abspath(__file__) ) )) )))
        from AI.yolov5.detect import *
        from SERVER.instagrapi.async_utils_connect_test.utils.image_path import *
<<<<<<< HEAD
=======
		
    else:
        from ....AI.yolov5 import detect
    
>>>>>>> 937933f30225b55376fe82b6fef17cddd233ed96

def make_directory_save_images(user_output_path):
    path = f'{Roots.IMAGE_OUTPUT_ROOT}/{user_output_path}'
    try:
        if not os.path.exists(path):
            os.makedirs(path)
    except OSError: 
        print("Error : Creating directory " + path)
    return path

def make_directory_save_warning(user_output_path):
    path = f'{Roots.WARNING_OUTPUT_ROOT}/{user_output_path}'
    try:
        if not os.path.exists(path):
            os.makedirs(path)
    except OSError:
        print("Error : Creating directory " + path)
    return path

def detect_images():
    print('Start Detecting Imgs')
    test_needed_user_list = os.listdir(f'{Roots.IMAGE_DOWNLOAD_ROOT}')
    test_needed_user_number = len(test_needed_user_list)

    for i in tqdm(range(0, test_needed_user_number)):
        print("== User Number : %d ==" % i)
        make_directory_save_images(test_needed_user_list[i])
        make_directory_save_warning(test_needed_user_list[i])

        test_needed_photo_list = os.listdir(f'{Roots.IMAGE_DOWNLOAD_ROOT}/{test_needed_user_list[i]}')
        test_needed_photo_number = len(test_needed_photo_list)

        for j in tqdm(range(0, test_needed_photo_number)):
            print("== Photo Number : %d ==" % j)
            user_photo_path = f'{test_needed_user_list[i]}/{test_needed_photo_list[j]}'
<<<<<<< HEAD
            IMAGE_INPUT_PATH = f'{IMAGE_DOWNLOAD_ROOT}/{user_photo_path}'
            IMAGE_OUTPUT_PATH = f'{IMAGE_OUTPUT_ROOT}/{user_photo_path}'
            WARNING_OUTPUT_PATH = f'{WARNING_OUTPUT_ROOT}/{user_photo_path}'+('.txt')
            LOG_OUTPUT_PATH = f'{LOG_OUTPUT_ROOT}/{user_photo_path}'+('.txt')
=======

            IMAGE_INPUT_PATH = f'{Roots.IMAGE_DOWNLOAD_ROOT}/{user_photo_path}'
            IMAGE_OUTPUT_PATH = f'{Roots.IMAGE_OUTPUT_ROOT}/{user_photo_path}'
            WARNING_OUTPUT_PATH = f'{Roots.WARNING_OUTPUT_ROOT}/{user_photo_path}'+('.txt')
>>>>>>> 937933f30225b55376fe82b6fef17cddd233ed96

            args = detectArgs()
            args.input_image_path = f'{IMAGE_INPUT_PATH}'
            args.output_image_path = f'{IMAGE_OUTPUT_PATH}'
            args.weight_path = './weight/yolov5m6.pt'
            args.output_warning_path = f'{WARNING_OUTPUT_PATH}'
            args.output_log_path = f'{LOG_OUTPUT_PATH}'

            # detect(args)

detect_images()