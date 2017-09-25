如何定义一个线程
================

使用线程最简单的一个方法是，用一个目标函数实例化一个Thread然后调用 ``start()`` 方法启动它。Python的threading模块提供了 ``Thread()`` 方法在不同的线程中运行函数或处理过程等。 ::

    class threading.Thread(group=None,
                           target=None,
                           name=None,
                           args=(),
                           kwargs={})	    

上面的代码中：

- ``group``: 一般设置为 ``None`` ，这是为以后的一些特性预留的。
- ``target``: 当线程启动的时候要执行的函数。
- ``name``: 
