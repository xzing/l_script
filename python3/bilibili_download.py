#!/usr/local/homebrew/bin/python3
# -*- coding:utf-8 -*-

# 需要pip3 安装 you-get
import os
import threading

TARGET_DIR = "/Users/zing/Downloads/Docker/"

SOURCE_URL = r"https://www.bilibili.com/video/av27122140?p={}"


def download_page(page):
    print(page)
    os.system(r"you-get " + SOURCE_URL.format(page) + " -o " + TARGET_DIR)


def download_all_page():
    threads = []

    for i in range(12):
        th = threading.Thread(target=download_page, args=(i + 1,))
        th.start()
        threads.append(th)

    for th in threads:
        th.join()


if __name__ == '__main__':
    download_all_page()
