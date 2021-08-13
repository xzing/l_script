# -*- coding: utf-8 -*-

import requests
import json
# from lxml import etree
from bs4 import BeautifulSoup


def get_web_page(bv):
    url = r"https://api.bilibili.com/x/player/pagelist?bvid=%s&jsonp=jsonp" % bv
    response = requests.get(url)
    response.encoding = 'utf-8'  # 解码
    # print(response.content)
    jo = json.loads(response.text)
    data = jo['data']
    for item in data:
        print(item['page'], item['part'])
    # root = BeautifulSoup(response.content, 'html.parser', from_encoding='utf-8')
    # # video_list = root.xpath("//ul[@class='list-box']//li//a//text()")
    # data = root.body.find('ul', attrs={"class": 'list-box'}).find('li').find()
    print(response)


if __name__ == '__main__':
    get_web_page("BV1qv411K7eE")
