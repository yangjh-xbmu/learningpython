# -*- coding: utf-8 -*-
# 注释不会运行
print "hello world"
a = 1
b = '1'
print type(a)
print type(b)
print 3+4
print 4/3
print 4/float(3)
print float(4/3)
print '\''
print '\\'

print 'y' + 'x'
print 'y'*5


a = 'yangps'
print a[0]
print a[5]
b = u'中华人民共和国'
print b[0]
print b[0:5]

# 元组
a = (1, 2, 3)
a = (1)
a = (1,)

# 列表
a = []
a = [1, 2, 3]
a = [1, 'str', [1, 2, 3]]

print a[2][1]

# 引用
c = [1, 2, 3]
d = c
d[0] = 4
print c


# 字典
a = {'a': 1, 'b': 2}
print a
print a['a'], a['b']
print a.keys()
print a.values()
print a.items()

# 自定义函数


def my_square(x):
    y = x*x
    return y

print my_square(5)

# 分支
age = 65
if age > 60:
    print 'old'
elif age > 30:
    print 'adult'
elif age > 10:
    print 'teen'
else:
    print 'kid'

# 循环
mylist = [1, 2, 3, 4]
for i in mylist:
    print(i)

# 循环添加列表元素
b = []
for a in range(1, 100):
    b.append(a)
print b

b = [x for x in range(1, 100)]
print b

import random
b = []
for x in range(1, 100):
    b.append(random.randint(1, 10))
print b

b = [random.randint(1, 10) for x in range(1, 100)]
print b

print[1 for x in range(1, 100)]
