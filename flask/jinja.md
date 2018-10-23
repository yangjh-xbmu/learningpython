# 模板

通过模板，将**业务逻辑**和**表现逻辑**进行分离，使用模板来处理表现逻辑，视图函数用来处理业务逻辑，这样做的目的在于提高应用的可维护性。

模板是包含响应文本的文件，其中包含用占位变量表示的动态部分，其具体值只在请求的上下文中才能知道。使用真实值替换变量，再返回最终得到的响应字符串，这一过程叫作**渲染**。

Flask使用Jinja2的模板引擎渲染模板。

## Jinja2模板引擎

Jinja2 是一个现代的，设计者友好的，仿照 Django 模板的 Python 模板语言。（选择 Jinja 作为名字是因为 Jinja 是日本寺庙的名称，并且 temple 和 template 的发音类似。）

### 渲染模板

默认情况下，Flask在应用目录的`template`子目录中寻找模板。`render_template()`函数把Jinja2模板引擎集成到了应用中。这个函数的第一个参数是模板的文件名，随后的参数都是键值对，表示模板中变量对应的具体值。

`render_template()`函数在使用前，需要导入。 例如：

```python
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return 'hello'


@app.route('/user/<name>')
def user(name):
    return 'hello,{}'.format(name)


@app.route('/temp/<name>')
def user_t(name):
    return render_template('user.html', name=name)
```

在上例中，`user.html`文件，默认存放在`templates`目录中。其内容可以为：

```html
<!DOCTYPE html>
<html lang="zh">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>

<body>
    <h1>Hello,{{ name }}!</h1>
</body>

</html>
```

### 模板中的变量

模板中的双花括弧中，放入的就是动态变量。在jinja中，变量除了上述案例中简单的形式外，还可以是Python中的列表、字典和对象。

变量的值，还可以使用过滤器修改。过滤器添加在变量名之后，二者之间以竖线分割。Jinja2中常用的过滤有：

|  过滤器名 |       作用       |
| ---------- | ---------------- |
| safe       | 渲染时不转义     |
| capitalize | 首字母大写       |
| lower      | 小写             |
| upper      | 大写             |
| title      | 每个首字母大写   |
| trim       | 删除收尾空白字符 |
| striptags  | 删除HTML标签     |

### 控制结构

Jinja2 提供了灵活的多种控制结构，用来改变模板的渲染流程。

### 分支

```django
{% if user %}
    hello,{{ user }}!
{% esle %}
    hello,Stranger!
{% endif %}
```

### 循环

```django
<ul>
    {% for comment in comments %}
        <li>{{ comment }}</li>
    {% endfor %}
</ul>
```

### 宏

Jinja2中的宏类似Python中的函数。例如定义宏：

```django
{% macro render_comment(comment) %}
    <li>{{ comment }}</li>
{% endmacro %}
```

使用宏：

```django
{{render_comment(comment)}}
```

宏还可以单独存放，然后在需要使用的模板中导入：

```django
{% import 'macros.html' as macros %}
{{ macros.render_comment(comment)}}
```

### 引用

需要在多处重复使用的模板代码，可以单独存放，然后在需要使用的地方引入：

```django
{% include 'common.html' %}
```

### 块

除了引入外，Jinja2模板引擎还可以继承。首先，定义可重用的区块（使用`block`和`endblock`指令），比如新建一个名为`base.html`的基础模板：

```django
<html>
    <head>
    {% block head %}
    {% endblock %}
    </head>
    <body>
    {% block body %}
    {% endblock %}
    </body>
</html>
```

基础模板中定义的区块可以在衍生模板中覆盖：

```django
{% extends 'base.html' %}
{% block body %}
<h1>Hello，world!</h1>
{% endblock %}
```

`extends`指令声明该模板继承自哪个基础模板。如果需要在已有内容的块添加新内容，使用`super()`函数。

## Flask-Bootstrap

BootStrap是一个广受欢迎的前端框架，要想在应用中使用BootStrap，有两种办法，一种是按照BootStrap的要求，在模板中进行内容组织。还有一种办法是使用flask的BootStrap扩展。

### 安装Flask-BootStrap扩展

