#!/usr/local/homebrew/bin/python3
# -*- coding:utf-8 -*-

import base64


def web_site():
    s = '''157.245.150.194	17934	aes-256-cfb	isx.yt-70795299	18:27:06	SG
118.27.4.161	15414	chacha20	W2019S	18:27:08	JP
172.105.193.88	26954	aes-256-cfb	57IhGRaJcKxf	18:27:16	JP
172.104.79.249	12060	aes-256-cfb	8je5DVcUSDAO	18:27:14	JP
52.69.248.106	52989	aes-256-cfb	W2rmeOGimi0F	18:27:21	JP
3.112.217.105	46943	aes-256-cfb	bAMy7mAxDCsX	18:27:27	JP
159.65.99.228	16601	aes-256-cfb	ssx.re-71154534	18:27:05	US
198.199.116.67	18315	aes-256-cfb	ss8.pm-71937212	18:27:05	US
45.88.42.58	3572	rc4-md5	cht1997...///	18:27:15	SG
18.176.55.40	25028	aes-256-cfb	A5itbvPy4x9I	18:27:19	JP
192.241.215.160	15710	aes-256-cfb	isx.yt-87085518	18:27:05	US
165.22.107.9	10178	aes-256-cfb	isx.yt-20325887	18:27:06	SG
172.105.71.4	8099	aes-256-cfb	eIW0Dnk69454e6nSwuspv9DmS201tQ0D	18:27:11	DE
45.84.1.61	34567	aes-256-cfb	11284296	18:27:06	US
172.104.111.87	39386	aes-256-cfb	TtEE5aSh1DsR	18:27:12	JP
80.93.182.63	39838	aes-256-cfb	n1CqnjERurS3	18:27:09	RU
165.22.123.120	12626	aes-256-cfb	ss8.pm-12675297	18:27:05	GB
172.104.105.168	30707	aes-256-cfb	f52XiTuuv2sq	18:27:14	JP
67.21.94.192	99	aes-256-cfb	dongtaiwang.com	18:27:17	US'''
    sn = s.split('\n')
    di = []
    for xxx in sn:
        str = xxx.replace(' ', '').split('\t')
        dictSS = {'ip': str[0], 'port': str[1], 'pass': str[2], 'enc': str[3], 'time': str[4], 'from': str[5]}
        di.append(dictSS)
        # print(xxx)
    for ssr in di:
        encbase64 = base64.b64encode("{}:{}".format(ssr['enc'], ssr['pass']).encode('utf-8')).decode('utf-8')
        print("ss://{}@{}:{}/?#{}-{}".format(encbase64, ssr['ip'], ssr['port'], ssr['from'], ssr['time']))


