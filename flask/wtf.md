# 表单

Flask的Flask-wtf扩展使得开发人员可以非常方便、优雅地处理Web表单，比如生成表单信息、验证表单数据等等。

## 安装和配置

启动虚拟环境，使用pip安装扩展：

```bash
pip install flask-wtf
```

在合适的地方写入配置信息，例如在之前的`hello.py`中写入：

```python
app.config['SECRET_KEY'] = 'GN9rwStf3v1E' # 配置wtf密钥
```

Flask-wtf要求应用配置一个密钥，主要用来防止表单遭到跨站请求伪造攻击(CSRF，cross-site request forgery)。Flask-wtf会根据密钥生成立牌，对会话中的数据进行保护。

## 表单类

使用Flask-wtf，需要将每个表单继承自FlaskForm类。这个类提供了全部HTML表单元素的对象，并且可对字段对象添加验证函数。所谓**验证函数**，就是用于验证用户提交数据是否有效的函数。

FlaskForm基类由Flask-WTF扩展定义，字段和验证函数由WTForms包导入。

例如，在前面的`hello.py`中加入如下内容：

```python
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class NameForm(FlaskForm):
    name = StringField('你的名字', validators=[DataRequired()])
    submit = SubmitField('Submit')
```

NameForm表单中定义了一个name文本字段和一个submit提交按钮。

WTForms支持所有的HTML标准字段（如复选框、文本字段、密码、日期等等），内建了很多验证函数，并且支持自定义验证函数。

## 把表单渲染成HTML

为了降低工作量，我们使用BootStrap预定义的表单样式，可以在模板中这样引入BootStrap，并使用wft.quick_form()函数创建表单。

比如在templates/index.html中，渲染表单：

```django
{% import "bootstrap/wtf.html" as wtf %}
 {{ wtf.quick_form(form) }}
```

## 在视图函数中处理表单

flask中的视图函数，除了指定渲染模板外，还可以接受用户在表单中提交的数据。例如：

```python
@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.date = ''
    return render_template('index.html', current_time=datetime.utcnow(), form=form, name=name)
```

`app.route`装饰器的`methods`参数，用来指定处理何种请求，默认值为`GET`。

如果表单中的数据通过了验证，则`form.validate_on_submit()`返回真值，`render_template()`函数可将多个变量传递到模板中。

## 重定向和用户会话

当应用把POST请求作为最后一个请求时，用户刷新表单，会出现要求用户确定的警告信息，这对于大部分用户而言有些莫名其妙。我们可以使用`Post/redirect/Get`模式，即把Post方式提交的信息，保存在session中，然后使用redirect方式重定向到Get模式，Get模式此时的数据，可从session中读取，这样，就避免了用户刷新表单时的警告信息。

```python
@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', current_time=datetime.utcnow(), form=form, name=session.get('name'))
```

## 闪现消息

当用户提交信息后，需要向用户反馈一些必要的信息，Flask内置的`flash()`函数可实现这个目标。

首先需要在视图函数中定义闪现消息的内容：

```python
@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('看起来你换了名字！')
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', current_time=datetime.utcnow(), form=form, name=session.get('name'))
```

然后再模板中设定闪现消息出现的位置：

```django
{% block content %}
<div class="container">
    {% for message in get_flashed_messages() %}
    <div class="alert alert-warning">
        <button type="button" class="close" data-dismiss="alert">&times;</button>
        {{ message }}
    </div>
    {% endfor %}
    {% block page_content %}{% endblock %}
</div>
{% endblock %}
```

闪现消息只显示一次，关闭后不会再次出现。

## 参考资料

1. [flask-wtf中文文档](http://www.pythondoc.com/flask-wtf/index.html)
1. [WTForms包文档](https://wtforms.readthedocs.io/en/stable/)