```bash
pip install flask-bootstrap
```

### 扩展初始化

扩展初始化的方式是把应用实例作为参数传给构造函数，例如：

```python
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap(app)
```

### Flask-Bootstrap基础模板中定义的区块

Flask-Bootstrap的基础模板定义了很多区块，都可在衍生模板中使用。

|    区块名    |           说明           |
| ------------ | ------------------------ |
| doc          | 整个HTML文档             |
| html_attribs | html元素的属性           |
| html         | html元素的内容           |
| head         | head元素内容             |
| title        | title元素内容            |
| metas        | 一组meta标签             |
| styles       | css声明                  |
| body_attribs | body标签属性             |
| body         | body元素内容             |
| navbar       | 用户定义的导航条         |
| content      | 用户定义的页面内容       |
| scripts      | 文档底部的JavaScript声明 |

### 基于Flask-Bootstrap基础模板创建模板

```django
{% extends "bootstrap/base.html" %}
```

Flask-Bootstrap基础模板提供了引入所有css和JavaScript文件的网页框架。我们通常还会在这个框架基础上再添加一些必要内容（如导航条、页脚）作为应用的基础模板。

## 自定义错误页面

Flask允许自定义错误页面。常见的错误代码有两个：404、500。使用app.errorhandler装饰器可以为这两个错误提供自定义的处理函数。

```python
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
```

错误处理函数中的模板，我们可以使用Flask-Bootstrap提供的基础模板创建，更进一步，我们可以再在其基础模板上创建具有统一页面布局的模板。例如我们基于Flask-Bootstrap提供的基础模板创建名为`base.html`的模板：

```django
{% extends "bootstrap/base.html" %}

{% block title %}Flasky{% endblock %}

{% block content %}
<div class="container">
    {% block page_content %}{% endblock %}
</div>
{% endblock %}
```

将上述base.html模板保存到templates目录中，基于该目录，我们创建自定义错误信息模板如下：

```django
{% extends "base.html" %}

{% block title %}Flasky - 找不到页面{% endblock %}

{% block page_content %}
<div class="page-header">
    <h1>找不到该页面。</h1>
</div>
{% endblock %}
```

这样，我们就基于flask-bootstrap模板创建了我们自己的可继承衍生模板。

## 链接

Flask提供了url_for()函数，使用它可以创建基于应用信息的动态链接，如：

```python
url_for('index')                #生成应用的根URL，如/
url_for('index',_external=True) #生成应用根URL的绝对地址，如http://localhost:5000/
```

## 静态文件

默认情况下，Flask会在根目录中的static的子目录中寻找静态文件。使用`url_for()`的`static`参数可以指定静态文件,`filename`参数用来指定文件所在位置，如：

```django
{% block head %}
{{ super() }}
<link rel="shortcut icon" href="{{ url_for('static', filename='favicon.ico')}}" type="image/x-icon">
<link rel="icon" href="{{ url_for('static', filename='favicon.ico')}}" type="image/x-icon">
{% endblock %}
```

为了保留基础模版中`head`区域中的原始内容，我们调用了`super()`函数。

## 本地化日期

服务器一般使用协调世界时(UTC, coordinated universal time)，不过客户端需要转换成本地时间，`Moment.js`是一个非常优秀的客户端时间处理库，`Flask-Moment`是一个Flask扩展，集成`Moment.js`到Jinja2模板中。

### 安装Flask-Moment扩展

```bash
pip install flask-moment
```

### 初始化扩展

```python
from flask_moment import Moment
moment = Moment(app)
```

### 在模板中引入Moment.js库

```django
{% block scripts %}
{{ super() }}
{{ moment.include_moment() }}
{{ moment.locale('zh-CN')}}
{% endblock %}
```

### 在衍生模板中使用moment

```django
    <p>本地时间为：{{ moment(current_time).format('LLL') }}</p>
    <p>过去了{{ moment(current_time).fromNow(refresh=True) }}</p>
```

更加详细的用法，参考`moment.js`、`flask-moment`文档。

## 参考资料

1. [Jinja2中文手册](http://docs.jinkan.org/docs/jinja2/)
