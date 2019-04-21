PyCSP和通信顺序进程
===================

PyCSP 是基于通信顺序进程的一个 Python 模块。通信顺序进程是通过消息处理建立并发程序的编程范式。PyCSP 模块的特点是:

- 进程之间交换消息
- 线程之间可以共享内存
- 通过 channels 来实现交换消息

Channels 可以做：
- 进程之间传值
- 进程同步

PyCSP 允许多种不同的 channel 类型: One2One, One2Any, Any2One, Any2Any. 这些名字代表多少 readers 和 writers 可以额通过 channel 通讯。

|ready|
-------

(译者注：本文使用的 python-csp 已经发生了比较大的变化， 文中的代码可能已经无法运行）

PyCSP 可以通过 pip 用以下命令安装： ::

   pip install python-csp

Github 也有库的源码: https://github.com/futurecore/python-csp .

下载之后在项目目录执行以下命令来安装： ::

   python setup.py install

在本例子中，我们使用 Python2.7 .

|how|
-----

在第一个例子中，我们会先介绍 PyCSP 中的基本概念，processes 和 channels. 我们将定义两个进程，分别是 counter 和 printer. 下面我们来看如何定义这两个进程之间的通信过程。

参考下面的代码： ::

   # -*- coding: utf-8 -*-
   from pycsp.parallel import *

   @process
   def processCounter(cout, limit):
       for i in xrange(limit):
           cout(i)
       poison(cout)

   @process
   def processPrinter(cin):
       while True:
           print cin(),

   A = Channel('A')

   Parallel(
       processCounter(A.writer(), limit=5),
       processPrinter(A.reader())
   )

   shutdown()

在 Python2.7 中的运行结果如下： ::

   Python 2.7.9 (default, Dec 10 2014, 12:28:03) [MSC v.1500 64 bit (AMD64)] on win32
   Type "copyright", "credits" or "license()" for more information. 
   >>> ========================RESTART ==========================
   >>> 
   0 1 2 3 4

|work|
------

// TODO

|more|
------

CSP是一种用于描述并发进程交互的语言。在数学中被称为代数过程。它在实践中被用作规范和验证各种系统的竞争条件的工具。 CSP启发的编程语言Occam的现在被广泛用作并行编程语言。

   对 CSP 有兴趣的同学，建议阅读霍尔的原著： http://www.usingcsp.com/cspbook.pdf .
