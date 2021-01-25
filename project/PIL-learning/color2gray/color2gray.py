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

def color2grayimage(dir, outdir):
    filesname=[]
    got_files(dir, filesname)

    my_mkdir(outdir)
    for file in filesname:
        print("processing %s" % (file))
        outfile = "%s/%s" % (outdir, got_onlyfilename(file))
        img = Image.open(file).convert('L')
        img.save(outfile)
        


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
    if (len(sys.argv) < 3):
        print("usage: %s <input dir> <output dir>" % (sys.argv[0]))
        quit()
    #for arg in sys.argv:   
    #    print(arg) 
    color2grayimage(sys.argv[1], sys.argv[2])
