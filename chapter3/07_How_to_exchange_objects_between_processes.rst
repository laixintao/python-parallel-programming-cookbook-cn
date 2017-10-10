如何在进程之间交换对象
======================

并行应用常常需要在进程之间交换数据。Multiprocessing库有两个Communication Channel可以交换对象：队列(queue)和管道（pipe）。

.. images:: ../images/communication-channel.png

使用队列交换对象
----------------

我们可以通过队列数据结构来共享对象。


