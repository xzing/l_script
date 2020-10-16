# -*- coding: utf-8 -*-
import os
import threading

saveTo = "C:\Users\Zing\Downloads\GoInit"

# https://www.bilibili.com/video/BV1S7411m7vM?p=2
def download():
    for i in range(1,9):
        urlStr = "https://www.bilibili.com/video/BV1xE411T7Dy?p=%d" % i;
        print(urlStr)
        myThread(i, "Thread-%d" % i, urlStr).start()
    pass


exitFlag = 0


class myThread(threading.Thread):  # 继承父类threading.Thread
    def __init__(self, threadID, name, urlStr):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.urlStr = urlStr

    def run(self):  # 把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        print
        "Starting " + self.name
        print(os.system(r"you-get -o %s %s" % self.urlStr))
        print
        "Exiting " + self.name


if __name__ == '__main__':
    download();
