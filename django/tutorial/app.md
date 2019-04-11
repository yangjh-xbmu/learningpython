# 在 Django 项目中创建 APP

在 Django 框架中，一个**应用** (app) 实现某个专门的功能（如投票、博客），而**项目**（project）可以由多个 app 和配置文件的集合构成，多个 app 组成完整站点的功能。而且，App 还可以在多个 project 中共享。

## 初始化 APP

App 可以在任何 `Python path` 支持的路径中存放，可通过如下命令查看当前 Python 支持的路径：

```python
>>> import sys
>>> sys.path
['', '/pyweb/lib/python3.7/site-packages']
```

为了方便，我们在 `manage.py` 所在的目录中创建 app，这样我们就可以在之后将 app 作为顶级模块导入。进入到项目目录，执行如下操作：

```bash
python manage.py startapp polls
```

执行之后，目录结构如下：

```bash
├── db.sqlite3
├── manage.py
├── mysite
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── polls
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── migrations
    │   └── __init__.py
    ├── models.py
    ├── tests.py
    └── views.py
```

我们可以看到，名为 `polls` 的 app 目录下，也有视图、模型、后台管理等默认文件，方便 app 在其他项目中的重用。

## 将应用添加到项目中

Django 应用是“可插拔”的。你可以在多个项目中使用同一个应用。除此之外，你还可以发布自己的应用，因为它们并不会被绑定到当前安装的 Django 上。

为了在我们的项目中包含应用，我们需要在配置类 `INSTALLED_APPS` 中添加设置。因为 `PollsConfig` 类写在文件 `polls/apps.py` 中，所以它的点式路径是 `'polls.apps.PollsConfig'`。在文件 `mysite/settings.py` 中 `INSTALLED_APPS` 子项添加点式路径后，它看起来像这样：

```python
INSTALLED_APPS = [
    'polls.apps.PollsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

现在你的 Django 项目会包含 `polls` 应用。

## 创建视图

在当前 app 的`views.py`中可以设置视图内容，如：

```python
from django.http import HttpResponse
def index(request):
    return HttpResponse("这是我的第一个 Django 视图")
```

有了视图要输出的内容之后，还需要将一个 URL 映射到这个视图。

## 规划路由

简洁优雅的 URL 规划对于一个高质量 Web 应用来说至关重要，为了设计你的 URL，你需要创建一个称为 `URL configuration`（简称 `URLConf`）的 Python 模块(通常为`urls.py`)，在该模块中设置 URL 模式和处理访问的函数，即用户通过什么地址访问，这个地址使用哪个模块响应。

### 设置应用的路由规则

为了创造路由信息，我们在 `polls` 目录中，创建一个名为 `urls.py` 的文件，并在该文件中输入如下代码：

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

在这段代码中，引入了框架中的 path() 方法，该方法用以设定路由的具体规则。具体到上述代码中，设定的规则为：进入到当前的访问信息，使用 views.index 模块去处理

### path() 函数详解

函数 `path()` 具有四个参数，两个必须参数：`route` 和 `view`，两个可选参数：`kwargs` 和 `name`。

#### route

`route` 是一个匹配 URL 的准则（类似正则表达式）。当 Django 响应一个请求时，它会从 urlpatterns 的第一项开始，按顺序依次匹配列表中的项，直到找到匹配的项。

这些准则不会匹配 GET 和 POST 参数或域名。例如，URLconf 在处理请求 <https://www.example.com/myapp/> 时，它会尝试匹配 `myapp/` 。处理请求 <https://www.example.com/myapp/?page=3> 时，也只会尝试匹配 `myapp/`。

#### view

当 Django 找到了一个匹配的准则，就会调用这个特定的视图函数，并传入一个 HttpRequest 对象作为第一个参数，被“捕获”的参数以关键字参数的形式传入。

#### kwargs

任意个关键字参数可以作为一个字典传递给目标视图函数。

#### name

为你的 URL 取名能使你在 Django 的任意地方唯一地引用它，尤其是在模板中。这个特性允许你只改一个文件就能全局地修改某个 URL 模式。

### 设置项目的路由规则

下一步是要在根 `URLconf` 文件中指定我们创建的 `polls.urls` 模块。在 `mysite/urls.py` 文件的 `urlpatterns` 列表里插入一个 `include()`， 如下：

```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
```

当包括其它 URL 模式时你应该总是使用 `include()` ，`admin.site.urls` 是唯一例外。

函数 `include()` 允许引用其它 `URLconfs`。每当 Django 遇到：`func：~django.urls.include` 时，它会截断与此项匹配的 URL 的部分，并将剩余的字符串发送到 URLconf 以供进一步处理。

使用 `include()` 的理念是使其可以即插即用。因为投票应用有它自己的 URLconf( polls/urls.py )，他们能够被放在 "/polls/" ， "/fun_polls/" ，"/content/polls/"，或者其他任何路径下，这个应用都能够正常工作，这是提高代码重用率的措施之一。

## 预览效果

经过上面的步骤后，已经创建了一个应用的首页视图和路由规则，现在是检验它们的时候了：

```bash
python manage.py runserver
```

用你的浏览器访问 <http://localhost:8000/polls/>，你应该能够看见在`index`视图中定义的内容了。

## 参考文献

1. [编写你的第一个 Djongo 应用](https://docs.djangoproject.com/zh-hans/2.2/intro/tutorial01/)
