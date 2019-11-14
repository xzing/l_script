#!/usr/local/homebrew/bin/python3
# -*- coding:utf-8 -*-

import json

import yaml


# 去除字符串首尾空白
def trim_str(s):
    if isinstance(s, str):
        return s.strip()
    elif s is None:
        return ''
    else:
        raise TypeError


def trim_to_one_line(s):
    if isinstance(s, str):
        return trim_str(s).replace('\n', ' ').replace('\r', ' ').replace('\t', ' ')
    elif s is None:
        return ''
    elif not isinstance(s, str):
        return f"{str(s)}"
    else:
        raise TypeError(f"{str(s)}")


# 判断字符不为空
def is_not_empty_str(s):
    if s is None:
        return False
    elif isinstance(s, str):
        return s.strip() != ""
    else:
        return False


# 判断字符不为空
def is_empty_str(s):
    if s is None:
        return True
    elif isinstance(s, str):
        return s.strip() == ""
    else:
        return True


# 加载JSON
def load_json_file(file_name):
    with open(file_name) as json_file:
        return json.load(json_file)


# 加载YAML
def load_yaml_config(file_path):
    with open(file_path, 'r') as yaml_file:
        return yaml.load(yaml_file, Loader=yaml.FullLoader)


def number_remove_useless_info(num_data):
    if num_data is None:
        return ""
    elif isinstance(num_data, str):
        return num_data
    elif isinstance(num_data, int):
        return num_data
    elif isinstance(num_data, float):
        return '{:g}'.format(num_data)
