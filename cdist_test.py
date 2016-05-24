#!/usr/bin/python
# 圭

from __future__ import print_function
import os
import sys
import shutil
import glob
import tempfile
import argparse
import datetime
import subprocess
import re
import copy
import inspect

class Error(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return self.value
    def __repr__(self):
        return str(self)

class Trees:
    """
    Store for Tree objects which re-uses already-created objects
    and checks for requests for different versions of the same thing.
    """

    def __init__(self):
        self.trees = []

    def get(self, name, specifier, target):
        for t in self.trees:
            if t.name == name and t.specifier == specifier and t.target == target:
                return t
            elif t.name == name and t.specifier != specifier:
                raise Error('conflicting versions of %s requested (%s and %s)' % (name, specifier, t.specifier))

        nt = Tree(name, specifier, target)
        self.trees.append(nt)
        return nt

# 全局类
class Globals:
    quiet = False
    command = None
    trees = Trees()

globals = Globals()


#
# Configuration
#

class Option(object):
    def __init__(self, key, default=None):
        self.key = key
        self.value = default

    def offer(self, key, value):
        # print("self key:%s value:%s\ninput: %s %s" % (self.key, self.value, key, value))
        if key == self.key:
            self.value = value

class BoolOption(object):
    def __init__(self, key):
        self.key = key
        self.value = False

    def offer(self, key, value):
        if key == self.key:
            self.value = (value == 'yes' or value == '1' or value == 'true')

class Config:
    def __init__(self):
        self.options = [ Option('linux_chroot_prefix'),
                         Option('windows_environment_prefix'),
                         Option('mingw_prefix'),
                         Option('git_prefix'),
                         Option('osx_build_host'),
                         Option('osx_environment_prefix'),
                         Option('osx_sdk_prefix'),
                         Option('osx_sdk'),
                         Option('parallel', 4) ]

        try:
            f = open('./cdist.txt', 'r')
            while True:
                l = f.readline()
                if l == '':
                    break

                if len(l) > 0 and l[0] == '#':
                    continue

                s = l.strip().split()
                if len(s) == 2:
                    for k in self.options:
                        k.offer(s[0], s[1])
        except:
            raise

    def get(self, k):
        for o in self.options:
            if o.key == k:
                return o.value

        raise Error('Required setting %s not found' % k)

    def set(self, k, v):
        for o in self.options:
            o.offer(k, v)

config = Config()

def main():
    # 必须输入的命令字段
    commands = {
        "build": "build project",
        "package": "package and build project",
        "release": "release a project using its next version number (changing wscript and tagging)",
        "pot": "build the project's .pot files",
        "changelog": "generate a simple HTML changelog",
        "manual": "build the project's manual",
        "doxygen": "build the project's Doxygen documentation",
        "latest": "print out the latest version",
        "test": "run the project's unit tests",
        "shell": "build the project then start a shell in its chroot",
        "checkout": "check out the project",
        "revision": "print the head git revision number"
    }

    one_of = "Command is one of:\n"
    summary = ""
    for k, v in commands.items():
        one_of += "\t%s\t%s\n" % (k, v)
        summary += k + " "
    print(summary)
    # argparse.ArgumentParser为内置的
    parser = argparse.ArgumentParser()
    parser.add_argument('command', help=summary) # 必备的
    
    #以下是可选的
    parser.add_argument('-p', '--project', help='project name')
    parser.add_argument('--minor', help='minor version number bump', action='store_true') #True Flase
    parser.add_argument('--micro', help='micro version number bump', action='store_true')
    parser.add_argument('--major', help='major version to return with latest', type=int)
    parser.add_argument('-c', '--checkout', help='string to pass to git for checkout')
    parser.add_argument('-o', '--output', help='output directory', default='.')
    parser.add_argument('-q', '--quiet', help='be quiet', action='store_true')
    parser.add_argument('-t', '--target', help='target')
    parser.add_argument('-k', '--keep', help='keep working tree', action='store_true')
    parser.add_argument('--debug', help='build with debugging symbols where possible', action='store_true')
    parser.add_argument('-w', '--work', help='override default work directory')
    parser.add_argument('-g', '--git-prefix', help='override configured git prefix')
    parser.add_argument('-z', '--zz-test', help='WTF...')
    args = parser.parse_args()
    print(args) # 打印解析的结果(含默认值)

main()