# -*- coding:utf-8 -*-

# 抠门，图片不给外链了，为了博客上不在裂图，回收自己的图片，就有了这个脚本
import json
from time import sleep

import requests
from lxml import etree

all_article = '''
[{"IntelliJ IDEA管理Docker容器的小技巧": "https://www.jianshu.com/p/714b51d54f5d"},
               {"2019我的年终总结": "https://www.jianshu.com/p/525eb14d8e5c"},
               {"Postgres慢SQL查询与效率分析": "https://www.jianshu.com/p/a811436e6a10"},
               {"IDEA Services 工具窗口: 一个管理所有服务的地方【译】": "https://www.jianshu.com/p/2e2332f247fe"},
               {"分布式数据库与C.A.P.": "https://www.jianshu.com/p/18da8c7f09d1"},
               {"使用Ubuntu快速搭建Java Web开发环境——河蟹版": "https://www.jianshu.com/p/abcec8c82a95"},
               {"从0开始学线程并发（二）——线程通信": "https://www.jianshu.com/p/cd06cef38599"},
               {"Go的数组和指针": "https://www.jianshu.com/p/107ea36c0198"},
               {"Go变量类型与定义": "https://www.jianshu.com/p/de5f7325eb29"},
               {"(译)SOA VS microservices: 有啥不一样?": "https://www.jianshu.com/p/97d71a3ce65f"},
               {"从0开始学线程并发（一）": "https://www.jianshu.com/p/70c767877c57"},
               {"Java8  Stream 系列（三）深入源码之Collector": "https://www.jianshu.com/p/1128dc085e74"},
               {"眼见他起高楼，眼见他楼塌了": "https://www.jianshu.com/p/e0b56636832b"},
               {"IDEA又双叒叕崩溃了，怎么去找崩溃原因": "https://www.jianshu.com/p/13e0b9bbfca2"},
               {"macOS Mojave如何为蓝牙耳机开启AAC、aptX": "https://www.jianshu.com/p/032be9a63bcd"},
               {"利用Scala的隐式转换，扩展对象方法": "https://www.jianshu.com/p/f54e174c79e7"},
               {"Scala的隐式转换": "https://www.jianshu.com/p/edfc9c16d86a"},
               {"拜占庭共识算法": "https://www.jianshu.com/p/38b25920b247"},
               {"25种以太坊代币标准详细列表": "https://www.jianshu.com/p/998ebfa05098"},
               {"Elasticsearch计算Array中元素的个数": "https://www.jianshu.com/p/3bc797dcfa62"},
               {"30种共识算法完全列表": "https://www.jianshu.com/p/b62e68566192"},
               {"Java 11 正式发布，8 个逆天新特性": "https://www.jianshu.com/p/02fff4761f27"},
               {"替换macOS High Sierra APP图标": "https://www.jianshu.com/p/f9dbe851894c"},
               {"macOS High Sierra 显示隐藏文件": "https://www.jianshu.com/p/6a0ceb52a8a9"},
               {"Spring Boot 2.x 启动全过程源码分析": "https://www.jianshu.com/p/414d3e2f04e9"},
               {"SpringBoot整合Elasticsearch的Java Rest Client": "https://www.jianshu.com/p/0b4f5e41405e"},
               {"Elasticsearch Java Rest Client 上手指南（下）": "https://www.jianshu.com/p/d2c8326e8fa3"},
               {"Elasticsearch Java Rest Client 上手指南（上）": "https://www.jianshu.com/p/c1f2161a5d22"},
               {"以太坊白皮书（区块链入门必读）": "https://www.jianshu.com/p/2a33441874af"},
               {"SpringMVC学习笔记": "https://www.jianshu.com/p/69dedd1904af"},
               {"CGLib 使用手册【转】": "https://www.jianshu.com/p/76a12f333e7a"},
               {"Java8  Stream 系列（二）Stream应当注意的点": "https://www.jianshu.com/p/1e0dee43f09c"},
               {"领域驱动设计（一）": "https://www.jianshu.com/p/f5e28439b25e"},
               {"Java8  Stream系列（一）从入坑到沉迷": "https://www.jianshu.com/p/78330c679b60"},
               {"线程学习笔记（一）": "https://www.jianshu.com/p/3b2a5da2d9fd"},
               {"Java线程内存模型": "https://www.jianshu.com/p/4e0bfcb1711e"},
               {"03-类和接口 —— 《Effective Java II》 读书笔记": "https://www.jianshu.com/p/bb3349b46fd4"},
               {"02-对象通用方法——《Effective Java II》 读书笔记": "https://www.jianshu.com/p/c38384416080"},
               {"01-创建和销毁对象——《Effective Java II》 读书笔记": "https://www.jianshu.com/p/51834deb766d"},
               {
                   "Could not connect to remote process. Aborting debug session.解决办法": "https://www.jianshu.com/p/ada2fc7088d7"},
               {"Ansible自动化部署从入门到弃坑": "https://www.jianshu.com/p/23f2dc487ee1"},
               {"Ansible自动化部署入门": "https://www.jianshu.com/p/dd9e8ba5ec65"},
               {"自动化部署工具 Ansible填坑记录": "https://www.jianshu.com/p/0dbcda624252"},
               {"初探Gradle": "https://www.jianshu.com/p/c89015c7d6c2"},
               {"使用Ubuntu快速搭建Java Web开发环境": "https://www.jianshu.com/p/9ea92a188bdc"},
               {"Java8避免空指针的新工具——Optional源码分析": "https://www.jianshu.com/p/17108360856b"},
               {"Java的GC如何玩弄对象——GC的几种算法": "https://www.jianshu.com/p/795617ef8194"},
               {"夯基础：涮一遍Java JDBC": "https://www.jianshu.com/p/8b249f375167"},
               {"（FS计划）理清楚Spring的AOP到底怎么玩": "https://www.jianshu.com/p/3c2cbafed4ea"},
               {"(FS计划)AOP和Spring中AOP的简单介绍": "https://www.jianshu.com/p/d03c6c8daab9"},
               {"Spring中Bean的作用域": "https://www.jianshu.com/p/9e14411c2eff"},
               {"关于编程，我要矫情两句": "https://www.jianshu.com/p/316db34f7bd1"},
               {"MyBatis使用笔记": "https://www.jianshu.com/p/e8165eecfc4b"},
               {"（笔记）CentOS 7 安装与卸载MySQL 5.7跳坑": "https://www.jianshu.com/p/e54ff5283f18"},
               {"Win10安装CentOS7填坑记": "https://www.jianshu.com/p/7190643259a9"},
               {"函数式接口和Lambda表达式深入理解": "https://www.jianshu.com/p/40f833bf2c48"},
               {"函数式接口和Java8的lambda表达式": "https://www.jianshu.com/p/916eb657eb28"},
               {"(FS计划)Java里的动态代理模式和代理方法增强": "https://www.jianshu.com/p/893ffc0b7a73"},
               {"快速了解Java反射以及使用场景": "https://www.jianshu.com/p/8e42fc36d6d8"},
               {"Re：从零开始挑选相机": "https://www.jianshu.com/p/bd4391e647fe"},
               {"macOS 软件提示‘软件已损坏’，或‘不是Mac Appstore下载的’解决办法": "https://www.jianshu.com/p/3d47a1675f69"},
               {"App Store无法更新iTunes解决办法": "https://www.jianshu.com/p/f156256c37dd"},
               {"（个人备用）Linux 服务器搭建 Shadowsocks服务端": "https://www.jianshu.com/p/dec58fb03ee7"},
               {"极路由1、1s等机型刷OpenWrt--成为真正的极客": "https://www.jianshu.com/p/196a43b79c24"},
               {"如何用Nginx代理静态博客": "https://www.jianshu.com/p/682e62c2a3dc"},
               {"OS X如何搭建Hexo+github 静态博客": "https://www.jianshu.com/p/3109057b2b8b"},
               {"Ubuntu下搭建Hexo + github 博客": "https://www.jianshu.com/p/dd111ea16f4d"},
               {"Spring之方法注入": "https://www.jianshu.com/p/e27df48a6c7c"},
               {"OS X上的免费的gif动态截屏软件，截表情专用": "https://www.jianshu.com/p/2825ae7c3d09"},
               {"CentOS下搭建Hexo + github 博客": "https://www.jianshu.com/p/0823e387c019"},
               {"简单说说jvm的对象存储与访问": "https://www.jianshu.com/p/740f00cf03b2"},
               {"Mac上简单的Android逆向": "https://www.jianshu.com/p/7696c7e33eac"},
               {"(FS计划)Spring的IoC容器对bean的实例化": "https://www.jianshu.com/p/a3d2e41c1cd2"},
               {"(FS计划)IoC 控制反转": "https://www.jianshu.com/p/9e09411d446c"},
               {"(FS计划)SpringMVC的使用配置": "https://www.jianshu.com/p/3965bf5d3c1e"},
               {"IntelliJ IDEA创建SpringMVC+Maven项目": "https://www.jianshu.com/p/2101d176555b"},
               {"OS X 中Launchpad 图标行列数量更改": "https://www.jianshu.com/p/3671b495e28a"},
               {"OS X EI Capitan 安装mysql-5.7.9": "https://www.jianshu.com/p/776e72742c6e"}]
'''


