#!/usr/local/homebrew/bin/python3
# -*- coding:utf-8 -*-

import os
import re

path = r"G:/test"


def func(path):
    files = []
    for i in os.listdir(path):
        path2 = os.path.join(path, i)  # 拼接绝对路径
        if os.path.isdir(path2):  # 判断如果是文件夹,调用本身
            func(path2)
        else:
            files.append(i)
    return files


# 读取所有文件名
def read_under_files(path):
    return os.listdir(path)  # 得到文件夹下的所有文件名称


# 替换文件中指定文字
def replace_file_name(file_name, replace_str, replace_to):
    new_name = re.sub(replace_str, replace_to, file_name)
    os.rename(path + r"/" + file_name, path + r"/" + new_name)
    return new_name


# 添加前缀
def add_prefix(file_name, prefix):
    new_name = prefix + file_name
    os.rename(path + r"/" + file_name, path + r"/" + new_name)
    return new_name


# 添加后缀
def add_suffix(file_name, suffix):
    f = os.path.splitext(file_name)
    f_name = f[0]
    f_end = f[-1]
    new_name = f_name + suffix + f_end
    os.rename(path + r"/" + file_name, path + r"/" + new_name)
    return new_name


# 前置编号
def add_prefix_number(file_name_list, start_num, with_padding, delimiter=''):
    if file_name_list is None or len(file_name_list) == 0:
        print("find nothing")
    length = len(file_name_list)
    format_str = '{' + f':0{with_padding}d' + '}'
    print(format_str)
    for i in range(start_num, start_num + length):
        add_prefix(file_name_list[i - start_num], format_str.format(i) + delimiter)


# 后置编号
def add_suffix_number(file_name_list, start_num, with_padding, delimiter=''):
    if file_name_list is None or len(file_name_list) == 0:
        print("find nothing")
    length = len(file_name_list)
    format_str = '{' + f':0{with_padding}d' + '}'
    for i in range(start_num, start_num + length):
        add_suffix(file_name_list[i - start_num], format_str.format(i) + delimiter)


# 批量替换名称
def bulk_replace_name(path, old_name, replace_name):
    under_file = read_under_files(path)
    for f_name in under_file:
        print(f_name, " to ", replace_file_name(f_name, old_name, replace_name))


# 批量添加前缀
def bulk_add_prefix(file_path, prefix):
    under_file = read_under_files(file_path)
    for f_name in under_file:
        print(f_name, " to ", add_prefix(f_name, prefix))


# 批量添加后缀
def bulk_add_suffix(file_path, suffix):
    under_file = read_under_files(file_path)
    for f_name in under_file:
        print(f_name, " to ", add_suffix(f_name, suffix))


if __name__ == '__main__':
    bulk_add_prefix(path, '0')
