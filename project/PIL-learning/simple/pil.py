# encoding: utf-8
# Author: Late Lee
# 2017.8.29
# linux+python3
#
# haar训练正样本提取
# 根据pos_image目录下的文件（注：未对后缀名做判断），生成pos_image.txt文件，
# 该文件内容：文件名 1 0 0 宽 高


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
    img.convert('L')
    img.show()

def init_python_env():
    if sys.version_info.major == 2:
       reload(sys)
       sys.setdefaultencoding('utf8')

#### main
if __name__ == '__main__':
    init_python_env()
    #generate_haar_posimage("pos_image", "pos_image.txt")
    show_image("IMG_20170810_001.jpg_1.jpg")