def free_ss():
    niu_neng = [
        {'IP': '54.65.52.79', 'Port': '50237', 'Password': 'pMw7tAEKyejw', 'Crypton': 'aes-256-cfb', 'Time': '11:12:16',
         'County': 'JP'},
        {'IP': '138.68.212.168', 'Port': '16858', 'Password': 'ss8.pm-50297644', 'Crypton': 'aes-256-cfb',
         'Time': '11:12:05', 'County': 'US'},
        {'IP': '159.203.193.202', 'Port': '10741', 'Password': 'ssx.re-60193930', 'Crypton': 'aes-256-cfb',
         'Time': '11:12:05', 'County': 'US'},
        {'IP': '54.199.151.23', 'Port': '9515', 'Password': 'LusoBN5wkL3c', 'Crypton': 'aes-256-cfb',
         'Time': '11:12:13', 'County': 'JP'},
        {'IP': '3.112.41.63', 'Port': '15212', 'Password': 'GRzV3SUyKnF7', 'Crypton': 'aes-256-cfb', 'Time': '11:12:19',
         'County': 'JP'},
        {'IP': '68.183.229.253', 'Port': '16388', 'Password': 'ssx.re-66548122', 'Crypton': 'aes-256-cfb',
         'Time': '11:12:06', 'County': 'SG'},
        {'IP': '45.90.142.24', 'Port': '2236', 'Password': 'lncn.org p6', 'Crypton': 'rc4', 'Time': '11:12:13',
         'County': 'JP'},
        {'IP': '165.22.54.117', 'Port': '12763', 'Password': 'ss8.pm-71146763', 'Crypton': 'aes-256-cfb',
         'Time': '11:12:06', 'County': 'SG'},
        {'IP': '85.117.235.147', 'Port': '2236', 'Password': 'lncn.org c2', 'Crypton': 'rc4', 'Time': '11:12:15',
         'County': 'RU'},
        {'IP': '104.248.152.32', 'Port': '17922', 'Password': 'isx.yt-62431042', 'Crypton': 'aes-256-cfb',
         'Time': '11:12:06', 'County': 'SG'},
        {'IP': '159.203.206.133', 'Port': '13520', 'Password': 'isx.yt-19456208', 'Crypton': 'aes-256-cfb',
         'Time': '11:12:05', 'County': 'US'},
        {'IP': '167.71.141.11', 'Port': '11928', 'Password': 'ss8.pm-91667999', 'Crypton': 'aes-256-cfb',
         'Time': '11:12:05', 'County': 'GB'},
        {'IP': '165.22.133.55', 'Port': '17113', 'Password': 'ssx.re-87724836', 'Crypton': 'aes-256-cfb',
         'Time': '11:12:05', 'County': 'US'},
        {'IP': '45.77.134.121', 'Port': '2236', 'Password': 'lncn.org h2', 'Crypton': 'rc4', 'Time': '11:12:15',
         'County': 'JP'},
        {'IP': '159.203.198.140', 'Port': '16566', 'Password': 'isx.yt-56550805', 'Crypton': 'aes-256-cfb',
         'Time': '11:12:05', 'County': 'US'},
        {'IP': '194.124.34.249', 'Port': '2236', 'Password': 'lncn.org p6', 'Crypton': 'rc4', 'Time': '11:12:07',
         'County': 'MY'},
        {'IP': '159.203.198.100', 'Port': '18716', 'Password': 'isx.yt-60337840', 'Crypton': 'aes-256-cfb',
         'Time': '11:02:05', 'County': 'US'},
        {'IP': '114.38.82.133', 'Port': '3572', 'Password': 'cht1997...///', 'Crypton': 'rc4-md5', 'Time': '11:12:27',
         'County': 'TW'},
        {'IP': '52.194.215.226', 'Port': '37799', 'Password': 'gc98lmtXMbkb', 'Crypton': 'aes-256-cfb',
         'Time': '11:12:11', 'County': 'JP'},
        {'IP': '45.33.82.202', 'Port': '443', 'Password': '9d6cceaa373bf2c8acb22e60b6a58be6', 'Crypton': 'aes-256-cfb',
         'Time': '11:07:14', 'County': 'US'},
        {'IP': '198.13.56.96', 'Port': '2236', 'Password': 'lncn.org h2', 'Crypton': 'rc4', 'Time': '11:12:15',
         'County': 'US'},
        {'IP': '45.89.230.74', 'Port': '2236', 'Password': 'lncn.org c2', 'Crypton': 'rc4', 'Time': '11:12:08',
         'County': 'RU'},
        {'IP': '52.195.10.232', 'Port': '37962', 'Password': 'z3UJc1Ihc8MW', 'Crypton': 'aes-256-cfb',
         'Time': '11:12:28', 'County': 'JP'},
        {'IP': '52.68.175.191', 'Port': '51895', 'Password': 'c21B7oInRDJF', 'Crypton': 'aes-256-cfb',
         'Time': '11:12:11', 'County': 'JP'},
        {'IP': '45.129.3.231', 'Port': '2236', 'Password': 'lncn.org c2', 'Crypton': 'rc4', 'Time': '11:12:10',
         'County': 'RU'},
        {'IP': '108.160.130.243', 'Port': '2236', 'Password': 'lncn.org h2', 'Crypton': 'rc4', 'Time': '11:12:16',
         'County': 'JP'},
        {'IP': '157.245.146.209', 'Port': '15722', 'Password': 'isx.yt-36962774', 'Crypton': 'aes-256-cfb',
         'Time': '11:12:06', 'County': 'SG'},
        {'IP': '85.117.235.82', 'Port': '2236', 'Password': 'lncn.org c2', 'Crypton': 'rc4', 'Time': '11:12:10',
         'County': 'RU'},
        {'IP': '45.79.45.155', 'Port': '51174', 'Password': 'pBzioBo1MoM2', 'Crypton': 'aes-256-cfb',
         'Time': '11:12:15', 'County': 'US'},
        {'IP': '13.115.123.101', 'Port': '14174', 'Password': 'PIY0Nc3wV6EW', 'Crypton': 'aes-256-cfb',
         'Time': '11:12:38', 'County': 'JP'},
        {'IP': '178.128.213.50', 'Port': '15722', 'Password': 'isx.yt-24580860', 'Crypton': 'aes-256-cfb',
         'Time': '11:12:06', 'County': 'SG'},
        {'IP': '13.125.154.75', 'Port': '13498', 'Password': 'pO5CgCQeDN2M', 'Crypton': 'aes-256-cfb',
         'Time': '11:12:23', 'County': 'KR'},
        {'IP': '176.58.121.60', 'Port': '19289', 'Password': 'QZY5fDRp6aHD', 'Crypton': 'aes-256-cfb',
         'Time': '11:12:10', 'County': 'GB'},
        {'IP': '54.249.24.12', 'Port': '43566', 'Password': 'Fs7YdMOLVq6T', 'Crypton': 'aes-256-cfb',
         'Time': '11:12:11', 'County': 'JP'}
    ]
    niu_neng.sort(key=(lambda item: item['Time']), reverse=True)
    for item in niu_neng:
        encbase64 = base64.b64encode("{}:{}".format(item['Crypton'], item['Password']).encode('utf-8')).decode('utf-8')
        print("ss://{}@{}:{}/?#{}-{}".format(encbase64, item['IP'], item['Port'], item['County'], item['Time']))


if __name__ == "__main__":
    web_site()
