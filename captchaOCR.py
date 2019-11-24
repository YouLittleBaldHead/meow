#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
captchaOCR  调用百度OCR API实现验证码识别

@Author: MiaoTony
"""

from aip import AipOcr
from base64 import b64encode

config = {
    'appId': '17841884',
    'apiKey': 'apPBDxE0U8mfUzF7riZqO1ml',
    'secretKey': 'GwbTq8ksBQxeB6GoVI0LfSMFMwi1LZgG'
}

client = AipOcr(**config)


# def get_file_content(file):
#     with open(file, 'rb') as fp:
#         return fp.read()

def img_to_str(image):  # (image_path):
    # image = get_file_content(image_path)
    result = client.basicGeneral(b64encode(image))
    if 'words_result' in result:
        print(result)
        return '\n'.join([w['words'] for w in result['words_result']])
