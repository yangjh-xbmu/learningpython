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
