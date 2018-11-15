# 命令行参数模块argparse

Argparse模块主要用来开发类似于shell中原生命令那样用户友好的命令行工具。使用该模块可以定义必需参数、可选参数，还能自动生成帮助和使用说明。

先看一个简单例子：

```python
#! /Users/ncsxbmu/anaconda3/bin/python
# coding=utf-8

import sys
print ("文件名 = ", sys.argv[0])
for i in range(1, len(sys.argv)):
    print ("参数%s = %s"%(i, sys.argv[i]))
```

假设上述代码存放在名为`test.py`的文件中，则上述代码输出结果如下：

```bash
 # 不带参数调用
👉  python test.py
file =  test.py

# 带多个参数调用
👉  python test.py 1 3
file =  test.py
参数1 = 1
参数2 = 3
```

从这个例子中我们可以看出，利用内置模块sys.argv能非常方便地获取参数内容。但这个模块在处理复杂参数时不够简洁和方便。因此，我们需要更加强大的argparse模块，该模块的用法是：

1. 创建解析器
1. 添加参数
1. 解析参数

下面分别讲解：

## 创建解析器

使用`ArgumentParser`类创建参数解析器，参数都为关键字参数。语法为：

```python
class argparse.ArgumentParser(prog=None, usage=None, description=None, epilog=None, parents=[], formatter_class=argparse.HelpFormatter, prefix_chars='-', fromfile_prefix_chars=None, argument_default=None, conflict_handler='error', add_help=True, allow_abbrev=True)
```

其中主要参数说明如下：

1. prog - 程序名称，默认值为程序文件名。
1. usage - 程序用法描述，默认根据添加的参数生成。
1. description - 参数说明信息之前的文本默认为空。
1. epilog - 参数说明信息之后的文本，默认为空。
1. parents - 需要包含的父解析器。
1. add_help - 添加 -h/--help 选项，默认为真。
1. allow_abbrev - 是否允许参数缩写，默认为真。

例如：

```python
#! /Users/ncsxbmu/anaconda3/bin/python
# coding=utf-8

import argparse

parser = argparse.ArgumentParser()
parser = argparse.ArgumentParser(description = '合并多个markdown文件并转化为docx文件')
parser.print_help()
```

运行结果如下：

```bash
 👉  python test.py

usage: test.py [-h]

合并多个markdown文件并转化为docx文件

optional arguments:
  -h, --help  show this help message and exit
```

## 添加参数选项

使用`add_argument`类来添加参数,以及如何解析参数，语法如下：

```python
ArgumentParser.add_argument(name or flags...[, action][, nargs][, const][, default][, type][, choices][, required][, help][, metavar][, dest])
```

### name or flags

name 或者 flags 用来指定参数名称，或者参数列表，其中以`-`开始的参数为可选参数。例如：

```python
import argparse

parser = argparse.ArgumentParser()
parser = argparse.ArgumentParser(description = '合并多个markdown文件并转化为docx文件')
parser.add_argument('echo')
parser.add_argument('-s','--source')

args = parser.parse_args()

print (args.echo)
print (args.source)
```

上述代码增加了1个必需参数`echo`，和1个可选参数`source`，测试结果如下：

```bash
👉  test.py hello -s sun
hello
sun

👉  test.py hello --source sun
hello
sun

 👉  test.py --source sun
usage: test.py [-h] [-s SOURCE] echo
test.py: error: the following arguments are required: echo

 👉  test.py hello
hello
None
```

结果显示，如果缺少必填参数，则会报错，而可选参数即可用短参数形式，也可用长参数形式。

### help

不论是必选参数还是可选参数，强烈建议使用help参数添加说明文字，该说明文字会自动生成在help结果中。

```python
import argparse

parser = argparse.ArgumentParser()
parser = argparse.ArgumentParser(description = '合并多个markdown文件并转化为docx文件')
parser.add_argument('source',help='待转换的文件')
parser.add_argument('-st','--sourcetype',help='转换前的格式')

args = parser.parse_args()

print (args.source)
print (args.sourcetype)
```

当使用-h或者--help输出帮助信息时，结果如下：

```bash
 👉  test.py -h
usage: test.py [-h] [-st SOURCETYPE] source

合并多个markdown文件并转化为docx文件

positional arguments:
  source                待转换的文件

optional arguments:
  -h, --help            show this help message and exit
  -st SOURCETYPE, --sourcetype SOURCETYPE
                        转换前的格式
```

可见，argparse模块已经非常贴心地按照help参数值，生成了帮助信息。

### default和type

default参数用来指定参数默认值，type用来指定参数类型（默认值是string），这两个参数经常一起使用，用来限定参数值。

```python
import argparse

parser = argparse.ArgumentParser()
parser = argparse.ArgumentParser(description = '合并多个markdown文件并转化为docx文件')
parser.add_argument('--source','-s',help='待转换的文件',default='source.md')
parser.add_argument('-st','--sourcetype',help='转换前的格式')
parser.add_argument('-l','--level',help='压缩级别',type=int,default=1)

args = parser.parse_args()

print (args.source)
print (args.sourcetype)
print (args.level)
```

在上述代码中，增加了三个可选参数，并设定了默认值和类型，结果输出如下：

```bash
 👉  test.py
source.md
None
1

 👉  test.py -l 3
source.md
None
3
```

可以看到，指定的默认值都起了作用。

## 参数解析

只有使用`parse_args()`方法对添加的参数进行解析后，才能在命令行中使用参数，用法很简单，已在前面的代码中多次出现。

## 小结

agrparse模块的功能还有很多，这里只是介绍了入门的用法，还有很多细节没有提到，详细信息请查看官方文档。

## 参考文献

1. [argparse模块官方手册](https://docs.python.org/3/library/argparse.html)
1. [argparse用法总结](https://www.jianshu.com/p/fef2d215b91d)

