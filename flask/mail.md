# 电子邮件

当特定时间发生时，需要通知用户，而常用的方式就是通过电子邮件。

## 安装Flask-Mail

包装了smtplib的Flask-Mail扩展能更好地与Flask集成。使用pip安装：

```bash
pip install flask-mail
```

Flask-Mail使用SMTP协议发送邮件，若不进行配置，则使用localhost的25端口，无需验证身份就可发送邮件。在实际工作中，我们通常是连接到外部SMTP服务器发送电子邮件。

Flask-Mail SMTP服务器的配置信息如下：

|     配置      |  默认值   |              说明              |
| ------------- | --------- | ------------------------------ |
| MAIL-SEVER    | localhost | 电子邮件服务器的主机名或IP地址 |
| MAIL_PORT     | 25        | 电子邮件服务器的端口           |
| MAIL_USE_TLS  | False     | 启用传送层安全协议             |
| MAIL_USE_SSL  | False     | 启用安全套接层协议             |
| MAIL_USERNAME | None      | 邮件账户用户名                 |
| MAIL_PASSWORD | None      | 邮件账户密码                   |

我们使用外部服务器的配置示例如下：

```python
app.config['MAIL_SERVER'] = 'smtp.yeah.net'
app.config['MAIL_USE_SSL'] = 'True'
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
```

为了保护账户信息，脚本应该从环境变量中导入敏感信息，如使用`os.environ.get()`得到系统的环境变量。在Mac中，可以使用如下方式定义环境变量：

```bash
export MAIL_USERNAME="yangjh@yeah.net"
```

## 在应用中集成电子邮件发送功能

我们将发送电子邮件的通用部分定义为函数：

```python
from flask_mail import Message, Mail
mail = Mail(app)
app.config['FLASK_MAIL_SUBJECT_PREFIX'] = '[Flasky]'
app.config['FLASK_MAIL_SENDER'] = 'ADMIN <yangjh@yeah.net>'
def send_email(to, subject, template, **kwargs):
    msg = Message(app.config['FLASK_MAIL_SUBJECT_PREFIX'] + subject,
                  sender=app.config['FLASK_MAIL_SENDER'], recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    mail.send(msg)
```

## 异步发送电子邮件

为了在处理请求过程中避免不必要的延迟，我们可以把发送电子邮件的函数放在后台线程中。

```python
from threading import Thread

def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


def send_email(to, subject, template, **kwargs):
    msg = Message(app.config['FLASK_MAIL_SUBJECT_PREFIX'] + subject,
                  sender=app.config['FLASK_MAIL_SENDER'], recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    return thr
```

在不同的线程中执行`mail.send()`函数时，要使用`app.app_context()`人工创建应用上下文。

## 参考资料

1. [Flask Mail](http://www.pythondoc.com/flask-mail/index.html)
1. [多线程](https://docs.python.org/3.7/library/threading.html)
