# 使用Selenium抓取动态渲染页面

有些网站的内容是由浏览器经过JavaScript渲染后生成，直接抓取其内容时，只能得到js代码，在这种情况下，我们可以使用模拟浏览器运行的库，如Selenium先渲染页面，这样就可以抓取渲染后的页面内容了。

## 安装

首先需要安装chrome浏览器和chromedriver，例如在Mac中：

```bash
brew cask install google-chrome
brew cask install chromedriver
```

上面的操作，如果出现超时，就需要设置代理，建议使用ShadowsocksX-NG。启动ShadowsocksX-NG之后，点击“Copy HTTP proxy shell export line”命令，将可在终端中粘贴如下内容：

```bash
export http_proxy=http://127.0.0.1:1087;export https_proxy=http://127.0.0.1:1087;
```

也可将上述内容加入到`~/.bash_profile`文件，一劳永逸地解决终端代理问题。

接着，安装Selenium，在合适的python虚拟环境中，执行：

```bash
pip3 install selenium
```

## Selenium的使用

### 初始化浏览器对象

除Chorome浏览器外，Selenium还支持主要浏览器厂商的产品，如Firefox、Edge、Safari。

初始化代码如下：

```python
from selenium import webdriver
browser = webdriver.Chrome()
```

这样我们就得到了Chrome浏览器对象。还可以在初始化时传入参数，比如无界面模式：

```python
chrome_options = web

### 访问页面

使用`get()`方法，传入必要参数，就可访问页面，如：

```python
from selenium import webdriver
browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
print(broswer.page_source)
brower.close
```

### 查找节点

为了在浏览器中完成操作，需要获取页面中的特定节点，如填充搜索框、模拟点击等等。

#### 单个节点

Selenium提供了获取多个单个节点方法`find_element_XX()`，其中查找方式可以为：

|             查找方式              |            说明            |
| --------------------------------- | -------------------------- |
| find_element_by_id                | 按照节点id获取             |
| find_element_by_name              | 按照节点name获取           |
| find_element_by_xpath             | 按照Xpath规则获取          |
| find_element_by_link_text         | 按照链接文本内容获取       |
| find_element_by_partial_link_text | 按照链接文本的部分内容获取 |
| find_element_by_tag_name          | 按照标签名称获取           |
| find_element_by_class_name        | 按照类名获取               |
| find_element_by_css_selector      | 按照CSS选择器获取          |

#### 多个节点

如果要得到多个节点，需要使用`find_elements()`这样的方法，用法和获取单个节点的方式类似。

### 节点操作

获取节点后，可以进行模拟输入、点击等操作，常见操作有：

|    方法     |    说明    |
| ----------- | ---------- |
| send_keys() | 输入文字   |
| clear()     | 清空输入框 |
| click()     | 点击       |

### 执行JavaScript

可以利用`execute_script()`方法运行JavaScript指令，从而实现更多更精细的操作，如滚动浏览器、选择特殊节点等等。

### 获取节点信息

经过对节点的选择和操作后，最终目的是获取节点的信息，如文本内容、地址信息等等。

#### 获取属性

用`get_attribute()`方法，可以获取选中节点的属性。

#### 获取文本

直接使用`text`属性，可以调用节点内部的文本信息。

### 延时等待

在Selenium中，`get()`方法会在网页框架加载结束后执行，如果某些页面有额外的Ajax请求，我们在网页源代码中也不一定能成功获取信息，故我们需要延时等待一段时间。
