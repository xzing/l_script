#!/usr/local/homebrew/bin/python3
# -*- coding:utf-8 -*-

import os


path = "G:\TOAli"

def func(path):
    files = []
    for i in os.listdir(path):
        path2 = os.path.join(path, i)  # 拼接绝对路径
        if os.path.isdir(path2):  # 判断如果是文件夹,调用本身
            func(path2)
        else:
            files.append(i)
    return files

def readUnderFiles(path):
    return os.listdir(path) #得到文件夹下的所有文件名称

def replaceFile(file:str, replaceStr:str, replaceTo:str):
    open(file).name
    orgName = file.name

    return


def printAllItem(naleList):
    for fName in naleList:
        print(fName);





if __name__ == '__main__':
    naleList = readUnderFiles(path)
    printAllItem(naleList)