# -*- coding: utf-8 -*-

import requests
# url = u'http://alumni.xjtu.edu.cn:9090/donation/namelist?pageNo=3&pageSize=10&billnum=&donateUserName=&orderWay=&donationid=0'
# r = requests.get(url)
# r.encoding = 'utf-8'
# content = r.text
# # print content
# f = open('xjtu.html', 'w')
# f.write(content.encode('utf-8'))
# f.close()


def getXjtuDonation(pageNo):
    url = u'http://alumni.xjtu.edu.cn:9090/donation/namelist'
    params = {
        u'pageNo': '3',
        u'pageSize': '10',
        u'billnum': '',
        u'donateUserName': '',
        u'orderWay': '',
        u'donationid': '0'
    }
    r = requests.get(url, params=params)
    r.encoding = 'utf-8'
    content = r.text
    return content

for x in range(1, 10):
    print '正在抓取第' + str(x) + '页信息……'
    content = getXjtuDonation(x + 1)
    f = open('xjtu' + str(x) + '.html', 'w')
    f.write(content.encode('utf-8'))
