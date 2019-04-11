# 创建视图

Django 中的视图的概念是「一类具有相同功能和模板的网页的集合」。在 Django 中，网页和其他内容都是从视图派生而来。每一个视图表现为一个简单的 Python 函数（或者说方法，如果是在基于类的视图里的话）。Django 将会根据用户请求的 URL 来选择使用哪个视图（更准确的说，是根据 URL 中域名之后的部分）。

为了将 URL 和视图关联起来，Django 使用了 'URLconfs' 来配置。URLconf 将 URL 模式映射到视图。

## 添加多个视图

现在再创建几个显示投票信息的页面，在 polls/views.py 中添加如下代码：

```python
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("这是我的第一个视图。")

def detail(request, question_id):
    return HttpResponse("你正在查看第 %s 个问题" % question_id)

def results(request, question_id):
    response = "你正在查看第 %s 个问题的选项"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("你正在填写第 %s 个问题的选项" % question_id)
```

每个视图必须要做的只有两件事：返回一个包含被请求页面内容的 HttpResponse 对象，或者抛出一个异常，比如 Http404 。至于你还想干些什么，随便你。

### 添加路由信息

为了显示上述视图，需要添加路由信息，方可访问。在 polls.urls 模块中，添加如下代码：

```python
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
```

当某人请求你网站的某一页面时——比如说， "/polls/34/" ，Django 将会载入 mysite.urls 模块，因为这在配置项 ROOT_URLCONF 中设置了。然后 Django 寻找名为 urlpatterns 变量并且按序匹配正则表达式。在找到匹配项 'polls/'，它切掉了匹配的文本（"polls/"），将剩余文本——"34/"，发送至 'polls.urls' URLconf 做进一步处理。在这里剩余文本匹配了 '<int:question_id>/'，使得我们 Django 以如下形式调用 detail():

```python
detail(request=<HttpRequest object>, question_id=34)
```

## 模版命名空间

为什么要用模板？如果把页面的设计写死在视图函数的代码里，当想改变页面的样式是，就需要编辑 Python 代码。可使用 Django 的模板系统，只要创建一个视图，就可以将页面的设计从代码中分离出来。这样在逻辑上更加清晰，有利于项目的维护。

首先，在 polls 目录里创建一个 templates 目录。Django 将会在这个目录里查找模板文件。在你刚刚创建的 templates 目录里，再创建一个目录 polls，然后在其中新建一个文件 index.html 。换句话说，你的模板文件的路径应该是 polls/templates/polls/index.html 。因为 Django 会寻找到对应的 app_directories ，所以你只需要使用 polls/index.html 就可以引用到这一模板了。

虽然我们现在可以将模板文件直接放在 polls/templates 文件夹中（而不是再建立一个 polls 子文件夹），但是这样做不太好。Django 将会选择第一个匹配的模板文件，如果你有一个模板文件正好和**另一个应用中的某个模板文件重名**，Django 没有办法区分它们。我们需要帮助 Django 选择正确的模板，最简单的方法就是把他们放入各自的**命名空间**中，也就是把这些模板放入一个**和自身应用重名的子文件夹**里。

## 在视图中使用模板

在视图`polls/view.py`中，载入模板、填充上下文，再返回由它生成的`HTTPResponse`对象，这就是在视图中使用模板的常用流程，Django 为此提供了一个快捷函数：`render()`

```python
from django.http import HttpResponse
from django.template import loader

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request,'polls/index.html',context)
```

## URL命名空间

在一个真实的 Django 项目中，可能会有五个，十个，二十个，甚至更多应用。Django 如何分辨重名的 URL 呢？举个例子，polls 应用有 detail 视图，可能另一个博客应用也有同名的视图。Django 如何知道 `{% url %}` 标签到底对应哪一个应用的 URL 呢？

答案是：在根 URLconf 中添加命名空间。在 `polls/urls.py` 文件中稍作修改，加上 `app_name` 设置命名空间：

```python
app_name = 'polls'
```

对应的，在模板文件中，将原来的URL编码：

```python
<li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
```

修改为：

```python
<li><a href="{% url 'polls:detail' question.id %}">{{ question.question_text }}</a></li>
```

这样做的好处是，当你想改变投票详情视图的 URL，比如想改成 `polls/specifics/12/` ，你不用在模板里修改任何东西（包括其它模板），只要在 `polls/urls.py` 里稍微修改即可，实现了模板和路由的部分解耦。

## 参考资料

1. <https://docs.djangoproject.com/zh-hans/2.2/intro/tutorial03/>
