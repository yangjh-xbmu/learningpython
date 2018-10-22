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

所有Flask应用都必须创建一个应用实例。Web服务器使用一种名为WSGI（Web server gateway interface)的谢意，把接收到的所有请求转交给这个对象处理。创建应用实例的最简单代码通常为：

```python
from flask import Flask
app = Flask(__name__)
```

其中`flask()`是构造函数，`__name__`参数表示导入模块的名字。

## 路由和视图函数

处理URL和函数之间关系的程序成为路由，用来指定特定URL的请求，要求运行哪些代码。

### 动态路由
