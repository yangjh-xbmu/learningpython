# 模块

Python模块是一个包含有函数、变量、类和常量等等内容的python文件。模块帮助我们将相关的代码组织在一起，例如math模块拥有数学相关的函数。

## 创建模块

创建一个名为`mymodule.py`的新文件，并写入下面的代码：

```python
foo = 100

def hello():
    print("i am from mymodule.py")
```

在这个文件中，我们定义了一个全部变量foo和一个名为hello()的方法。现在我们可以使用import关键词来引入这个模块，并使用`mymodule.py`中的变量和函数：

```python
import mymodule

print(mymodule.foo)
mymodule.hello()
```

上述代码的运行结果如下：

```python
100
i am from mymodule.py
```

如之前代码所示，调用模块的变量和函数时，需要指定模块的名称。

## 使用模块中的指定内容

当我们使用import声明导入模块时，模块中的所有内容都被导入到当前文件中。如果我们只需要模块中的个别内容时该如何操作呢？使用from关键词，就可以达到这样的目的，比如：

```python
from mymodule import foo
print(foo)
```

上述代码的运行结果为100。

当使用from improt语句导入特定内容后，访问这些内容就不需要再使用模块名了。

## dir函数

内置的 dir() 函数能够返回由对象所定义的名称列表。 如果这一对象是一个模块，则该列表会包括函数内所定义的函数、类与变量。
该函数接受参数。 如果参数是模块名称，函数将返回这一指定模块的名称列表。 如果没有提供参数，函数将返回当前模块的名称列表。

```python
>>> import sys

# 给出 sys 模块中的属性名称
>>> dir(sys)
['__displayhook__', '__doc__',
'argv', 'builtin_module_names',
'version', 'version_info']
# only few entries shown here

# 给出当前模块的属性名称
>>> dir()
['__builtins__', '__doc__',
'__name__', '__package__']

# 创建一个新的变量 'a'
>>> a = 5

>>> dir()
['__builtins__', '__doc__', '__name__', '__package__', 'a']
```

## 包

包是指一个包含模块与一个特殊的 \_\_init\_\_.py 文件的文件夹，后者向 Python 表明这一文件夹是特别的，因为其包含了 Python 模块。

假设你想创建一个名为“world”的包，其中还包含着 ”asia“、”africa“等其它子包，同时这些子包都包含了诸如”india“、”madagascar“等模块。下面是你会构建出的文件夹的结构：

```python
- <some folder present in the sys.path>/
    - world/
        - __init__.py
        - asia/
            - __init__.py
            - india/
                - __init__.py
                - foo.py
        - africa/
            - __init__.py
            - madagascar/
                - __init__.py
                - bar.py
```

包是一种能够方便地分层组织模块的方式。
