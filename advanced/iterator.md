# Python可迭代对象

迭代器（`iterator`）有时又称游标（cursor）是程式设计的软件设计模式，可在容器物件（container，例如链表或阵列）上遍访的界面，设计人员无需关心容器物件的内存分配的实现细节。

## 可迭代对象

Python中经常使用`for`来对某个对象进行遍历，此时被遍历的这个对象就是可迭代对象，像常见的序列（字符串、列表、元组）、字典都是。如果给一个准确的定义的话，就是只要它定义了可以返回一个迭代器的`__iter__`方法，或者定义了可以支持下标索引的`__getitem__`方法，那么它就是一个可迭代对象。

## 迭代器

迭代器是通过`next()`来实现的，每调用一次他就会返回下一个元素，当没有下一个元素的时候返回一个`StopIteration`异常，所以实际上定义了这个方法的都算是迭代器。

## 生成器

生成器是构造迭代器的最简单有力的工具，与普通函数不同的只有在返回一个值的时候使用`yield`来替代`return`，然后`yield`会自动构建好`next()`和`iter()`。

## 三者之间关系

1. 可迭代对象包含迭代器。
1. 如果一个对象拥有`__iter__`方法，其是可迭代对象；如果一个对象拥有`next`方法，其是迭代器。
1. 定义可迭代对象，必须实现`__iter__`方法；定义迭代器，必须实现`__iter__`和`next`方法。

## 迭代器长度的计算

迭代器（包括生成器）是不能直接使用`len()`方法计算长度的，例如：

```python
>>>l = (i for i in xrange(100) if i&1)

>>>len(l)

Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: object of type 'generator' has no len()
```

计算迭代器的长度，我们可以先将其转化为列表再计算，但如果迭代器规模较大，这将消耗大量内存，并不是很好的解决方案：

```python
>>>len(list(l))
```

我们可以使用更为简洁的方式，即通过循环求和的方式得到迭代器的长度：

```python
>>sum(1 for _ in l)
50
```

在此基础上，我们可以定义一个函数，专门用来求迭代器（生成器）的长度：

```python
def leniter(iterator):
    """leniter(iterator): return the length of an iterator,consuming it."""
    if hasattr(iterator, "__len__"):
        return len(iterator)
    nelements = 0
    for _ in iterator:
        nelements += 1
    return nelements
```
