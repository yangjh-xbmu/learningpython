# Pyquery

Pyquery是一个使用jQuery方式进行高效解析的库。与使用正则表达式相比，借助于诸如pyquery之类的解析库，开发人员可以写出可读性更强的网页解析代码。

## 安装

```bash
pip3 install pyquery
```

## 初始化

所谓初始化，就是引入pyquery库，获取解析文本。例如：

```python
from pyquery import PyQuery as pq
import requests

html = requests.get('http://www.yangzh.cn').text
doc = pq(html)
print(doc('title').text())
```

上面的代码使用requests库获得网页内容，再使用pyquery库进行解析，获取网页标题元素的内容。

## 获取信息

使用pyquery获取网页信息的方式和jQuery是一致的，先通过选择符进行对象的选择，再对选择的对象进行操作。

### 通过选择符选定元素

```python
titles = doc('ul.kanban-List li h3').items()
times = doc('ul.kanban-List li p span.redTxt').items()
locations = doc('ul.kanban-List li b.localIcon').parent().items()
```

### 通过迭代获取最终结果

使用`text()`方法，可以获取元素的内容，当然，还可以使用`attr()`获取指定属性的值。利用zip函数，可以对多个迭代器进行遍历：

```python
def merge_info():
    for title, time, location in zip(titles, times, locations):
        # print(title.text(), time.text(), location.text())
        if '江安' in location.text():
            yield {
                'title': title.text(),
                'time': time.text(),
                'location': location.text()
            }
```

## 参考资料

1. [https://pyquery.readthedocs.io/en/latest/](https://pyquery.readthedocs.io/en/latest/)
1. [https://jquery.com/](https://jquery.com/)
