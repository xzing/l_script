#!/usr/local/homebrew/bin/python3
# -*- coding:utf-8 -*-

import json


# 加载JSON
from python3.file_util import append_to_new_line


def load_json_file(file_name):
    with open(file_name) as json_file:
        return json.load(json_file)
#
#
# if __name__ == '__main__':
#     jsonObj = load_json_file("./split_template.json")
#     for k in jsonObj:
#         kStr = "PUT _template/" + k
#         kStr = kStr + "\n" + str(jsonObj.get(k)).replace('\'', '\"')
#         kStr = kStr + "\n"
#         append_to_new_line("./script/all_in_one.kibana", kStr)
#
#         print(kStr)
