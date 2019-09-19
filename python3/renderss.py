#!/usr/local/homebrew/bin/python3
# -*- coding:utf-8 -*-

import base64

if __name__ == "__main__":
    s = '''54.64.241.228	35048	2iYUdOGONPGf	aes-256-cfb	14:12:13	JP
3.112.188.58	18336	6BwqeD036fP6	aes-256-cfb	14:12:13	JP
3.112.244.187	40800	qdEGwkjjg4wd	aes-256-cfb	14:12:11	JP
52.193.150.185	31785	n8fegdXgjffm	aes-256-cfb	14:12:06	JP
18.182.9.75	22132	yjomm2Tcbgva	aes-256-cfb	14:03:03	JP
138.68.219.79	19214	ssx.re-25544258	aes-256-cfb	14:12:05	US
3.112.189.252	47208	oHXDDMtCRS2W	aes-256-cfb	14:12:11	JP
54.249.3.109	27380	tIpOezt0RIYD	aes-256-cfb	14:07:12	JP
138.68.216.52	15083	isx.yt-30068238	aes-256-cfb	14:12:06	US
54.95.17.252	49873	xNMuJqxUdmbF	aes-256-cfb	14:12:12	JP
172.105.226.147	17006	txK4UtQMdGKq	aes-256-cfb	14:12:13	JP
3.113.4.82	14316	zJQdzJMISW1j	aes-256-cfb	14:12:11	JP
13.230.155.198	20055	mBOhcEX4WP6T	aes-256-cfb	14:07:13	JP
3.112.197.139	49053	dx9hQq3Dcc1K	aes-256-cfb	14:12:13	JP
54.249.16.114	21158	AHLaW0OFllwn	aes-256-cfb	14:12:12	JP
13.114.165.158	33819	Gb8sSKEceXL4	aes-256-cfb	14:12:10	JP
172.105.211.10	48770	m14cGpTCb7X6	aes-256-cfb	14:12:13	JP
54.238.237.239	49996	0UFUGIHyXkB0	aes-256-cfb	14:12:07	JP
3.112.190.253	16448	X43Y5ldiO9ny	aes-256-cfb	14:12:32	JP
139.162.109.38	25258	rJt9fK1UMycL	aes-256-cfb	14:12:06	JP
172.105.228.213	36534	Mw3picafRFHR	aes-256-cfb	14:12:11	JP
172.105.217.50	37254	vCGHHM62O2zA	aes-256-cfb	14:12:11	JP
18.179.31.36	22287	Fexi3k3rw1w8	aes-256-cfb	14:12:30	JP
68.183.188.87	12884	ssx.re-16714597	aes-256-cfb	14:12:06	SG
52.192.255.131	10706	ifOMGFrJCY1w	aes-256-cfb	14:12:19	JP
172.105.206.213	48470	SUHkvIxwCgdV	aes-256-cfb	14:12:12	JP
54.238.189.48	13266	H7krbSdwQLzH	aes-256-cfb	14:12:13	JP
157.245.185.68	16301	ssx.re-68829943	aes-256-cfb	14:12:05	US
139.162.70.249	38026	0U7SAaBANQOQ	aes-256-cfb	14:12:12	JP
139.162.104.7	46458	jQpP93UZdTV0	aes-256-cfb	14:12:13	JP'''
    sn = s.split('\n')
    di = []
    for xxx in sn:
        str = xxx.split('\t')
        dictSS = {'ip': str[0], 'port': str[1], 'pass': str[2], 'enc': str[3], 'time': str[4], 'from': str[5]}
        di.append(dictSS)
        # print(xxx)
    for ssr in di:
        encbase64 = base64.b64encode("{}:{}".format(ssr['enc'], ssr['pass']).encode('utf-8')).decode('utf-8')
        print("ss://{}@{}:{}/?#{}-{}".format(encbase64, ssr['ip'], ssr['port'], ssr['from'], ssr['time']))
