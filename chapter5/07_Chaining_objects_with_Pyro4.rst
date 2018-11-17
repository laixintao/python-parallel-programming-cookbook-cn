使用 Pyro4 链接对象
===================

本节将展示如何用 Pyro4 做对象链，通过 Pyro4 可以互相调用。假设我们想创建如下的架构：

.. image:: ../images/objects-chain.png

我们有四个对象，一个 Client 和三个 Server，如图中所示，它们以链式拓扑依赖。客户端将一个请求转发到 ``Server1`` 开始链式调用，然后转发到 ``Server2`` ，然后它调用链式拓扑中的下一个对象 ``Server3`` ，最后 ``Server3`` 调用 ``Server1`` 结束。

通过这个例子，我们可以学到如何管理远程对象，进而组合出更加复杂的分布式系统。

|how|
-----

实现这样一个对象链，我们需要写 5 个 Python 脚本。第一个是客户端代码（ ``client.py`` ），代码内容如下：  ::

   from __future__ import print_function
   import Pyro4
   obj = Pyro4.core.Proxy("PYRONAME:example.chain.A")
   print("Result=%s" % obj.process(["hello"]))
