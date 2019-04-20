# 《Python Parallel Programming Cookbook》翻译计划

在线阅读：http://python-parallel-programmning-cookbook.readthedocs.io/

Read the doc编译状态: [![Documentation Status](https://readthedocs.org/projects/python-parallel-programmning-cookbook/badge/?version=latest)](http://python-parallel-programmning-cookbook.readthedocs.io/zh_CN/latest/?badge=latest) CircleCI状态: [![CircleCI](https://circleci.com/gh/laixintao/python-parallel-programming-cookbook-cn.svg?style=svg)](https://circleci.com/gh/laixintao/python-parallel-programming-cookbook-cn)

本书结合Python讨论了线程、进程和异步编程三种模型，是Python并行编程不错的参考书籍。

译者平时主要写 Python，职业是 SRE(Devops)。大学期间给 CSDN 兼职翻译了很多文章（有稿费），给 Importnew 和 伯乐在线也翻译了很多文章（没有稿费）。这本书是业余时间翻译的，所以没办法保证完成时间，但是感觉圣诞节之前差不多能完成。

由于时间仓促、经常加班、心情不好、个人专业深度有限，所以文中出现错误在所难免。鼓励读者自己尝试运行书中的代码，如果发现错误、错别字等欢迎提交 PR，Issue 也行。

本书绝大部分尊重原著，译者忍不住会在书中卖弄自己的小聪明宣扬自己的人生观，这些一般都会加特殊的标注。


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

## 需要注意的问题(!)

1. 如果使用了特殊字符可能编译 pdf 或者 epub 的过程中会出错（LaTex比较难搞），比如[这个commit](https://github.com/laixintao/python-parallel-programming-cookbook-cn/commit/6ea2c41ded6020c37756022cec2dc8159bc8666b) 的[这个编译](http://readthedocs.org/projects/python-parallel-programmning-cookbook/builds/7524187/)就有问题。
