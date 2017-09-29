使用 ``queue`` 进行线程通信
============================

前面我们已经讨论到，当线程之间如果要共享资源或数据的时候，可能变的非常复杂。如你所见，Python的threading模块提供了很多同步原语，包括信号量，条件变量，事件和锁。如果可以使用这些原语的话，应该优先考虑使用这些，而不是使用queue（队列）模块。队列操作起来更容易，也使多线程编程更安全，因为队列可以将资源的使用通过单线程进行完全控制，并且可以使用“清理着”等可读性更高的设计模式。

Queue常用的方法有以下四个：

- ``put()``: 往queue中放一个item
- ``get()``: 从queue删除一个item，并返回删除的这个item
- ``task_done()``: 每次item被处理的时候需要调用这个方法
- ``join()``: 所有item都被处理之前一直阻塞

|how|
-----

在本例中，我们将学习如何在threading模块中使用queue。同样，本里中将会有两个实体共享部分资源，代码如下： ::

        from threading import Thread, Event
        from queue import Queue
        import time
        import random
        class producer(Thread):
            def __init__(self, queue):
                Thread.__init__(self)
                self.queue = queue

            def run(self) :
                for i in range(10):
                    item = random.randint(0, 256)
                    self.queue.put(item)
                    print('Producer notify: item N° %d appended to queue by %s' % (item, self.name))
                    time.sleep(1)

        class consumer(Thread):
            def __init__(self, queue):
                Thread.__init__(self)
                self.queue = queue

            def run(self):
                while True:
                    item = self.queue.get()
                    print('Consumer notify : %d popped from queue by %s' % (item, self.name))
                    self.queue.task_done()

        if __name__ == '__main__':
            queue = Queue()
            t1 = producer(queue)
            t2 = consumer(queue)
            t3 = consumer(queue)
            t4 = consumer(queue)
            t1.start()
            t2.start()
            t3.start()
            t4.start()
            t1.join()
            t2.join()
            t3.join()
            t4.join()

代码的运行结果如下：

.. image:: ../images/Page-85-Image-15.png

|work|
------


