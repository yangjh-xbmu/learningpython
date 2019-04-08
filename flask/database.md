# 数据库

数据库按照一定规则保存应用的数据，应用再发起查询，取回所需的数据。对中小型应用来说，SQL和NoSQL数据库都是很好的选择，而且性能相当。

## Python数据库框架

选择数据库框架时，要考虑很多因素：

1. 易用性
2. 性能
3. 可移植性
4. Flask集成度

基于以上因素，选择数据库Flask-SQLAlchemy。

## 使用Flask-SQLAlchemy管理数据库

Flask-SQLAlchemy是一个Flask扩展，简化了Flask应用中使用SQLAlchemy的操作。SQLAlchemy是一个强大的关系型数据库框架，支持多种数据库后台。

### 安装

可以使用`pip`安装：

```bash
pip install flask-sqlalchemy
```

### 配置

下面展示如何初始化及配置一个简单的SQLite数据库：

```python
import os
from flask_sqlalchemy import SQLAlchemy
basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SECRET_KEY'] = 'GN9rwStf3v1E'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' + \
    os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
```

在Flask-SQLAlchemy中，选择何种数据库，由`SQLALCHEMY_DATABASE_URI`来指定。几种常见的数据库引擎URL格式如下：

|     数据库引擎      |                      URL                      |
| ------------------- | --------------------------------------------- |
| MySQL               | `mysql://username:password@hostname/dabatase` |
| SQLite(Linux,MacOS) | `sqlite:////absolute/path/to/database`        |
| SQLite(windows)     | `sqlite:///C:\\path\\to\\foo.db`              |

SQLAlchemy 暂不支持mongoDB，但可以使用Flask-MongoDB的独立扩展来使用MongoDB数据库。

`SQLALCHEMY_TRACK_MODIFICATIONS`的值设为`False`，可以在不需要追踪对象变化时降低内存消耗。

## 定义模型

**模型**表示应用使用的持久化实体，在ORM中，模型一般是一个类，类的属性对应于数据库表中的列。

Flask-SQLAlchemy创建的数据库实例为模型提供了一个基类以及一系列辅助类和辅助函数，用于定义模型的结构。例如：

```python
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)

    def __repr__(self):
        return '<Role %r>' % self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)

    def __repr__(self):
        return '<User %r>' % self.username
```

类变量`__tablename__`定义在数据库中使用的表名，其余的类变量都是该模型的类型。`db.Column`的其他参数可以指定属性的配置选项。

最常用的SQLAlchemy列选项如下：

|   选项名    |                  说明                  |
| ----------- | -------------------------------------- |
| primary_key | 如果设为True，列为表的主键             |
| unique      | 如果为True，列不允许出现重复的值       |
| index       | 如果为True，为列创建索引，提示查询效率 |
| nullable    | 如果为True，列允许使用空值             |
| default     | 为列定义默认值                         |

虽然没有强制要求，但都定义了`__repr()__`方法，返回一个具有可读性的字符串表示模型，供调试和测试时使用。

## 关系

关系型数据库使用关系把不同表中的行联系起来。使用`relationship()`方法建立模型中的关系：

```python
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role')

    def __repr__(self):
        return '<Role %r>' % self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' % self.username
```

常用的SQLAlchemy关系选项：

|    选项名     |                         说明                         |
| ------------- | ---------------------------------------------------- |
| backref       | 在关系的另一个模型中添加反向引用                     |
| primaryjoin   | 明确指定两个模型之间使用的连接条件                   |
| lazy          | 指定如何加载相关记录                                 |
| uselist       | 如果设为False，不使用列表，而使用标量值              |
| order_by      | 指定关系中记录的排序方式                             |
| secondary     | 指定多对多关系中关联表的名称                         |
| secondaryjoin | SQLAlchemy无法决定时，指定多对多关系中的二级联结条件 |

## 数据库操作

### 创建表

`db.create_all()`函数将寻找所有`db.Model`的子类，然后在数据库中创建对应的表：

```python
db.creat_all()
```

如果数据表已经存在与数据库中，`db.creat_all()`不会重新创建或者更新相应的表。

### 插入行

模型的构造函数接收初始化模型的参数，对数据库的改动通过数据库**会话**管理，会话由`db.session`表示。为了把对象写入数据库，我们要调用commit()方法提交会话。

```python
admin_role = Role(name='Admin')
mod_role = Role(name='Moderator')
user_role = Role(name='User')
user_john = User(username='john', role=admin_role)
user_susan = User(username='susan', role=user_role)
user_david = User(username='david', role=user_role)
db.session.add_all([admin_role, mod_role, user_role,
                    user_john, user_susan, user_david])
db.session.commit()
```

数据库会话能保证数据库的一致性，如果在会话过程中发生了错误，那么整个会话都会失效。

### 修改行

在数据库会话调用`add()`方法就能更新模型。

```python
admin_role.name = 'Administrator'
db.session.add(admin_role)
db.session.commit()
```

### 删除行

数据库会话使用`delete()`方法，能够删除数据，例如：

```python
db.session.delete(mod_role)
db.session.commit()
```

### 查询行

使用`query`对象，可以进行复杂的查询。**过滤器**可以配置query对象进行更精确的数据库查询。例如：

```python
User.query.filter_by(role=user_role).all()
```

常用的SQLAlchemy查询过滤器

|   过滤器    |                    说明                    |
| ----------- | ------------------------------------------ |
| filter()    | 把过滤器添加到原查询上，返回一个新查询     |
| filter_by() | 把等值过滤器添加到原查询上，返回一个新查询 |
| limit()     | 指定返回结果的数量，返回新查询             |
| offset()    | 偏移原查询返回的结果，返回一个新查询       |
| order_by()  | 排序                                       |
| group_by()  | 分组                                       |

多个过滤器可以一起调用，直到获得所需结果。

## 在视图函数中操作数据库

上述的操作，可以在视图函数中进行，例如：

```python
@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            db.session.commit()
            session['known'] = False
        else:
            session['known'] = True
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', current_time=datetime.utcnow(), form=form, name=session.get('name'), known=session.get('known', False))
```

上述代码中新增了变量`known`，这个变量被传给模板，可用于显示自定义的欢迎消息。对应在`index.html`模板中：

```html
{% extends "base.html" %}
{% import "bootstrap/wtf.html" as wtf %}
{% block title %}Flasky - 首页{% endblock %}

{% block page_content %}
<div class="page-header">
    <h1>Hello，{% if name %}{{ name }} {% else %}Stranger{% endif %}!</h1>
    {% if not known %}
    <p>欢迎你，新同学</p>
    {% else %}
    <p>欢迎回来！</p>
    {% endif %}
    {{ wtf.quick_form(form) }}
    <p>本地时间为：{{ moment(current_time).format('LLL') }}</p>
    <p>过去了{{ moment(current_time).fromNow(refresh=True) }}</p>
</div>
{% endblock %}
```

## 参考资料

1. [Flask-SQLAlchemy文档](http://www.pythondoc.com/flask-sqlalchemy/)
1. [SQLAlchemy文档](https://docs.sqlalchemy.org/en/latest/)
