# zip函数

## 描述

将不同迭代对象中的元素整合为一个迭代对象。

## 语法

```python
zip(*iterables)
```

## 返回值

返回元组。

## 特殊用法

`zip()`方法和`*`运算符连用时，用来拆解一个列表。

## 实例

```python
>>> x = [1, 2, 3]
>>> y = [4, 5, 6]
>>> zipped = zip(x, y)
>>> list(zipped)
[(1, 4), (2, 5), (3, 6)]
>>> x2, y2 = zip(*zip(x, y))
>>> x == list(x2) and y == list(y2)
True
```
