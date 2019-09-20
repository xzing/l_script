#!/usr/local/homebrew/bin/python3
# -*- coding:utf-8 -*-

import base64


def web_site():
    s = '''157.245.160.79	11678	ssx.re-44764782	aes-256-cfb	17:12:05	US
    52.192.255.131	10706	ifOMGFrJCY1w	aes-256-cfb	17:12:11	JP
    54.249.16.114	21158	AHLaW0OFllwn	aes-256-cfb	17:12:21	JP
    3.112.190.253	16448	X43Y5ldiO9ny	aes-256-cfb	17:12:28	JP
    54.249.3.109	27380	tIpOezt0RIYD	aes-256-cfb	17:12:17	JP
    54.238.189.48	13266	H7krbSdwQLzH	aes-256-cfb	17:07:47	JP
    139.162.109.38	25258	rJt9fK1UMycL	aes-256-cfb	17:12:06	JP
    139.162.70.249	38026	0U7SAaBANQOQ	aes-256-cfb	17:12:14	JP
    18.179.31.36	22287	Fexi3k3rw1w8	aes-256-cfb	17:07:22	JP
    172.104.114.238	32914	196OzJ8Lxrh0	aes-256-cfb	17:12:14	JP
    3.113.4.82	14316	zJQdzJMISW1j	aes-256-cfb	17:12:28	JP
    3.112.189.252	47208	oHXDDMtCRS2W	aes-256-cfb	17:12:11	JP
    172.105.217.50	37254	vCGHHM62O2zA	aes-256-cfb	17:12:10	JP
    13.114.165.158	33819	Gb8sSKEceXL4	aes-256-cfb	17:02:34	JP
    172.105.211.10	48770	m14cGpTCb7X6	aes-256-cfb	17:12:12	JP
    172.105.228.213	36534	Mw3picafRFHR	aes-256-cfb	17:12:10	JP
    139.162.104.7	46458	jQpP93UZdTV0	aes-256-cfb	17:12:12	JP
    138.68.211.26	13051	ssx.re-43731273	aes-256-cfb	17:12:04	US
    3.112.244.187	40800	qdEGwkjjg4wd	aes-256-cfb	17:12:51	JP
    172.105.206.213	48470	SUHkvIxwCgdV	aes-256-cfb	17:12:11	JP
    54.95.17.252	49873	xNMuJqxUdmbF	aes-256-cfb	17:12:16	JP
    54.238.237.239	49996	0UFUGIHyXkB0	aes-256-cfb	17:12:35	JP
    139.162.124.153	31554	QRgf0CkJuV4Y	aes-256-cfb	17:12:06	JP
    13.230.155.198	20055	mBOhcEX4WP6T	aes-256-cfb	17:02:27	JP
    172.105.226.147	17006	txK4UtQMdGKq	aes-256-cfb	17:12:11	JP
    18.182.9.75	22132	yjomm2Tcbgva	aes-256-cfb	17:02:14	JP
    68.183.225.185	12060	ssx.re-27936759	aes-256-cfb	17:12:06	SG
    3.112.188.58	18336	6BwqeD036fP6	aes-256-cfb	17:02:47	JP
    3.112.197.139	49053	dx9hQq3Dcc1K	aes-256-cfb	17:12:16	JP
    172.105.215.98	44108	wQxjMI0STNZc	aes-256-cfb	17:12:06	JP
    103.29.68.199	19039	CIbNQGo4cHyx	aes-256-cfb	17:12:10	JP
    52.193.150.185	31785	n8fegdXgjffm	aes-256-cfb	17:12:15	JP
    54.64.241.228	35048	2iYUdOGONPGf	aes-256-cfb	17:12:58	JP'''
    sn = s.split('\n')
    di = []
    for xxx in sn:
        str = xxx.replace(' ').split('\t')
        dictSS = {'ip': str[0], 'port': str[1], 'pass': str[2], 'enc': str[3], 'time': str[4], 'from': str[5]}
        di.append(dictSS)
        # print(xxx)
    for ssr in di:
        encbase64 = base64.b64encode("{}:{}".format(ssr['enc'], ssr['pass']).encode('utf-8')).decode('utf-8')
        print("ss://{}@{}:{}/?#{}-{}".format(encbase64, ssr['ip'], ssr['port'], ssr['from'], ssr['time']))


