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

模板中的双花括弧中，放入的就是动态变量，在jinja中，变量除了上述案例中简单的形式外，还可以是Python中的列表、字典和对象。

变量的值，还可以使用过滤器修改。过滤器添加在变量名之后，二者之间以竖线分割。Jinja2中常用的过滤有：

|  过滤器名  |       作用       |
| ---------- | ---------------- |
| safe       | 渲染时不转义     |
| capitalize | 首字母大写       |
| lower      | 小写             |
| upper      | 大写             |
| title      | 每个首字母大写   |
| trim       | 删除收尾空白字符 |
| striptags  | 删除HTML标签     |
  
## 参考资料

1. [Jinja2中文手册](http://docs.jinkan.org/docs/jinja2/)

### 控制结构

Jinja2 提供了灵活的多种控制结构，用来改变模板的渲染流程。

### 分支

```html
{% if user %}
    hello,{{ user }}!
{% esle %}
    hello,Stranger!
{% endif %}
```

### 循环

```html
<ul>
    {% for comment in comments %}
        <li>{{ comment }}</li>
    {% endfor %}
</ul>
```
