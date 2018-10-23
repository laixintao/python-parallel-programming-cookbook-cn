使用SCOOP进行科学计算
=====================
Scalable Concurrent Operations in Python (SCOOP) 是一个可扩展的 Python 并行计算库，可以将并行的任务（Python 的 ``Futures`` ）放到各种各样的计算节点上执行。它基于 ØMQ 架构，提供了一种在分布式系统中管理 Futures 的方法。SCOOP 主要的应用场景是科学计算，尽可能利用所有的结算资源来执行大量的分布式任务。

在将 Futures 分发这方面，SCOOP 使用了 Broker 模式的变体。

.. image:: ../images/SCOOP.png

这个通信系统的中心是 Broker，Broker 和所有的节点通讯，在它们之间传输信息。Futures 由各个节点创建，而不是由中心化的 Broker 创建。这种方案让系统的拓扑结构更加可靠，性能更高。事实上，Broker 占用的主要资源是 I/O ，CPU 使用很小。

|ready|

SCOOP 是
