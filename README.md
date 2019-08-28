# 简介

在这本电子书（在线阅读地址为：[http://yangjh.gitee.io/learningpython/](http://yangjh.gitee.io/learningpython/)) 中，我们将学习 Python 的基础知识，最终达到抓取网络数据、分析数据的目的。

> Life is short, you need Python。Bruce Eckel

## Python 发展历史

Python 的创始人为 Guido van Rossum。1989 年圣诞节期间，在阿姆斯特丹，Guido 为了打发圣诞节的无趣，决心开发一个新的脚本解释程序，做为 ABC 语言的一种继承。之所以选中 Python（大蟒蛇的意思）作为程序的名字，是因为他是一个叫 Monty Python 的喜剧团体的爱好者。ABC 是由 Guido 参加设计的一种教学语言。就 Guido 本人看来，ABC 这种语言非常优美和强大，是专门为非专业程序员设计的。但是 ABC 语言并没有成功，究其原因，Guido 认为是非开放造成的。Guido 决心在 Python 中避免这一错误。同时，他还想实现在 ABC 中闪现过但未曾实现的东西。

截至目前，Python 的版本为 3.7.4，2019 年 7 月 8 日发布。

## Python 特点

1. 简单 Python 是一种代表简单主义思想的语言。阅读一个良好的 Python 程序就感觉像是在读英语一样。它使你能够专注于解决问题而不是去搞明白语言本身。
2. 易学 Python 很容易上手，一方面是由于 Python 有完善的说明文档，另一方面网络中有大量的教程，学习资源可谓丰富。本书的写作就参考了诸多网络教程。\cite{pythonguru，2015}
3. 开源 开源意味着人们可以自由地发布这个软件的拷贝、阅读它的源代码、对它做改动、把它的一部分用于新的自由软件中。Python 有非常活跃的开源社区，来自世界各地的程序员不断完善着 Python，如今 Python 拥有功能强大且门类齐全的扩展库。它可以帮助处理各种工作，包括正则表达式、文档生成、单元测试、线程、数据库、网页浏览器、CGI、FTP、电子邮件、XML、XML-RPC、HTML、WAV 文件、密码系统、GUI（图形用户界面）、Tk 和其他与系统有关的操作。Python 语言及其众多的扩展库所构成的开发环境十分适合工程技术、科研人员处理实验数据、制作图表，甚至开发科学计算应用程序。
4. 解释性 在计算机内部，Python 解释器把源代码转换成称为字节码的中间形式，然后再把它翻译成计算机使用的机器语言并运行。这使得使用 Python 更加简单。也使得 Python 程序更加易于移植。
5. 可移植 Python 已经被移植在许多平台上（经过改动使它能够工作在不同平台上）。这些平台包括 Linux、Windows、FreeBSD、Macintosh、Solaris、OS/2、Amiga、AROS、AS/400、BeOS、OS/390、z/OS、Palm OS、QNX、VMS、Psion、Acom RISC OS、VxWorks、PlayStation、Sharp Zaurus、Windows CE、PocketPC、Symbian 以及 Google 基于 linux 开发的 android 平台。
6. 面向对象 Python 既支持面向过程的编程也支持面向对象的编程。在“面向过程”的语言中，程序是由过程或仅仅是可重用代码的函数构建起来的。在“面向对象”的语言中，程序是由数据和功能组合而成的对象构建起来的。
7. 可扩展 如果需要一段关键代码运行得更快或者希望某些算法不公开，可以部分程序用 C 或 C++编写，然后在 Python 程序中使用它们。
8. 可嵌入 可以把 Python 嵌入 C/C++程序，从而向程序用户提供脚本功能。

## 使用 Python 的知名项目

以下是使用 Python 作为主力开发语言的知名项目，其中有一些是用 python 进行开发，有一些在部分业务或功能上使用到了 python，还有的是支持 python 作为扩展脚本语言。

1. Reddit 社交分享网站，最早用 Lisp 开发，在 2005 年转为 python。
1. Dropbox 文件分享服务。
1. 豆瓣网 图书、唱片、电影等文化产品的资料数据库网站。
1. Django 鼓励快速开发的 Web 应用框架。
1. EVE 网络游戏 EVE 大量使用 Python 进行开发。
1. Fabric 用于管理成百上千台 Linux 主机的程序库。
1. Blender 以 C 与 Python 开发的开源 3D 绘图软件。
1. BitTorrent bt 下载软件客户端。
1. Ubuntu Software Center Ubuntu 9.10 版本后自带的图形化包管理器。
1. YUM 用于 RPM 兼容的 Linux 系统上的包管理器。
1. Civilization IV 游戏《文明 4》。
1. Battlefield 2 游戏《战地 2》。
1. Google 谷歌在很多项目中用 python 作为网络应用的后端，如 Google Groups、Gmail、Google Maps。
1. NASA 美国宇航局，从 1994 年起把 python 作为主要开发语言。
1. Industrial Light & Magic 工业光魔，乔治·卢卡斯创立的电影特效公司。
1. Yahoo Groups 雅虎推出的群组交流平台。
1. YouTube 视频分享网站，在某些功能上使用到 python。
1. Cinema 4D 一套整合 3D 模型、动画与绘图的高级三维绘图软件，以其高速的运算和强大的渲染插件著称。
1. Autodesk Maya 3D 建模软件，支持 python 作为脚本语言。
1. gedit Linux 平台的文本编辑器。
1. GIMP Linux 平台的图像处理软件。
1. Minecraft: Pi Edition 游戏《Minecraft》的树莓派版本。
1. MySQL Workbench 可视化数据库管理工具。
1. Digg 社交新闻分享网站。
1. Mozilla 为支持和领导开源的 Mozilla 项目而设立的一个非营利组织。
1. Quora 社交问答网站。
1. Path 私密社交应用。
1. Pinterest 图片社交分享网站。
1. SlideShare 幻灯片存储、展示、分享的网站。
1. Yelp 美国商户点评网站。
1. Slide 社交游戏/应用开发公司，被谷歌收购。

## 学习资源

1. [简明 Python 教程](https://bop.molun.net/)
1. [官方文档](https://www.python.org/doc/)
