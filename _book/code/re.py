# -*- coding: utf-8 -*-

import re

pattern = re.compile(u'中华人民共和国')

resulte1 = re.search(pattern, u'中华人民共和国万岁')
resulte2 = re.search(pattern, u'中国共和国万岁')

print resulte1.group(), resulte2

f = open('xjtu1.html', 'r')
content = f.read()
f.close()
# print content

pattern = re.compile(u'.*', re.S)
resulte = re.search(pattern, content).group()

print resulte
