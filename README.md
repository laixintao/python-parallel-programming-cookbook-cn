# 《Python Parallel Programming Cookbok》翻译计划

在线阅读：http://python-parallel-programmning-cookbook.readthedocs.io/ [![Documentation Status](https://readthedocs.org/projects/python-parallel-programmning-cookbook/badge/?version=latest)](http://python-parallel-programmning-cookbook.readthedocs.io/zh_CN/latest/?badge=latest)

本书结合Python讨论了线程、进程和异步编程三种模型，是Pyhton并行编程不错的参考书籍。

目前进度： 40%

## 如何参与翻译？

Fork本仓库，翻译一小部分内容即可（例如标题），然后向本仓库提交一个PR保持打开状态，之后的翻译工作就可以直接push到这个PR。PR的名字最好是章节号码和标题。

*翻译资源* ：原书是仓库中的 ./book.pdf 。原书图片抽取到了 ./images。但是原书的图表没办法抽取，请自己截图。

注意：

- 翻译之前请先看一下打开的PR，避免多个人翻译了同一部分内容
- 建议一次PR即为一个小节的内容，方便Review
- 内容使用rst和sphinx组织，如果你不会rst，可以使用Markdown格式或者纯文本，我合并的时候会处理格式

**你可以不必关心本书的目录以及内容格式问题，将精力放在翻译内容上，其他的部分我会处理**


## 如何编译本书

1. 安装requirements.txt
2. `make html`

如果内容有误，编译过程中将会以红色提示。
