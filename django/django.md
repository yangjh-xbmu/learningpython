# Django 框架

Django 框架是一个全功能的 Web 开发框架，虽然微型框架能够让你快速上手，但在后期的扩展上，需要将多个插件拼装起来，对初学者的代码组织能力和学习能力，提出了实质性的考验。Django 框架是直接面向企业级开发的工具，无论是从功能的完备性和生态发展来看，Django 框架都是十分成熟的框架，拥有完善的周边生态，虽然需要初学者投入更多的时间成本学习，但一旦掌握，则可大大提高开发效率。

## 安装

### 安装 Django

安装 Django 框架之前，需要已经安装好 Python 及开发工具。需要提醒的是 Django 的版本不同，对 Python 的版本依赖也不同。在合适的地方执行如下操作：

```bash
python3 -m venv pyweb # 在当前目录下创建 pyweb 目录，再在其中创建 Python3 的虚拟环境。
cd pyweb
source bin/activate
pip install django    # 安装 Django 最新版本
```

上面的命令将会在当前目录中新建 `pyweb`目录，并在其中安装 Python3 和 Django。

### 验证安装

使用如下命令测试是否安装成功：

```bash
python -m django --version
```

如果能正确输出 Django 的版本号，则表示安装无误。

### 创建项目并预览效果

```bash
django-admin startproject mysite
cd mysite
python manage.py runserver
```

使用`django-admin startproject`自动创建目录，并生成必要代码。此时的目录结构如下：

```bash
├── db.sqlite3
├── manage.py
├── mysite
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
```

可以看到，自动创建的文件并不多。之后进入项目目录，使用`python manage.py runserver`指令启动内置的用于开发的服务器，现在可以通过浏览器访问<http://127.0.0.1:8000/>，将会看到`Django`的默认欢迎界面。

## 学习资源

1. 胡阳. Django 企业开发实战--高效 Python Web 框架指南[M]. 第 1 版. 北京：人民邮电出版社，2019.
1. [Django 快速安装指南](https://docs.djangoproject.com/zh-hans/2.2/intro/install/)
