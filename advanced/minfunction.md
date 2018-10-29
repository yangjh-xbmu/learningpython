# min函数

## 描述

求多个参数中的最小值，或者是可迭代数据中的最小元素。

## 语法

```python
min(iterable, *[, key, default])
min(arg1, arg2, *args[, key])
```

## 返回值

最小的元素，可能是字符串、数字，也可能是元组、列表。

## 实例

```python
>>> min(1,2,3)  # 求三个元素中的最小值
1
>>> min(1,'2') # 不同类型的变量无法直接求最小值
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: '<' not supported between instances of 'str' and 'int'
>>> min('2','3') # 可以对字符串求最小值，按字母顺序求值
'2'
>>> min(-1,-2) # 可以对负数求最小值
-2
>>> min(-1,-2,key = abs) # key参数可以是函数，例如abs()
-1
>>> min(-1,'-2',key = int) # key参数为类型转换函数
'-2'
>>> min([1,2],(1,1)) # 无法直接对元素和列表求最小值
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: '<' not supported between instances of 'tuple' and 'list'
>>> min([1,2],(1,1),key = lambda x:x[1]) # key值可以是列表中的某个元素
(1, 1)
>>> min([1,2],(1,3),key = lambda x:x[1])
[1, 2]
>>> min([1,2,3],(1,3,3),key = lambda x:x[1])
[1, 2, 3]
>>> min([1,2,3],(1,3,3),key = lambda x:x[2])
[1, 2, 3]
>>> min([1,4,3],(1,3,3),key = lambda x:x[2])
[1, 4, 3]
>>> min([1,4,3],(1,3,3),key = lambda x:x[0])
[1, 4, 3]
>>> min([1,4,3],(1,3,3),key = lambda x:x[1])
(1, 3, 3)
>>> min([1,4,3],(1,3,3),key = lambda x:x[1])
(1, 3, 3)
```
