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
    
def write_img_res(image, f):
    
    img = Image.open(image)  
    text = "%s 1 0 0 %d %d\n" % (image, img.width, img.height)
    f.write(text) # write text to file
    img.close();

def generate_haar_posimage(dir, outfile):
    filesname=[]
    got_files(dir, filesname)   
    f = open(outfile, "w")
    for file in filesname:
        print("processing %s" % (file))
        write_img_res(file, f)

    f.close()
    print("saving to %s success!" %(outfile));
    
def got_onlyfilename(path):
    #return path.split("/")[-1]
    return os.path.basename(path)

# 不要后缀名、不要目录
def got_onlyfilename_noext(path):
    f = os.path.basename(path)
    return f.split(".")[0]

def my_mkdir(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)

def generate_haar_negimage(dir, outdir):
    filesname=[]
    got_files(dir, filesname)

    my_mkdir(outdir)
    width = 150
    height = 120
    x = 0
    y = 0
    x1 = x+width
    y1 = y+height
    i = 0
    for file in filesname:
        print("processing %s" % (file))
        #write_img_res(file, f)
        img = Image.open(file)
        src_w = img.width
        src_h = img.height
        for h in range(0, src_h, height):
            #print("h: %d" % (h))
            for w in range(0, src_w, width):
                #print("w: %d h: %d" % (w, h))
                x = w
                y = h
                x1 = x+width
                y1 = y+height
                if (x1 < src_w and y1 < src_h):
                    region = (x, y, x1, y1)
                    cropImg = img.crop(region)
                    f = got_onlyfilename_noext(file)
                    outfile = "%s/%s_%d.jpg" % (outdir, f, i)
                    i += 1
                    #outfile = outdir + "/" + f + "_.jpg"
                    #print("(%d, %d) (%d, %d)" % (x, y, x1, y1))
                    print("saving to file: %s" % (outfile))
                    cropImg.save(outfile)
                    
        x = 0
        y = 0
        x1 = x+width
        y1 = y+height

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
    #generate_haar_posimage("pos_image", "pos_image.txt")
    generate_haar_negimage("src", "out")
