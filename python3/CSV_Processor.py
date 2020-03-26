#!/usr/local/homebrew/bin/python3
# -*- coding:utf-8 -*-
from python3.file_util import append_to_new_line

if __name__ == '__main__':
    mm_data = {}
    all_str = '';
    with open("/Users/zing/Desktop/csv_data/3.csv") as fp:
        line = fp.readline()
        cnt = 1
        while line:
            a = line.strip();
            # print("Line {}: {}".format(cnt, line.strip()))
            c_user = a.split(',')
            mm_data[c_user[0]] = c_user[1]
            line = fp.readline()
            cnt += 1
    with open("/Users/zing/Desktop/csv_data/results.csv") as rp:
        line = rp.readline()
        cnt = 1
        while line:
            a = line.strip()
            c_user = a.split(',')
            print(c_user)
            d = mm_data[c_user[1]]
            new_line = f'{c_user[0]}, {c_user[1]},{d},{c_user[2]},{c_user[3]}\n'
            all_str = all_str + new_line
            line = rp.readline()
            cnt += 1
    append_to_new_line("./script/all_data.csv", all_str)
    print(mm_data)
