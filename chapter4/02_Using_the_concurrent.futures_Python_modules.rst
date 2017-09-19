使用Python的 ``concurrent.futures`` 模块
========================================

Python3.2带来了 ``concurrent.future`` 模块，这个模块具有线程池和进程池、管理并行编程任务、处理非确定性的执行流程、进程/线程同步等功能。

此模块由以下部分组成：

- ``concurrent.futures.Executor``: 这是一个虚拟基类，提供了一步执行的方法。
