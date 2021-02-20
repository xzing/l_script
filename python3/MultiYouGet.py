# -*- coding: utf-8 -*-
import os
import sys
import threading
from multiprocessing import Pool
from you_get import common as you_get


# https://www.bilibili.com/video/BV1S7411m7vM?p=2
def download():
    #  串行
    for i in range(40,60):
        urlStr = "https://www.bilibili.com/video/BV1c4411J7Ty?p=%d" % i
        print(urlStr)
        myThread(i, "Thread-%d" % i, urlStr).start()
    pass

def multi_process(urls):
    sys.argv = ['you-get', '-o', save_to, '--no-caption', urls]
    you_get.main()



def multi_download(start, end):
    urlStr = 'https://www.bilibili.com/video/BV1c4411J7Ty?p='
    process_url=[]
    for i in range(start, end):
        process_url.append(urlStr + str(i))
    print(urlStr)
    print("Starting ...")
    pool = Pool(8)
    pool.map(multi_process, process_url)
    pool.close()
    pool.join()
    print("waiting ..." )


exitFlag = 0
save_to = "G:\\Netty"


class myThread(threading.Thread):  # 继承父类threading.Thread
    def __init__(self, threadID, name, urlStr):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.urlStr = urlStr

    def run(self):  # 把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        print("Starting " + self.name)
        print(os.system(r"you-get -o %s %s" % (save_to, self.urlStr)))
        print("Exiting " + self.name)


if __name__ == '__main__':
    # download()
    multi_download(60, 90)
