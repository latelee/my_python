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
    ## 图像读取、显示
    # 读取
    img = Image.open(file) # 创建一个PIL图像对象
    print(type(img)) # PIL图像对象
    print(img.format, img.size, img.mode)
    #plt.imshow(img)
    img.save("foo.bmp")

def init_python_env():
    if sys.version_info.major == 2:
       reload(sys)
       sys.setdefaultencoding('utf8')

#### main
if __name__ == '__main__':
    init_python_env()
    show_image("foo.jpg_1.jpg")
