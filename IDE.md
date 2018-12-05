# Python开发环境搭建

Python支持多个平台，其中在Mac、类UNIX平台中已默认安装，Windows平台中的安装也非常简单，从官方网站下载安装包安装即可，注意安装时将Python所在目录添加到系统路径中即可。

## 在MacOS 中安装Python 3

在目前的MacOs中，内置的Python版本为2.7。如果要安装Python3，步骤如下：

### 安装Xcode

在终端中运行如下命令：

```bash
xcode-select --install
```

### 安装Homebrew

在终端中运行如下命令：

```bash
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

Homebrew安装完后，使用vim或者其他编辑器将如下内容添加到`~/.profile`文件中。

```bash
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

## 使用python虚拟环境

### 为什么要用虚拟环境

虽然使用python3这样的工具，能够使用python3解释器，但在开发人员需要在不同的版本中安装扩展包时，或者在需要使用不同版本的某个解释器、扩展包时，如果只使用系统唯一的开发环境，就显得捉襟见肘。

### 虚拟环境的创建与使用

因此，python提供了创建虚拟环境的工具venv，例如：

```bash
python3.7 -m venv python37
```

上面的命令将在当前目录中创建名为`python37`的目录，进入该目录后，运行：

```bash
source bin/activate
```

就会激活该虚拟环境，命令后会出现`(python37)`这样的提示符。

在该目录中运行`deactivate`则会退出虚拟环境。

### 虚拟环境与系统环境的区别

使用venv命令创建的虚拟环境是一个独立于系统python目录的轻量级python目录，虚拟环境目录和系统python目录之间共享的是python标准库，而每个虚拟目录各自拥有独立的python扩展以及各自的pip包管理，如果系统有多个版本的python主库，也可以基于其自身创建不同版本的python虚拟环境。

在一个虚拟环境中，只能有一个版本的python。而在系统环境中，可以由多个版本的pyhton

## 编辑器

虽然Python自带编辑器，但其不够方便，推荐使用轻量级的编辑器Sublime Text或者Visual Studio Code。使用编辑器将文件保存成`.py`后缀，然后通过命令行调用即可执行。

如在编辑器中键入如下内容：

```python
print("hello world")
```

保存为`hello.py`（文件名最好不要与Python的各种函数、库名相同），注意设置文件编码方式为`UTF-8`。

启动终端，进入到脚本所在路径，执行：

```bash
python hello.py
```

即可看到运行结果。

### Visual Studio Code 中的必要设置

使用VS Code作为Python开发编辑器，最好进行如下操作：

1. 安装Python扩展。
1. 安装语法提示插件。
1. 选择解释器。当 VSCode 遇到 Python 虚拟环境的时候时常会无法找到正确的 Python 解释器和虚拟环境，导致调试无法进行，在工作目录中设置 Python 的解释器，这样可以避免项目之间发生版本冲突。正确设置`python.pythonPath`即可。
