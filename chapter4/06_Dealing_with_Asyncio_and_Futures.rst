使用Asyncio和Futures
====================

Asyncio 模块的另一个重要的组件是 ``Future`` 类。它和 ``concurrent.futures.Futures`` 很像，但是针对Asyncio的事件循环做了很多定制。 ``asyncio.Futures`` 类代表还未完成的结果（有可能是一个Exception）。所以综合来说，它是一种抽象，代表还没有做完的事情。

实际上，必须处理一些结果的回调函数被加入到了这个类的实例中。

|ready|
-------

要操作Asyncio中的 ``Future`` ，必须进行以下声明： ::

    import asyncio
    future = asyncio.Future()

基本的方法有： 

- ``cancel()``: 取消future的执行，调度回调函数
- ``result()``: 返回future代表的结果
- ``exception()``: 返回future中的Exception
- ``add_done_callback(fn)``: 添加一个回调函数，当future执行的时候会调用这个回调函数
- ``remove_done_callback(fn)``: 从“call whten done”列表中移除所有callback的实例
- ``set_result(result)``: 将future标为执行完成，并且设置result的值
- ``set_exception(exception)``: 将future标为执行完成，并设置Exception

|how|
-----

下面的例子展示了 ``Future`` 类是如何管理两个协程的，第一个协程 ``first_coroutine`` 计算前n个数的和， 第二个协程 ``second_coroutine`` 计算n的阶乘，代码如下： ::

        # -*- coding: utf-8 -*-

        """
        Asyncio.Futures -  Chapter 4 Asynchronous Programming
        """
        import asyncio
        import sys

        @asyncio.coroutine
        def first_coroutine(future, N):
            """前n个数的和"""
            count = 0
            for i in range(1, N + 1):
                count = count + i
            yield from asyncio.sleep(3)
            future.set_result("first coroutine (sum of N integers) result = " + str(count))

        @asyncio.coroutine
        def second_coroutine(future, N):
            count = 1
            for i in range(2, N + 1):
                count *= i
            yield from asyncio.sleep(4)
            future.set_result("second coroutine (factorial) result = " + str(count))

        def got_result(future):
           print(future.result())

        if __name__ == "__main__":
           N1 = int(sys.argv[1])
           N2 = int(sys.argv[2])
           loop = asyncio.get_event_loop()
           future1 = asyncio.Future()
           future2 = asyncio.Future()
           tasks = [
               first_coroutine(future1, N1),
               second_coroutine(future2, N2)]
           future1.add_done_callback(got_result)
           future2.add_done_callback(got_result)
           loop.run_until_complete(asyncio.wait(tasks))
           loop.close()

输出如下： ::

        $ python asy.py 1 1
        first coroutine (sum of N integers) result = 1
        second coroutine (factorial) result = 1
        $ python asy.py 2 2
        first coroutine (sum of N integers) result = 3
        second coroutine (factorial) result = 2
        $ python asy.py 3 3
        first coroutine (sum of N integers) result = 6
        second coroutine (factorial) result = 6
        $ python asy.py 4 4
        first coroutine (sum of N integers) result = 10
        second coroutine (factorial) result = 24

|work|
------

在主程序中，我们通过定义future对象和协程联系在一起： ::

        if __name__ == "__main__":
           ...
           future1 = asyncio.Future()
           future2 = asyncio.Future()

定义tasks的时候，将future对象作为变量传入协程中： ::

   tasks = [
       first_coroutine(future1, N1),
       second_coroutine(future2, N2)]

最后，添加一个 ``future`` 执行时的回调函数： ::

        def got_result(future):
           print(future.result())

在我们传入future的协程中，在计算之后我们分别添加了3s、4s的睡眠时间： ::

    yield from asyncio.sleep(4)

然后，我们将future标为完成，通过 ``future.set_result()`` 设置结果。

|more|
------

交换两个协程睡眠的时间，协程2会比1更早得到结果： ::

        $ python asy.py 3 3
        second coroutine (factorial) result = 6
        first coroutine (sum of N integers) result = 6
        $ python asy.py 4 4
        second coroutine (factorial) result = 24
        first coroutine (sum of N integers) result = 10
