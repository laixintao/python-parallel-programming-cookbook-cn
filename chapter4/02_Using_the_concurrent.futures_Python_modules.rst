使用Python的 ``concurrent.futures`` 模块
========================================

Python3.2带来了 ``concurrent.future`` 模块，这个模块具有线程池和进程池、管理并行编程任务、处理非确定性的执行流程、进程/线程同步等功能。

此模块由以下部分组成：

- ``concurrent.futures.Executor``: 这是一个虚拟基类，提供了一步执行的方法。
- ``submit(function, argument)``: 调度函数（可调用的对象）的执行，将 ``argument`` 作为参数传入。
- ``map(function, argument)``: 将 ``argument`` 作为参数执行函数，以 **异步** 的方式。
- ``shutdown(Wait=True)``: 发出让执行者释放所有资源的信号。
- ``concurrent.futures.Future``: 其中包括函数的异步执行。Future对象是submit任务（即带有参数的functions）到executor的实例。

Executor是抽象类，可以通过子类访问，即线程或进程的 ``ExecutorPools`` 。因为，线程或进程的实例是依赖于资源的任务，所以最好以“池”的形式将他们组织在一起，作为可以重用的launcher或executor。

使用线程池和进程池
------------------

线程池或进程池是用于在程序中优化和简化线程/进程的使用。通过池，你可以提交任务给executor。池由两部分组成，一部分是内部的队列，存放着待执行的任务；另一部分是一系列的进程或线程，用于执行这些任务。池的概念主要目的是为了重用：让线程或进程在生命周期内可以多次使用。它减少了创建创建线程和进程的开销，提高了程序性能。重用不是必须的规则，但它是程序员在应用中使用池的主要原因。

.. image:: ../images/pooling-management.png

|ready|
-------

``current.Futures`` 模块提供了两种 ``Executor`` 的子类，各自独立操作一个线程池和一个进程池。这两个子类分别是：

- ``concurrent.futures.ThreadPoolExecutor(max_workers)``
- ``concurrent.futures.ProcessPoolExecutor(max_workers)``
 
``max_workers`` 参数表示最多有多少个worker并行执行任务。

|how|
-----

下面的示例代码展示了线程池和进程池的功能。这里的任务是，给一个list ``number_list`` ，包含1到10。对list中的每一个数字，乘以1+2+3...+10000000的和（这个任务只是为了消耗时间）。

下面的代码分别测试了：

- 顺序执行
- 通过有5个worker的线程池执行
- 通过有5个worker的进程池执行

代码如下：::

        # -*- coding: utf-8 -*-

        """ Concurrent.Futures Pooling - Chapter 4 Asynchronous Programming """

        import concurrent.futures
        import time
        number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        def evaluate_item(x):
            # 计算总和，这里只是为了消耗时间
            result_item = count(x)
            # 打印输入和输出结果
            print ("item " + str(x) + " result " + str(result_item))

        def  count(number) :
            for i in range(0, 10000000):
                i=i+1
            return i * number

        if __name__ == "__main__":
            # 顺序执行
            start_time = time.clock()
            for item in number_list:
                evaluate_item(item)
            print("Sequential execution in " + str(time.clock() - start_time), "seconds")
            # 线程池执行
            start_time_1 = time.clock()
            with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
                for item in number_list:
                    executor.submit(evaluate_item,  item)
            print ("Thread pool execution in " + str(time.clock() - start_time_1), "seconds")
            # 进程池
            start_time_2 = time.clock()
            with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
                for item in number_list:
                    executor.submit(evaluate_item,  item)
            print ("Process pool execution in " + str(time.clock() - start_time_2), "seconds")

运行这个代码，我们可以看到运行时间的输出：::

		$ python3 pool.py
		item 1 result 10000000
		item 2 result 20000000
		item 3 result 30000000
		item 4 result 40000000
		item 5 result 50000000
		item 6 result 60000000
		item 7 result 70000000
		item 8 result 80000000
		item 9 result 90000000
		item 10 result 100000000
		Sequential execution in 7.495329 seconds
		item 1 result 10000000
		item 2 result 20000000
		item 4 result 40000000
		item 3 result 30000000
		item 5 result 50000000
		item 8 result 80000000
		item 7 result 70000000
		item 9 result 90000000
		item 6 result 60000000
		item 10 result 100000000
		Thread pool execution in 8.349609000000001 seconds
		item 1 result 10000000
		item 2 result 20000000
		item 3 result 30000000
		item 4 result 40000000
		item 5 result 50000000
		item 7 result 70000000
		item 8 result 80000000
		item 6 result 60000000
		item 9 result 90000000
		item 10 result 100000000
		Process pool execution in 0.02012900000000073 seconds

|work|
------


