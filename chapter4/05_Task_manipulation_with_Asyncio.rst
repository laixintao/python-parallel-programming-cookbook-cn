使用Asyncio控制任务
===================

Asyncio是用来处理事件循环中的异步进程和并发任务执行的。它还提供了 ``asyncio.Task()`` 类，可以在任务中使用协程。它的作用是，在同一事件循环中,运行某一个任务的同时可以并发地运行多个任务。当协程被包在任务中，它会自动将任务和事件循环连接起来，当事件循环启动的时候，任务自动运行。这样就提供了一个可以自动驱动协程的机制。

|ready|
-------

Asyncio模块为我们提供了 ``asyncio.Task(coroutine)`` 方法来处理计算任务，它可以调度协程的执行。任务对协程对象在事件循环的执行负责。如果被包裹的协程要从future yield，那么任务会被挂起，等待future的计算结果。

当future计算完成，被包裹的协程将会拿到future返回的结果或异常（exception）继续执行。另外，需要注意的是，事件循环一次只能运行一个任务，除非还有其它事件循环在不同的线程并行运行，此任务才有可能和其他任务并行。当一个任务在等待future执行的期间，事件循环会运行一个新的任务。

|how|
-----

在下面的代码中，我们展示了三个可以被 ``Asyncio.Task()`` 并发执行的数学函数。


运行的结果如下： ::

    python3 task.py
    Asyncio.Task: Compute factorial(2)
    Asyncio.Task: Compute fibonacci (0)
    Asyncio.Task: Compute binomialCoeff (1)
    Asyncio.Task: Compute factorial(3)
    Asyncio.Task: Compute fibonacci (1)
    Asyncio.Task: Compute binomialCoeff (2)
    Asyncio.Task: Compute factorial(4)
    Asyncio.Task: Compute fibonacci (2)
    Asyncio.Task: Compute binomialCoeff (3)
    Asyncio.Task: Compute factorial(5)
    Asyncio.Task: Compute fibonacci (3)
    Asyncio.Task: Compute binomialCoeff (4)
    Asyncio.Task: Compute factorial(6)
    Asyncio.Task: Compute fibonacci (4)
    Asyncio.Task: Compute binomialCoeff (5)
    Asyncio.Task: Compute factorial(7)
    Asyncio.Task: Compute fibonacci (5)
    Asyncio.Task: Compute binomialCoeff (6)
    Asyncio.Task: Compute factorial(8)
    Asyncio.Task: Compute fibonacci (6)
    Asyncio.Task: Compute binomialCoeff (7)
    Asyncio.Task: Compute factorial(9)
    Asyncio.Task: Compute fibonacci (7)
    Asyncio.Task: Compute binomialCoeff (8)
    Asyncio.Task: Compute factorial(10)
    Asyncio.Task: Compute fibonacci (8)
    Asyncio.Task: Compute binomialCoeff (9)
    Asyncio.Task - factorial(10) = 3628800
    Asyncio.Task: Compute fibonacci (9)
    Asyncio.Task: Compute binomialCoeff (10)
    Asyncio.Task - fibonacci(10) = 55
    Asyncio.Task - binomialCoeff(20 , 10) = 184756.0

|work|
------


