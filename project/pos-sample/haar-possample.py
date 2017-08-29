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
    
def process_single(image, f):
    
    img = Image.open(image)  
    text = "%s 1 0 0 %d %d\n" % (image, img.width, img.height)
    f.write(text) # write text to file
    img.close();

def generate_haar_posimage(dir, outfile):
    filesname=[]
    got_files("pos_image", filesname)
    
    f = open(outfile, "w")
    
    for file in filesname:
        print("processing %s" % (file))
        process_single(file, f)

    print("saving to %s success!" %(outfile));
    f.close()

def got_files(dir, outlist):
    list = os.listdir(dir)
    for file in list:
        filename = "%s/%s" % (dir, file) #os.path.join(dir, file)
        outlist.append(filename)

def init_python_env():
    if sys.version_info.major == 2:
       reload(sys)
       sys.setdefaultencoding('utf8')

#### main
if __name__ == '__main__':
    init_python_env()
    # add here
    generate_haar_posimage("pos_image", "pos_image.txt")
