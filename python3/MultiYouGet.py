# -*- coding: utf-8 -*-
import json
import os
import sys
import threading
from multiprocessing import Pool

import requests

from you_get import common as you_get


# https://www.bilibili.com/video/BV1S7411m7vM?p=2
def download():
    #  串行 174
    for i in range(1, 28):
        # for i in [17]:
        url_str = "https://www.bilibili.com/video/BV19y4y1b7Uo?p=%d" % i
        # urlStr = "https://www.bilibili.com/video/BV1RT4y137an"
        print(url_str)
        DownloadThread(i, "Thread-%d" % i, url_str).start()
    pass


def download(list):
    url_str = "https://www.bilibili.com/video/%s?p=%d"
    for m in list:
        index = m['page']
        part_url = url_str % (bv_name, index)
        print(part_url)
        DownloadThread(index, "Thread-%d" % index, part_url, m['name']).start()


def get_bv_playlist(bv):
    url = r"https://api.bilibili.com/x/player/pagelist?bvid=%s&jsonp=jsonp" % bv
    response = requests.get(url)
    response.encoding = 'utf-8'  # 解码
    jo = json.loads(response.text)
    return jo['data']


def download_and_save_name(bv):
    playlist = get_bv_playlist(bv)


def multi_process(k_and_v):
    url = k_and_v['url']
    file_name = k_and_v['file_name']
    print('url', url, 'file_name', file_name)
    sys.argv = ['you-get', '-o', save_to, '--no-caption', url, '-O', file_name]
    you_get.main()


def multi_download(data_list):
    url_str = 'https://www.bilibili.com/video/%s?p=%d'
    process_url = []
    for i in data_list:
        k_and_v = {'url': url_str % (bv_name, i['page']), 'file_name': i['name']}
        process_url.append(k_and_v)
    print("Starting ...")
    pool = Pool(8)
    pool.map(multi_process, process_url)
    pool.close()
    pool.join()
    print("waiting ...")


exitFlag = 0
save_to = "~/Downloads/a_kafka"
bv_name = 'BV11q4y1D7go'


# save_to = "F:\\FuckThunder\\ASC"


class DownloadThread(threading.Thread):  # 继承父类threading.Thread
    def __init__(self, thread_id, name, url_str, file_name):
        threading.Thread.__init__(self)
        self.threadID = thread_id
        self.name = name
        self.url_str = url_str
        self.file_name = file_name

    def run(self):  # 把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        print("Starting " + self.name)
        if self.file_name:
            print(os.system(r"you-get -o %s --no-caption %s -O %s" % (save_to, self.url_str, self.file_name)))
        else:
            print(os.system(r"you-get -o %s --no-caption %s" % (save_to, self.url_str)))
        print("Exiting " + self.name)


def mkdir(path):
    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")
    # 判断路径是否存在
    is_exists = os.path.exists(path)
    # 判断结果
    if not is_exists:
        # 如果不存在则创建目录,创建目录操作函数
        '''
        os.mkdir(path)与os.makedirs(path)的区别是,当父目录不存在的时候os.mkdir(path)不会创建，os.makedirs(path)则会创建父目录
        '''
        # 此处路径最好使用utf-8解码，否则在磁盘中可能会出现乱码的情况
        os.makedirs(path)
        print(path + ' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path + ' 目录已存在')
        return False


if __name__ == '__main__':
    str_name = get_bv_playlist(bv_name)
    print(str_name)
    list = []
    for obj in str_name:
        file_name = 'p-{:<4d}'.format(obj['page'])+'-'+obj['part']
        list.append({'page': obj['page'], 'name': obj['part']})
    print(list)
    mkdir(save_to)
    # download(list)
    multi_download(list)
    os.startfile(save_to)
