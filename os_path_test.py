#!/usr/bin/python3
# encoding: utf-8

# os.pathµÄ²âÊÔÊ¾Àý

''' os path test sample '''

import os.path

file="test.txt"
def path_test(file):
    print("abspath: %s" % os.path.abspath(file))
    print("basename: %s" % os.path.basename(file))
    print("commonprefix: %s" % os.path.commonprefix(file))
    print("dirname: %s" % os.path.dirname(file))
    print("exists: %s" % os.path.exists(file))
    print("expanduser: %s" % os.path.expanduser("~"))
    print("getatime: %s" % os.path.getatime(file))
    print("getmtime: %s" % os.path.getmtime(file))
    print("getctime: %s" % os.path.getctime(file))
    print("getsize: %s" % os.path.getsize(file))
    print("isabs: %s" % os.path.isabs(file))
    print("isfile: %s" % os.path.isfile(file))
    print("isdir: %s" % os.path.isdir(file))
    print("islink: %s" % os.path.islink(file))
    print("ismount: %s" % os.path.ismount(file))
    print("normpath: %s" % os.path.normpath("~"))
    print("realpath: %s" % os.path.realpath(file))
    print("relpath: %s" % os.path.relpath(file))
    print(os.path.split(file))


#### main
if __name__ == '__main__':
    path_test(file)
