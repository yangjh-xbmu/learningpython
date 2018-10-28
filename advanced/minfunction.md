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
>>> min(1,2,3)
1
>>> min(1,'2')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: '<' not supported between instances of 'str' and 'int'
>>> min('2','3')
'2'
>>> min(-1,-2)
-2。≤>>> min(-1,-2,key = abs)
-1
>>> min(-1,'-2',key = int)
'-2'
>>> min([1,2],(1,1))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: '<' not supported between instances of 'tuple' and 'list'
>>> min([1,2],(1,1),key = lambda x:x[1])
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
>>> min({},{})
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: '<' not supported between instances of 'dict' and 'dict'
>>> min({a:1,b:2},{a:1,b:3})
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'a' is not defined
>>> min({(a:1),(b:2)})
  File "<stdin>", line 1
    min({(a:1),(b:2)})
           ^
SyntaxError: invalid syntax
>>> a = [1,4,3]
>>> a[1]
4
>>> a[0]
1
>>> b = (1,2,3)
>>> b[0]
1
>>> 
```
