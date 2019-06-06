# 模板

## 如何在模板中使用静态文件？

1. 在`settings.py`中

## 模板中的数据从何而来？

### 通过视图传递

在视图中定义方法，在其中获取数据，然后通过`render()`函数传递。

```python
def index(request):
    entries = models.Entry.objects.all()
    page = request.GET.get('page', 1)
    entry_list, paginator = make_paginator(entries, page)
    page_data = pagination_data(paginator, page)

    return render(request, 'blog/index.html', locals())
```

如上例中，就将变量：`entries、page、entry_list,pageinator,page_data`，通过`locals()`函数，传递到视图`blog/index.html`中。

在模板文件中使用模板提供的语法标签，就可以使用传递过来的数据了。例如：

```html
{% if entry.abstract %}
  <p>{{ entry.abstract }}</p>
{% else %}
```

### 通过自定义标签获取

1. 在应用中创建`templatetags`包。
1. 在此包中新建Python文件。
1. 在Python文件中：
    ```python
    from django import template
    from ..models import Category, Tag, Entry

    register = template.Library()


    @register.simple_tag
    def get_recent_entries(num=5):
        return Entry.objects.all().order_by('-created_time')[:num]
    ```
1. 在模板文件中引入自定义标签之后，就可以通过自定义标签获取数据了：
    ```html
    {% load blog_tags %}
        {% get_recent_entries as recent_entry_lists %}
            {% for entry in recent_entry_lists %}
                do something
            {% endfor %}
        </dl>
    ```
