# HTTP库

Python提供了功能齐全的HTTP库，使用这些库，我们只需要关心请求的地址是什么，参数是什么，不用关心更底层的技术，大大降低了信息抓取的难度。最基础的HTTP库有urllib、request等等。

## urllib

Urllib是Python3内置的http库，它包含四个模块：

1. request
2. error
3. parse
4. robotparser

### 发送请求

使用urllib的request模块，可以方便地实现请求的发送，并得到响应。

```python
import urllib.request

rqs = urllib.request.urlopen('http://www.baidu.com')
html = rqs.read()
print(html)
```

`request()`方法返回`HTTPResponse`类型的对象，具有一些处理信息的属性和方法。其中最基本的是`urlopen()`方法，可以完成最基本的请求。它的使用方法如下：

```python
urllib.request.urlopen(url, data=None, [timeout, ]*, cafile=None, capath=None, cadefault=False, context=None)
```

#### data参数

如果要添加`data`参数，则需要使用`byte()`方法构造一个字节流编码格式的内容。使用`data`参数后，请求方式就变成了`POST`方式。

```python
import urllib.request
import urllib.parse

data = bytes(urllib.parse.urlencode({'word':'hello'}),encoding='utf8')
rqs = urllib.request.urlopen('http://httpbin.org/post',data = data)

print(rqs.read())
```

#### timeout参数

timeout参数用于设置超时时间，单位为秒，默认为全局默认时间。

```python
import urllib.request
import urllib.parse
import socket
import urllib.error

data = bytes(urllib.parse.urlencode({'word':'hello'}),encoding='utf8')

try:
    rqs = urllib.request.urlopen('http://httpbin.org/post',data = data,timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason,socket.timeout):
        print('time out')
```

通过设置timeout参数来实现超时处理，是非常有用的策略。

#### Request方法

如果要在请求中加入头信息，就需要使用Request类。

```python
import urllib.request
import urllib.parse
import socket
import urllib.error

url = 'http://httpbin.org/post'
headers = {
    'User-Agent':'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
    'Host':'httpbin.org'
}
dict = {
    'name':'Yang'
}

data = bytes(urllib.parse.urlencode(dict),encoding='utf8')
req = urllib.request.Request(url=url,data = data,headers=headers)

try:
   response = urllib.request.urlopen(req,timeout=3)
except urllib.error.URLError as e:
    if isinstance(e.reason,socket.timeout):
        print('time out')

print(response.read())
```

依然用urlopen()方法来发送这个请求，只不过参数不是url，而是Request类型的对象。Request对象的参数如下：

```python
class urllib.request.Request(url, data=None, headers={}, origin_req_host=None, unverifiable=False, method=None)
```

1. url是必选参数
1. data必须是字节流类型。
1. headers是一个字典
1. origin_req_host是请求方的host名称或者ip地址
1. unverfiable表示请求是否无法验证（如读取图像的权限）
1. method的值为GET、POST、PUT等等。

### 处理异常

urllib的error模块定义了由request模块阐释的异常。如果出现了问题，request模块便会抛出error模块定义的异常。

#### URLError

URLError类继承自OSError，由request模块产生的异常都可以通过这个类捕获。它具有一个属性reason，即返回错误的原因。例如，我们访问一个不存在的页面：

```python
from urllib import request,error

try:
    response = request.urlopen('http://yangzh.cn/php.html')
except error.URLError as e:
    print(e.reason)
```

运行结果为`Not Found`。程序没有直接报错，而是输出上述内容，这样我们就具备了处理意外的能力，使得程序更加健壮。

#### HTTPError

HTTPError是URLError的子类，所以可以先捕获HTTPError，然后再捕获URLError，如果正常，则用else来处理，这是一种更加稳妥的异常处理方式。例如：

```python
from urllib import request,error

try:
    response = request.urlopen('http://yangzh.cn/php.html')
except error.HTTPError as e:
    print(e.reason,e.code,e.headers,sep='\n')
except error.URLError as e:
    print(e.reason)
else:
    print('请求成功')
```

HTTPError有3个属性：

1. code为HTTP状态码。
1. reason为错误原因，其值可能是字符串，也可能是对象。
1. headers为响应头信息。

### 解析链接

urllib中的parse模块，可以实现URL的抽取、合并以及链接转换，在数据抓取中使用频率很高。

#### urlparse()

`urlparse()`可以实现URL的识别和分段，例如：

```python
from urllib.parse import urlparse

url = 'https://cn.bing.com/search.php?q=python#id-1'
result = urlparse(url)
print(type(result),result,sep='\n')
```

运行结果如下：

```python
<class 'urllib.parse.ParseResult'>
ParseResult(scheme='https', netloc='cn.bing.com', path='/search.php', params='', query='q=python', fragment='id-1')
```

从结果可以看出，该方法将URL分解为六个部分：

1. scheme表示协议
1. netloc表示域名、主机
1. path表示主机中的路径
1. params表示参数
1. query表示查询条件，GET方式提交请求会产生此类信息
1. fragment表示地址片段，指向页面内部锚点

#### urlencode()

urlencode()用于构造GET请求，如：

```python
from urllib.parse import urlparse,urlencode

params ={
    'name':'yangzh',
    'age':'21'
}

base_url = 'http://www.yangzh.cn?'
url = base_url + urlencode(params)

print(url)
```

结果输出为`http://www.yangzh.cn?name=yangzh&age=21`。

#### parse_qs()

该函数可以将GET请求参数转化为字典，例如：

```python
from urllib.parse import urlparse,urlencode,parse_qs

params ={
    'name':'yangzh',
    'age':'21'
}

base_url = 'http://www.yangzh.cn?'
url = base_url + urlencode(params)

result = urlparse(url)

print(url)
print(result.query,parse_qs(result.query),sep='\n')
```

将打印出：

```bash
http://www.yangzh.cn?name=yangzh&age=21
name=yangzh&age=21
{'name': ['yangzh'], 'age': ['21']}
```

#### URL编码

`quote()`方法可以将特殊内容（如空格、中文等）转化为URL编码的格式，`unquote()`方法可以对URL编码进行解码。

## 使用requests

与urllib库相比，requests库要更为简洁和人性化，功能也更为丰富。

### 安装requests

使用pip工具，可以非常简单地实现requests库的安装：

```bash
pip install requests
```

## 参考资料

1. [https://docs.python.org/3/library/urllib.html](https://docs.python.org/3/library/urllib.html)
1. [http://cn.python-requests.org/zh_CN/latest/](http://cn.python-requests.org/zh_CN/latest/)
