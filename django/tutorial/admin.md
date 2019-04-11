# 后台管理

Django 全自动地根据模型创建后台界面。管理界面不是为了网站的访问者，而是为管理者准备的。

## 创建管理员账号

Django 提供了功能全面的后台管理程序，首先我们增加超级管理员：

```bash
python manage.py createsuperuser
```

输入用户名、邮箱、密码等信息后，Django会自动生成管理员账户信息。

## 添加引用到后台管理

打开 `polls/admin.py` 文件，在其中添加需要在后台管理的应用：

```python
from django.contrib import admin

from .models import Question

admin.site.register(Question)
```

## 进入后台管理界面

```bash
python manage.py runserve
```

在浏览器中`http://127.0.0.1:8000/admin/` 。你应该会看见管理员登录界面，输入之前设置的管理员信息后，就可以在后台管理界面中对数据进行操作。
