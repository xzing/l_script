from time import sleep

import requests
from lxml import etree

my_side = 'https://www.jianshu.com/u/4915ed24d1e3?order_by=shared_at&page={:d}'


def xpath_analyze(content_text):
    html_data = etree.HTML(content_text)
    title = html_data.xpath('//li//div//a[@class="title"]')
    for rel_ti in title:
        print('{"', rel_ti.xpath('text()')[0], '":"''https://www.jianshu.com{url}'.format(url=rel_ti.xpath('@href')[0]),
              '"},')


def read_by_page(rpl):
    if rpl.status_code == 200:
        content_text = rpl.content.decode('utf-8')
        # print(content_text)
        xpath_analyze(content_text)


def print_rpl(rpl):
    print(rpl.text)


def look_up_side():
    print("开始爬取:", my_side, '\n')
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,'
                  'application/signed-exchange;v=b3;q=0.9',
        # 这个Cookie已经没用了，自己去改吧
        'cookie': '骚瑞',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/999.36 (KHTML, like Gecko) '
                      'Chrome/81.0.4029.3 Safari/537.36 '
    }

    print("[")
    for i in range(1, 10):
        rpl = requests.get(my_side.format(i), headers=headers)
        sleep(1.5)
        read_by_page(rpl)
    print("]")

    # print_rpl(rpl)


if __name__ == '__main__':
    look_up_side()