def free_ss():
    niu_neng = [
        {'IP': '178.79.191.199', 'Port': '9924', 'Password': 'rX1sQJlQXrq3', 'Crypton': 'aes-256-cfb',
         'Time': '08:02:10', 'County': 'GB'},
        {'IP': '3.112.214.226', 'Port': '10439', 'Password': 'DRmcyG7v6fG4', 'Crypton': 'aes-256-cfb',
         'Time': '08:07:17', 'County': 'JP'},
        {'IP': '172.105.211.10', 'Port': '48770', 'Password': 'm14cGpTCb7X6', 'Crypton': 'aes-256-cfb',
         'Time': '08:12:12', 'County': 'JP'},
        {'IP': '172.105.217.50', 'Port': '37254', 'Password': 'vCGHHM62O2zA', 'Crypton': 'aes-256-cfb',
         'Time': '08:12:10', 'County': 'JP'},
        {'IP': '138.68.219.59', 'Port': '15903', 'Password': 'isx.yt-50802242', 'Crypton': 'aes-256-cfb',
         'Time': '08:07:04', 'County': 'US'},
        {'IP': '18.179.11.102', 'Port': '20203', 'Password': 'NwtNJsD119lf', 'Crypton': 'aes-256-cfb',
         'Time': '08:12:12', 'County': 'JP'},
        {'IP': '172.105.226.147', 'Port': '17006', 'Password': 'txK4UtQMdGKq', 'Crypton': 'aes-256-cfb',
         'Time': '08:12:11', 'County': 'JP'},
        {'IP': '172.105.206.213', 'Port': '48470', 'Password': 'SUHkvIxwCgdV', 'Crypton': 'aes-256-cfb',
         'Time': '08:12:12', 'County': 'JP'},
        {'IP': '172.104.114.238', 'Port': '32914', 'Password': '196OzJ8Lxrh0', 'Crypton': 'aes-256-cfb',
         'Time': '08:12:10', 'County': 'JP'},
        {'IP': '167.71.198.71', 'Port': '14275', 'Password': 'isx.yt-12599395', 'Crypton': 'aes-256-cfb',
         'Time': '08:12:06', 'County': 'SG'},
        {'IP': '138.68.210.60', 'Port': '18182', 'Password': 'isx.yt-89996459', 'Crypton': 'aes-256-cfb',
         'Time': '08:07:04', 'County': 'US'},
        {'IP': '139.162.106.86', 'Port': '9136', 'Password': 'PXV9wE4arGza', 'Crypton': 'aes-256-cfb',
         'Time': '08:12:10', 'County': 'JP'},
        {'IP': '212.71.239.20', 'Port': '39670', 'Password': 'SrM2ZT5NQJUP', 'Crypton': 'aes-256-cfb',
         'Time': '08:02:10', 'County': 'GB'},
        {'IP': '139.162.109.38', 'Port': '25258', 'Password': 'rJt9fK1UMycL', 'Crypton': 'aes-256-cfb',
         'Time': '08:12:06', 'County': 'JP'},
        {'IP': '139.162.70.249', 'Port': '38026', 'Password': '0U7SAaBANQOQ', 'Crypton': 'aes-256-cfb',
         'Time': '08:12:31', 'County': 'JP'},
        {'IP': '3.112.231.225', 'Port': '42936', 'Password': '43Lp9bSJsEl7', 'Crypton': 'aes-256-cfb',
         'Time': '08:12:24', 'County': 'JP'},
        {'IP': '54.249.87.198', 'Port': '32974', 'Password': '6YDLHiYBKaqJ', 'Crypton': 'aes-256-cfb',
         'Time': '08:13:08', 'County': 'JP'},
        {'IP': '45.33.40.14', 'Port': '16297', 'Password': 'ydEdVhcnhZjQ', 'Crypton': 'aes-256-cfb', 'Time': '08:07:10',
         'County': 'US'},
        {'IP': '139.162.124.153', 'Port': '31554', 'Password': 'QRgf0CkJuV4Y', 'Crypton': 'aes-256-cfb',
         'Time': '07:57:06', 'County': 'JP'},
        {'IP': '172.105.228.213', 'Port': '36534', 'Password': 'Mw3picafRFHR', 'Crypton': 'aes-256-cfb',
         'Time': '08:12:11', 'County': 'JP'},
        {'IP': '13.230.155.198', 'Port': '20055', 'Password': 'mBOhcEX4WP6T', 'Crypton': 'aes-256-cfb',
         'Time': '07:42:42', 'County': 'JP'},
        {'IP': '157.245.198.175', 'Port': '10443', 'Password': 'isx.yt-24893190', 'Crypton': 'aes-256-cfb',
         'Time': '08:12:06', 'County': 'SG'},
        {'IP': '13.230.8.111', 'Port': '46301', 'Password': 'qAxUZM9h6pnw', 'Crypton': 'aes-256-cfb',
         'Time': '08:12:12', 'County': 'JP'},
        {'IP': '104.237.152.5', 'Port': '15933', 'Password': 'QaUTl3Nkd04x', 'Crypton': 'aes-256-cfb',
         'Time': '08:07:09', 'County': 'US'},
        {'IP': '13.231.219.3', 'Port': '35015', 'Password': 'lKx3taAxvzAW', 'Crypton': 'aes-256-cfb',
         'Time': '08:12:18', 'County': 'JP'},
        {'IP': '13.114.172.140', 'Port': '17495', 'Password': 'JBz5xcdGnZrC', 'Crypton': 'aes-256-cfb',
         'Time': '08:12:17', 'County': 'JP'},
        {'IP': '3.113.33.157', 'Port': '41423', 'Password': 'sleGZmK6vJ2A', 'Crypton': 'aes-256-cfb',
         'Time': '08:12:42', 'County': 'JP'},
        {'IP': '138.68.220.125', 'Port': '14654', 'Password': 'isx.yt-41870149', 'Crypton': 'aes-256-cfb',
         'Time': '08:12:05', 'County': 'US'},
        {'IP': '178.79.140.49', 'Port': '40834', 'Password': '9Z1bUHwHtM2r', 'Crypton': 'aes-256-cfb',
         'Time': '08:02:12', 'County': 'GB'},
        {'IP': '103.29.68.199', 'Port': '40310', 'Password': 'jij9hPjvnOc1', 'Crypton': 'aes-256-cfb',
         'Time': '08:12:08', 'County': 'JP'},
        {'IP': '139.162.104.7', 'Port': '46458', 'Password': 'jQpP93UZdTV0', 'Crypton': 'aes-256-cfb',
         'Time': '08:12:22', 'County': 'JP'},
    ]
    for item in niu_neng:
        encbase64 = base64.b64encode("{}:{}".format(item['Crypton'], item['Password']).encode('utf-8')).decode('utf-8')
        print("ss://{}@{}:{}/?#{}-{}".format(encbase64, item['IP'], item['Port'], item['County'], item['Time']))


if __name__ == "__main__":
    free_ss()
