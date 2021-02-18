# -*- coding: utf-8 -*-
import os




def gen_sub(param):
    print(os.system(r"autosub  %s" % (param)))



if __name__ == '__main__':
    gen_sub("G:/CloudMusic/Rubia.flac")