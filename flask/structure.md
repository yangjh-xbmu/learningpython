# 应用的基本结构

## Hello World

在应用根目录中新建`hello.py`，内容如下：

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'hello'
```

虽然内容不多，但却创建了一个Flask应用实例，在这个实例中，有路由和视图函数。

## 应用实例

所有Flask应用都必须创建一个**应用实例**。Web服务器使用一种名为WSGI（Web server gateway interface)的谢意，把接收到的所有请求转交给这个对象处理。创建应用实例的最简单代码通常为：

```python
from flask import Flask
app = Flask(__name__)
```

其中`flask()`是构造函数，`__name__`参数表示导入模块的名字。

## 路由和视图函数

处理URL和函数之间关系的程序成为**路由**，用来指定特定URL的请求，要求运行哪些代码。在Flask中最简便的定义路由的方式，就是使用app.route装饰器，例如：

```python
@app.route('/')
def index():
    return 'hello'
```

上例中，定义了对根目录（`/`）的访问，都交给index()函数处理，类似index()处理入站请求的函数称为**视图函数**。

### 动态路由

在实际应用中，很多地址中都包含可变部分，Flask要定义动态路由，只需要在app.route装饰器中使用特殊语法，如：

```python
@app.route('/user/<name>')
def user(name):
    return 'hello,{}'.format(name)
```

路由URL中放在尖括号中的内容就是可变的动态部分。

## Web开发服务器

Flask自带Web开发服务器，通过flask run命令启动。如运行之前的hello.py应用，可在虚拟环境中启动Web服务器：

```bash
export FLASK_APP=hello.py
flask run
```

服务器启动后，开始轮询、处理请求。

## 调试模式

Flask的调试模式开启后，开发服务器会自动加载两个工具：重载器和调试器。

```bash
export FLASK_APP=hello.py
export FLASK_DEBUG=1
flask run
```

## 参考资料

1. [Flask Web开发-基于Python的Web应用开发实战](https://www.amazon.cn/dp/B07GRV89VL/ref=sr_1_1?s=books&ie=UTF8&qid=1540221653&sr=1-1&keywords=flask+web%E5%BC%80%E5%8F%91+%E7%AC%AC2%E7%89%88)
