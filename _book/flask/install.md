# 安装Flask

首先得具有一台安装了Python的计算机，并能使用命令行工具。

## 创建应用目录

```bash
mkdir flasky
cd flasky
```

## 创建虚拟环境

```bash
python3 -m venv venv
```

使用python3内置命令venv创建一个名为venv的虚拟环境，在这个虚拟环境中所作的一些设置，不会改变全局的Python设置。

## 使用虚拟环境

```bash
source venv/bin/activate
```

激活虚拟环境，虚拟环境的命令提示符，都会加入环境名，以示区别，如`(venv）`。使用`deactivate`命令将会退出虚拟环境。

## 使用pip安装Python包

```bash
pip install flask
```

将会使用pip工具，安装flask相关依赖包及flask。安装完毕后，执行如下命令，如无错误信息，flask安装成功：

```bash
python
>>> import flask
>>>
```
