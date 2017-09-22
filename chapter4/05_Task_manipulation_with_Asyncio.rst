使用Asyncio控制任务
===================

Asyncio是用来处理事件循环中的异步进程和并发任务执行的。它还提供了 ``asyncio.Task()`` 类，可以在任务中使用协程。它的作用是，在同一事件循环中,运行某一个任务的同时可以并发地运行多个任务。当协程被包在任务中，它会自动将任务和事件循环连接起来，当事件循环启动的时候，任务自动运行。这样就提供了一个可以自动驱动协程的机制。

|ready|
-------

Asyncio模块为我们提供了 ``asyncio.Task(coroutine)`` 方法来处理计算任务，它可以调度协程的执行。任务对协程对象在事件循环的执行负责。如果被包裹的协程要从future yield，那么任务会被挂起，等待future的计算结果。

当future计算完成，被包裹的协程将会拿到future返回的结果或异常（exception）继续执行。另外，需要注意的是，事件循环一次只能运行一个任务，除非还有其它事件循环在不同的线程并行运行，此任务才有可能和其他任务并行。当一个任务在等待future执行的期间，事件循环会运行一个新的任务。 ::

    """
    Asyncio using Asyncio.Task to execute three math function in parallel
    """
    import asyncio
    @asyncio.coroutine
    def factorial(number):
        f = 1
        for i in range(2, number + 1):
            print("Asyncio.Task: Compute factorial(%s)" % (i))
            yield from asyncio.sleep(1)
            f *= i
        print("Asyncio.Task - factorial(%s) = %s" % (number, f))

    @asyncio.coroutine
    def fibonacci(number):
        a, b = 0, 1
        for i in range(number):
            print("Asyncio.Task: Compute fibonacci (%s)" % (i))
            yield from asyncio.sleep(1)
            a, b = b, a + b
        print("Asyncio.Task - fibonacci(%s) = %s" % (number, a))

    @asyncio.coroutine
    def binomialCoeff(n, k):
        result = 1
        for i in range(1, k+1):
            result = result * (n-i+1) / i
            print("Asyncio.Task: Compute binomialCoeff (%s)" % (i))
            yield from asyncio.sleep(1)
        print("Asyncio.Task - binomialCoeff(%s , %s) = %s" % (n, k, result))

    if __name__ == "__main__":
        tasks = [asyncio.Task(factorial(10)),
                 asyncio.Task(fibonacci(10)),
                 asyncio.Task(binomialCoeff(20, 10))]
        loop = asyncio.get_event_loop()
        loop.run_until_complete(asyncio.wait(tasks))
        loop.close()

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

在这个例子中，我们定义了三个协程， ``factorial``, ``fibonacci`` 和 ``binomialCoeff`` ，每一个都带有 ``asyncio.coroutine`` 装饰器： ::

    @asyncio.coroutine
    def factorial(number):
        do Something

    @asyncio.coroutine
    def fibonacci(number):
        do Something

    @asyncio.coroutine
    def binomialCoeff(n, k):
        do Something

为了能并行执行这三个任务，我们将其放到一个task的list中： ::

    if __name__ == "__main__":
        tasks = [asyncio.Task(factorial(10)),
                 asyncio.Task(fibonacci(10)),
                 asyncio.Task(binomialCoeff(20, 10))]

得到事件循环： ::

        loop = asyncio.get_event_loop()

然后运行任务： ::

        loop.run_until_complete(asyncio.wait(tasks))

这里， ``asyncio.wait(tasks)`` 表示运行直到所有给定的协程都完成。

最后，关闭事件循环：  ::

        loop.close()
