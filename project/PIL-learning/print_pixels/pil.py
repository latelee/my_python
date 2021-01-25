# encoding: utf-8
# Author: Late Lee
# 
# pil库 读取并转换图片格式


import os
import sys

from PIL import Image  

import matplotlib.pyplot as plt
#matplotlib inline

def show_image(file):
    img = Image.open(file) # 创建一个PIL图像对象
    print(type(img)) # PIL图像对象
    print("fmt: %s res: %sx%s mode:%s" % (img.format, img.width, img.height, img.mode))
    height = img.height
    width = img.width
    for y in range(0, height):
        for x in range(0, width):
            #pixel = img[y][x]
            pixel = img.getpixel((x, y))
            if (pixel != 0):
                print("0 ", end='')
            else:
                print("1 ", end='')
            #print("%02x" % (pixel), end='')
        print("\n")

def init_python_env():
    if sys.version_info.major == 2:
       reload(sys)
       sys.setdefaultencoding('utf8')

def app_main():
    show_image("0.jpg")

#### main
if __name__ == '__main__':
    init_python_env()
    app_main()
    
