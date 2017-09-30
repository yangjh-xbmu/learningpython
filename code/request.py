# -*- coding: utf-8 -*-

import requests
import re
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
        u'pageNo': str(pageNo),
        u'pageSize': '10',
        u'billnum': '',
        u'donateUserName': '',
        u'orderWay': '',
        u'donationid': '0'
    }
    r = requests.get(url, params=params)
    print r.url
    r.encoding = 'utf-8'
    content = r.text
    return content

# for x in range(1, 10):
#     print '正在抓取第' + str(x) + '页信息……'
#     content = getXjtuDonation(x+1)
#     f = open('xjtu' + str(x) + '.html', 'w')
#     f.write(content.encode('utf-8'))
#     f.close()
target = '''<tr>
                         <td>
                                <a href="javascript:void(0);" target="_blank" title="">
                                            梁旭花
                                </a>
                         </td>
                         <td>


                                        10
                                (人民币
                                )

                         </td>
                         <td>
                            <a href="/donation/item-view?donationId=2090&amp;type=1" title="其他">
                                    其他
                            </a>
                         </td>
                         <td>
                            <a href="javascript:void(0);">
                                2017-08-07
                            </a>
                         </td>
                         <td>
                            <a href="javascript:void(0);">
                                 亲临学校
                            </a>
                         </td>
                         <td>
                            <a href="javascript:void(0);">
                                个人用户
                            </a>
                         </td>
                         <!--<td title="AlumniDonation-20170808139">
                                    Alum ...
                         </td>-->
                    </tr>'''


def getDate():
    pattern = re.compile(
        r'<tr>.*?<td>.*?<a.*?>(?P<name>.*?)<\/a>.*?<\/td>.*?<td>(?P<amount>.*?)<\/td>.*?<\/tr>', re.S)
    resulte = re.fullmatch(pattern, target)
    print resulte.group('name')
    print resulte.group('amount')
    return resulte


data = getDate()

# for x in data:
#     for i in x:
#         print i
