# 为 WOX 开发插件

Wox 是一款在 Windows 环境下运行的快速启动程序的工具，支持 C# 和 Python 语言的插件开发。

## 准备工作

1. 在`<WoxDirectory>\Plugins\`中创建`<YourPluginDirectory>`，如`ChineseDict`。
1. 创建`plugin.json`文件，具体内容参见官方文档。
1. 创建 python 文件，注意和 json 配置文件中配对。
1. 为了调试方便，将 `wox.py` 文件复制到自己的插件目录。
1. 安装必要的包，可以全局安装，也可以将包复制到本地目录中。
1. 使用诸如参数`python main.py "{\"method\":\"query\",\"parameters\":[\"hello\"]}"`进行调试。
1. Wox 的日志文件在`AppData\Roaming\Wox\Logs`目录中。在此可以查看 wox 的错误日志，方便调试。

## 参考资料

1. [用 Python 为 WoX 写插件](https://eason-yang.com/2016/06/19/use-python-to-build-a-wox-plugin/)
1. [官方文档中的 python 插件开发](http://doc.wox.one/zh/plugin/python_plugin.html)
