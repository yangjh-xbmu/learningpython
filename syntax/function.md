# 函数

函数是可重用的代码块，使用函数可以帮助我们组织代码的结构。我们创建函数的目的，是能在程序运行中多次使用一系列代码，而不用重复书写代码。

## 创建函数

Python使用def关键词创建函数，语法如下：

```python
def function_name(arg1, arg2, arg3, .... argN):
     #statement inside function
```

空白区在 Python 中十分重要。实际上，空白区在各行的开头非常重要。这被称作缩进（Indentation）。在逻辑行的开头留下空白区（使用空格或制表符）用以确定各逻辑行的缩进级别，而后者又可用于确定语句的分组。

这意味着放置在一起的语句必须拥有相同的缩进。每一组这样的语句被称为块（block）。有一件事你需要记住：错误的缩进可能会导致错误。

所有在函数内部的声明，都必须使用相等的缩进。函数可以没有参数，也可以有多个参数。多个参数之间用逗号隔开。还可以使用pass关键字忽略掉函数主题的声明。

我们看一个函数的例子，下面的函数将计算指定范围的整数之和：

```python
def sum(start, end):
    result = 0
    for i in range(start, end + 1):
        result += i
    print(result)

sum(1, 10)
```

在上面的代码中，我们定义了一个叫作`sum()`的函数，该函数有两个参数（`start`和`end`），该函数将从`start`开始，累加到`end`，最后打印出累积之和。代码运行的结果为55。

## 函数返回值

上文定义的函数只是简单地在控制台打印出结果，如果我们想要将计算结果赋值给变量，以便做更深入的处理时应该怎么办？当我们遇到这种情况时，可使用`return`语句，将返回函数计算结果并且退出函数。例如：

```python
def sumReturn(start, end):
    result = 0
    for i in range(start, end + 1):
        result += i
    return result

a = sumReturn(1, 5)
print(a)
```

在上面这段代码中，我们定义了有返回值的函数`sumReturn()`，并将其结果赋值给变量`a`。上面代码的运行结果为15。

当然，return语句也可以不返回值，而是用来退出函数（实际上会返回None，为NoneType对象）。每一个函数都在其末尾隐含了一句 return None，除非你写了你自己的 return 语句。

```python
def sum2(start, end):
    if(start > end):
        print("start should be less than end")
        return
    result = 0
    for i in range(start, end + 1):
        result += i
    return result

s = sum2(110, 50)
print(s, type(s))
```

上述代码的运行结果如下：

```python
start should be less than end
None <class 'NoneType'>
```

在Python中，如果你不指定return的返回值，则会返回None值。

## 全局变量和局域变量

全局变量指的是不属于任何函数，但又可以在函数内外访问的变量。而局域变量指的是在函数内部声明的变量，局域变量只能在函数内部使用，无法在函数外访问（函数执行完后，会销毁内部定义的局部变量）。

下面我们通过例子来演示这两者的区别：

```python
global_var = 12         # 定义全局变量

def func():
    local_var = 100     # 定义局部变量
    print(global_var)   # 可以在函数内部访问全局变量

func()                  # 调用函数func()

print(local_var)        # 无法访问变量local_var
```

上述代码将会出现错误：

```python
NameError: name 'local_var' is not defined
```

我们再看一个例子：

```python
xy = 100         # 定义全局变量xy

def func():
    xy = 200    # 定义局部变量xy
    print(xy)   # 此时访问的是局部变量xy

func()          # 调用函数func()
```

该代码显示的结果是200，不是100。

使用`global`关键字，可以将局部变量同全局变量绑定在一起。例如：

```python
t = 1

def increment():
    global t    # 现在的变量t在函数内外都是一致的
    t = t + 1
    print(t)    # 输出 2

increment()
print(t)        # 输出 2
```

使用`global`关键字声明全局变量时，无法直接赋值，比如“global t = 1”的写法存在语法错误。

## 参数的默认值

为参数指定默认值，只需在定义函数时使用赋值语句即可。例如：

```python
def func(i, j = 100):
    print(i, j)
```

上述定义的函数func()有两个参数i和j。j的默认值为100，这意味着我们在调用这个函数的时候可以忽略掉j的值，比如func(2)，运行结果为2 100。

## 关键字参数

为函数传递参数值的方法有两种：位置参数和关键字参数。我们之前调用函数的时候都使用的是位置参数。下面我们看如何使用关键字参数：

```python
def named_args(name, greeting):
    print(greeting + " " + name)

named_args(name='jim', greeting='Hello')
named_args(greeting='Hello', name='jim')
named_args('jim', greeting='hello')
```
上述代码运行结果都是“hello jim"。

关键字参数使用“name=value”的名称、值对传递数据，正如上面代码演示的那样，使用关键字参数的时候，参数的顺序是可以调换的，而且位置参数和关键字参数可以混合使用（只能先使用位置参数，后使用关键字参数）。

## 返回多个值

我们可以通过在return语句中使用逗号，将多个值返回，这种返回值的类型是元组。例如：

```python
def bigger(a, b):
    if a > b:
        return a, b
    else:
        return b, a

s = bigger(12, 100)
print(s)
print(type(s))
```

运行结果为：

```python
(100, 12)
<class 'tuple'>
```

## 函数文档字符串

Python 有一个甚是优美的功能称作文档字符串（Documentation Strings），在称呼它时通常会使用另一个短一些的名字docstrings。DocStrings 是一款你应当使用的重要工具，它能够帮助你更好地记录程序并让其更加易于理解。令人惊叹的是，当程序实际运行时，我们甚至可以通过一个函数来获取文档！

```python
def print_max(x, y):
    '''Prints the maximum of two numbers.

    The two values must be integers.'''
    # 如果可能，将其转换至整数类型
    x = int(x)
    y = int(y)

    if x > y:
        print(x, 'is maximum')
    else:
        print(y, 'is maximum')

print_max(3, 5)
print(print_max.__doc__)
输出：

$ python function_docstring.py
5 is maximum
Prints the maximum of two numbers.

    The two values must be integers.
```

该文档字符串所约定的是一串多行字符串，其中第一行以某一大写字母开始，以句号结束。第二行为空行，后跟的第三行开始是任何详细的解释说明。强烈建议你的文档字符串中都遵循这一约定。

我们可以通过使用函数的 `__doc__`（注意其中的双下划线）属性（属于函数的名称）来获取函数 print_max 的文档字符串属性。
