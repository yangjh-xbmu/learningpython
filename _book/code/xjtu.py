# -*- coding: utf-8 -*-

import re
import csv
import requests

# 先请求网页，再将数据保存到变量中


def getXjtuDonation(pageNo, pageSize):
    url = 'http://alumni.xjtu.edu.cn:9090/donation/namelist'
    params = {
        'pageNo': str(pageNo),
        'pageSize': str(pageSize),
        'billnum': '',
        'donateUserName': '',
        'orderWay': '',
        'donationid': '0'
    }
    r = requests.get(url, params=params)
    # print r.url
    r.encoding = 'utf-8'
    return r.text

# 使用正则表达式，得到需要的数据


def getData(target):
    pattern = re.compile(
        '<tr>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?</tr>', re.S)
    resulte = re.findall(pattern, target)
    # if resulte:
    #     print(resulte)
    return resulte

# 数据清理

# 定义清理工具


def purge(strings):
    return re.sub('\s|<.*?>', '', strings)

# 定义清理函数，用于清理多维列表

# 清理表头


def clearhead(lists):
    return lists[1:]

# 清理多余字符


def cleanList(lists):
    rows = []
    for x in lists:
        row = [purge(str(y)) for y in x]
        rows.append(row)
    return rows

# 将数据存储到csv文件


def save_infos(infos):
    fileName = 'data.csv'
    csvfile = open(fileName, 'a')
    writer = csv.writer(csvfile)
    for info in infos:
        writer.writerow(info)
    csvfile.close()

# 定义执行流程函数


def go():
    for x in range(1, 2):
        content = getXjtuDonation(x, 100)
        # print(content)
        resulte = getData(content)
        rows = clearhead(resulte)
        rows = cleanList(rows)
        save_infos(rows)

# 执行任务

go()
