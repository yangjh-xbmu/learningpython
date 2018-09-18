# 简介

在这本电子书中，我们将学习Python的基础知识，最终达到抓取网络数据、分析数据的目的。

> Life is short, you need Python。Bruce Eckel

## Python发展历史

Python的创始人为Guido van Rossum。1989年圣诞节期间，在阿姆斯特丹，Guido为了打发圣诞节的无趣，决心开发一个新的脚本解释程序，做为ABC 语言的一种继承。之所以选中Python（大蟒蛇的意思）作为程序的名字，是因为他是一个叫Monty Python的喜剧团体的爱好者。ABC是由Guido参加设计的一种教学语言。就Guido本人看来，ABC 这种语言非常优美和强大，是专门为非专业程序员设计的。但是ABC语言并没有成功，究其原因，Guido 认为是非开放造成的。Guido 决心在 Python 中避免这一错误。同时，他还想实现在 ABC 中闪现过但未曾实现的东西。

截至目前，Python的版本为3.6.2，2017年7月17日发布。

## Python特点

1. 简单 Python是一种代表简单主义思想的语言。阅读一个良好的Python程序就感觉像是在读英语一样。它使你能够专注于解决问题而不是去搞明白语言本身。
2. 易学 Python很容易上手，一方面是由于Python有完善的说明文档，另一方面网络中有大量的教程，学习资源可谓丰富。本书的写作就参考了诸多网络教程。\cite{pythonguru，2015}
3. 开源 开源意味着人们可以自由地发布这个软件的拷贝、阅读它的源代码、对它做改动、把它的一部分用于新的自由软件中。Python有非常活跃的开源社区，来自世界各地的程序员不断完善着Python，如今Python拥有功能强大且门类齐全的扩展库。它可以帮助处理各种工作，包括正则表达式、文档生成、单元测试、线程、数据库、网页浏览器、CGI、FTP、电子邮件、XML、XML-RPC、HTML、WAV文件、密码系统、GUI（图形用户界面）、Tk和其他与系统有关的操作。Python语言及其众多的扩展库所构成的开发环境十分适合工程技术、科研人员处理实验数据、制作图表，甚至开发科学计算应用程序。
4. 解释性 在计算机内部，Python解释器把源代码转换成称为字节码的中间形式，然后再把它翻译成计算机使用的机器语言并运行。这使得使用Python更加简单。也使得Python程序更加易于移植。
5. 可移植 Python已经被移植在许多平台上（经过改动使它能够工作在不同平台上）。这些平台包括Linux、Windows、FreeBSD、Macintosh、Solaris、OS/2、Amiga、AROS、AS/400、BeOS、OS/390、z/OS、Palm OS、QNX、VMS、Psion、Acom RISC OS、VxWorks、PlayStation、Sharp Zaurus、Windows CE、PocketPC、Symbian以及Google基于linux开发的android平台。
6. 面向对象 Python既支持面向过程的编程也支持面向对象的编程。在“面向过程”的语言中，程序是由过程或仅仅是可重用代码的函数构建起来的。在“面向对象”的语言中，程序是由数据和功能组合而成的对象构建起来的。
7. 可扩展 如果需要一段关键代码运行得更快或者希望某些算法不公开，可以部分程序用C或C++编写，然后在Python程序中使用它们。
8. 可嵌入 可以把Python嵌入C/C++程序，从而向程序用户提供脚本功能。

## 使用Python的知名项目

以下是使用Python作为主力开发语言的知名项目，其中有一些是用python进行开发，有一些在部分业务或功能上使用到了python，还有的是支持python作为扩展脚本语言。