def xpath_analyze(content_text):
    html_data = etree.HTML(content_text)
    images = html_data.xpath('//article//div[@class="image-package"]//img')
    for img in images:
        print('https:{path}'.format(path=img.xpath("@data-original-src")[0]))

    # print(image)


def read_by_page(rpl):
    if rpl.status_code == 200:
        content_text = rpl.content.decode('utf-8')
        # print(content_text)
        xpath_analyze(content_text)


def read_one_page(url_str):
    rpl = requests.get(url_str, headers=header)
    read_by_page(rpl)


header = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,'
              'application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/999.36 (KHTML, like Gecko) '
                  'Chrome/81.0.4029.3 Safari/537.36',
    'cookie': '__yadk_uid=jBBcODVC4yC8tQRWaFcQ1uDZguXPMppP; locale=zh-CN; read_mode=day; default_font=font2; remember_user_token=W1sxMTEyNjE1XSwiJDJhJDEwJG9FbWdoUGNMSE1idmFTdGUuMC5LVC4iLCIxNTc5ODUyMjAxLjk0MzY1MSJd--2f65b02d0f2ee50f0a8f463efc008e0627bc175d; _m7e_session_core=acbc2cea764d310913c1df638cf278ec; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216cf5f37ad41a6-0cdcc8ba147288-38607501-1764000-16cf5f37ad5d31%22%2C%22%24device_id%22%3A%2216cf5f37ad41a6-0cdcc8ba147288-38607501-1764000-16cf5f37ad5d31%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_utm_source%22%3A%22desktop%22%2C%22%24latest_utm_medium%22%3A%22search-input%22%7D%2C%22first_id%22%3A%22%22%7D'
}

if __name__ == '__main__':

    # read_one_page('https://www.jianshu.com/p/714b51d54f5d')
    for k in json.loads(all_article):
        for article, url in k.items():
            print('\n', article)
            read_one_page(url)
            sleep(1.5)

    # read_by_page('')
