# 单、双下划线的区别

在学习Python的时候，估计会对Python代码中的下划线产生困惑，现总结如下：

## 单下划线开头

在Python中不存在真正意义上的私有方法或者属性，前面加单下划线`_`只是表示你不应该去访问这个方法或者属性，因为它不是API的一部分。

```python
class BaseForm(StrAndUnicode):
    ...

    def _get_errors(self):
        "Returns an ErrorDict for the data provided for the form"
        if self._errors is None:
            self.full_clean()
        return self._errors

    errors = property(_get_errors)
```

这段代码的设计就是`errors`属性是对外API的一部分，如果你想获取错误详情，应该访问`errors`属性，而不是（也不应该）访问`_get_errors`方法。

## 双下划线开头

设计双下划线开头的初衷和目的，是为了避免子类覆盖父类的方法。

```python
class A(object):

    def __method(self):
        print("I'm a method in class A")

    def method_x(self):
        print("I'm another method in class A\n")

    def method(self):
        self.__method()
        self.method_x()


class B(A):

    def __method(self):
        print("I'm a method in class B")

    def method_x(self):
        print("I'm another method in class B\n")


if __name__ == '__main__':

    print("situation 1:")
    a = A()
    a.method()

    b = B()
    b.method()

    print("situation 2:")
    a._A__method()
```

执行结果：

```bash
situation 1:
I'm a method in class A
I'm another method in class A

I'm a method in class A
I'm another method in class B

situation 2:
I'm a method in class A
```

## 双下划线开头和结尾

一般来说像`__this__`这种开头结尾都加双下划线的方法表示这是Python自己调用的，你不要调用。比如我们可以调用`len()`函数来求长度，其实它后台是调用了`__len__()`方法。一般我们应该使用`len`，而不是直接使用`__len__()`。正如下面的例子：

```python
class Room(object):

    def __init__(self):
        self.people = []

    def add(self, person):
        self.people.append(person)

    def __len__(self):
        return len(self.people)

room = Room()
room.add("Igor")
print len(room)
```

这个例子中，因为我们实现了`__len__()`，所以`Room`对象也可以使用`len`函数了。