1. Reddit 社交分享网站，最早用Lisp开发，在2005年转为python。
1. Dropbox 文件分享服务。
1. 豆瓣网 图书、唱片、电影等文化产品的资料数据库网站。
1. Django 鼓励快速开发的Web应用框架。
1. EVE 网络游戏EVE大量使用Python进行开发。
1. Fabric 用于管理成百上千台Linux主机的程序库。
1. Blender 以C与Python开发的开源3D绘图软件。
1. BitTorrent bt下载软件客户端。
1. Ubuntu Software Center Ubuntu 9.10版本后自带的图形化包管理器。
1. YUM 用于RPM兼容的Linux系统上的包管理器。
1. Civilization IV 游戏《文明4》。
1. Battlefield 2 游戏《战地2》。
1. Google 谷歌在很多项目中用python作为网络应用的后端，如Google Groups、Gmail、Google Maps。
1. NASA 美国宇航局，从1994年起把python作为主要开发语言。
1. Industrial Light \& Magic 工业光魔，乔治·卢卡斯创立的电影特效公司。
1. Yahoo Groups 雅虎推出的群组交流平台。
1. YouTube 视频分享网站，在某些功能上使用到python。
1. Cinema 4D 一套整合3D模型、动画与绘图的高级三维绘图软件，以其高速的运算和强大的渲染插件著称。
1. Autodesk Maya 3D建模软件，支持python作为脚本语言。
1. gedit Linux平台的文本编辑器。
1. GIMP Linux平台的图像处理软件。
1. Minecraft: Pi Edition 游戏《Minecraft》的树莓派版本。
1. MySQL Workbench 可视化数据库管理工具。
1. Digg 社交新闻分享网站。
1. Mozilla 为支持和领导开源的Mozilla项目而设立的一个非营利组织。
1. Quora 社交问答网站。
1. Path 私密社交应用。
1. Pinterest 图片社交分享网站。
1. SlideShare 幻灯片存储、展示、分享的网站。
1. Yelp 美国商户点评网站。
1. Slide 社交游戏/应用开发公司，被谷歌收购。

## 搭建Python开发环境

Python支持多个平台，其中在Mac、类UNIX平台中已默认安装，Windows平台中的安装也非常简单，从官方网站下载安装包安装即可，注意安装时将Python所在目录添加到系统路径中即可。

### 在MacOS 中安装Python 3
在目前的MacOs中，内置的Python版本为2.7。如果要安装Python3，步骤如下：

### 安装Xcode

在终端中运行如下命令：

```bash
xcode-select --install
```

### 安装Homebrew

在终端中运行如下命令：

```bash
$ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

Homebrew安装完后，使用vim或者其他编辑器将如下内容添加到`~/.profile`文件中。

```
export PATH=/usr/local/bin:/usr/local/sbin:$PATH
```

### 安装Python3

在终端中运行如下指令：

```bash
brew install python3
```

### 使用Python3

使用Homebrew安装Python3后，系统就有两个Python环境，如果要使用系统自带的Python2
，则使用如下指令：

```bash
python
```

而如果要使用Python3，则使用如下指令：

```bash
python3
```

### 使用python虚拟环境

虽然使用python3这样的工具，能够使用python3解释器，但还不够方便，尤其是开发人员需要在不同的版本中安装扩展包时。因此，python提供了创建虚拟环境的工具enev，例如：

```bash
python3.7 -m venv python37
```

上面的命令将在当前目录中创建名为`python37`的目录，进入该目录后，运行：

```bash
source bin/activate
```

就会激活该虚拟环境，命令后会出现`(python37) `这样的提示符。

在该目录中运行`deactivate`则会退出虚拟环境。

### 编辑器

虽然Python自带编辑器，但其不够方便，推荐使用轻量级的编辑器Sublime Text。使用编辑器将文件保存成.py后缀，然后通过命令行调用即可执行，也可以在Sublime Text编辑器中使用编译命令（ctrl+b）查看运行结果。

如在编辑器中键入如下内容：

```python
print "hello world"
```

保存为hello.py，注意设置文件编码方式为UTF-8，然后使用ctrl+b即可在编辑器内部查看运行结果。

或者通过命令行进入到脚本所在路径，键入脚本名称也可运行脚本。

## 学习资源

1. [简明Python教程](https://bop.molun.net/)
1. [官方文档](https://www.python.org/doc/)



