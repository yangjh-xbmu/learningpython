# -*- coding: utf-8 -*-

import csv
import requests
import json

# 获取数据


def getManagerList(pageNo, pageSize):
    url = 'http://gs.amac.org.cn/amac-infodisc/api/pof/manager'
    params = {
        'rand': '0.36026727612108433',
        'page': pageNo,
        'size': pageSize
    }
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
        'Connection': 'keep-alive',
        'Content-Length': '2',
        'Content-Type': 'application/json',
        'Host': 'gs.amac.org.cn',
        'Origin': 'http://gs.amac.org.cn',
        'Referer': 'http://gs.amac.org.cn/amac-infodisc/res/pof/manager/managerList.html?nsukey=RCo1oGNVpM9EASwvsHizUZ2B%2BAcLyXDy1HB1MJ8EZD9DjLy57eycxNJUZDDac39p0k6T%2F06F0rq9kbxycTghwSz%2BNz6YhFBCCbTLNwE93GukdmK0JuKgiLn9tQicE8%2BwOiic5gxS%2BRTky%2Bmfo87O1hCq8uww0C%2FDBRa2vHhWWoUOnhbFU5Yf7vEEcJYrXLIK',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }
    payload = '{}'
    r = requests.post(url, data=payload, params=params, headers=headers)
    # print r.url
    r.encoding = 'utf-8'
    return r.text

# 解析json，得到列表数据


def getData(text):
    data = json.loads(text)['content']
    names = ['artificialPersonName',
             'establishDate',
             'fundCount',
             'fundScale',
             'hasCreditTips',
             'hasSpecialTips',
             'id',
             'inBlacklist',
             'managerHasProduct',
             'managerName',
             'officeAddress',
             'officeCity',
             'officeCoordinate',
             'officeProvince',
             'paidInCapital',
             'primaryInvestType',
             'regAdrAgg',
             'regCoordinate',
             'registerAddress',
             'registerCity',
             'registerDate',
             'registerNo',
             'registerProvince',
             'subscribedCapital',
             'url']
    infos = []
    for b in data:
        info = [b[name] for name in names]
        infos.append(info)
    return infos

# 保存到csv


def save_infos(infos):
    fileName = 'manager.csv'
    csvfile = open(fileName, 'a')
    writer = csv.writer(csvfile)
    for info in infos:
        writer.writerow(info)
    csvfile.close()

# 定义流程


def go():
    text = getManagerList(1, 50)
    data = getData(text)
    save_infos(data)

# 执行
go()
