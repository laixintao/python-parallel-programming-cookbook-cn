通过 SCOOP 使用 map 函数
========================

当处理 list 或其他类型的序列时，一种很常用的操作是对序列中的每一个元素都执行相同的操作，然后收集结果。举例说，通过 Python IDLE 可以对一个 list 这样更新： ::

   >>>items = [1,2,3,4,5,6,7,8,9,10]
   >>>updated_items = []
   >>>for x in items:
   >>>    updated_items.append(x*2)
   >>> updated_items
   >>>  [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

这是比较常见的一个操作，但是 Python 内置了一些功能可以更优雅地完成类似操作。

Python 的函数 ``map(aFunction, aSequence)`` 将在序列的每一个元素上调用传入的函数，并将结果以 list 的形式返回。用这个函数完成上面的操作： ::

   >>>items = [1,2,3,4,5,6,7,8,9,10]
   >>>def multiplyFor2(x):return x*2
   >>>print(list(map(multiplyFor2,items)))
   >>>[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

这里，我们将自定义的 ``multiplyFor2`` 函数传给 ``map`` . 它将对 ``items`` 中所有的元素执行此函数，最后以 list 的形式返回结果。

我们也可以将 lambda 函数（不用绑定变量名的匿名函数）当做参数传给 ``map`` 函数。这段代码就变成以下这样: ::

   >>>items = [1,2,3,4,5,6,7,8,9,10]
   >>>print(list(map(lambda x:x*2,items)))
   >>>[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

内置的 map 函数比手动写 for 循环的性能更高。

|ready|
-------

SCOOP 模块提供了多个 map 函数可以将异步计算任务下发到多个计算节点：

- ``futures.map(func, iterables, kargs)`` : 此函数返回一个生成器，可以按照输入的顺序遍历结果。可以说是内置 ``map`` 函数的一个并行执行版本。
- ``futures.map_as_completed(func, iterables, kargs)`` : 每当有结果出现时，就立刻 yield 出来。
- ``futures.scoop.futures.mapReduce(mapFunc, reductionOp, iterables, kargs)`` : map 函数执行过后可以通过此函数执行 reduction 函数。返回结果是一个元素。

|how|
-----

在这个例子中，我们将对比 SCOOP 实现 MapReduce 和 Python 内置函数实现： ::

    """
    Compare SCOOP MapReduce with a serial implementation
    """
    import operator
    import time
    from scoop import futures

    def simulateWorkload(inputData):
        time.sleep(0.01)
        return sum(inputData)

    def CompareMapReduce():
        mapScoopTime = time.time()
        res = futures.mapReduce(
            simulateWorkload,
            operator.add,
            list([a] * a for a in range(1000)),
        )
        mapScoopTime = time.time() - mapScoopTime
        print("futures.map in SCOOP executed in {0:.3f}s with result:{1}".format(
              mapScoopTime, res))

        mapPythonTime = time.time()
        res = sum(map(simulateWorkload, list([a] * a for a in range(1000))))
        mapPythonTime = time.time() - mapPythonTime
        print("map Python executed in: {0:.3f}s with result: {1}".format(
            mapPythonTime, res))

    if __name__ == '__main__':
        CompareMapReduce()

这段代码通过以下命令来执行： ::

    python -m scoop map_reduce.py
    > [2015-06-12 20:13:25,602] launcher  INFO    SCOOP 0.7.2 dev on win32
    using Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC
    v.1600 32 bit (Intel)], API: 1013
    [2015-06-12 20:13:25,602] launcher  INFO Deploying 2 worker(s) over 1
    host(s).
    [2015-06-12 20:13:25,602] launcher  INFO Worker d--istribution:
    [2015-06-12 20:13:25,602] launcher  INFO 127.0.0.1:       1 + origin
    Launching 2 worker(s) using an unknown shell.
    futures.map in SCOOP executed in 8.459s with result: 332833500
    map Python executed in: 10.034s with result: 332833500
    [2015-06-12 20:13:45,344] launcher  (127.0.0.1:2559) INFO
    is done.
    [2015-06-12 20:13:45,368] launcher  (127.0.0.1:2559) INFO
    cleaning spawned subprocesses.

|work|
------

在这个例子中，我们将 SCOOP 实现的 MapReduce 和 Python 内置函数的 MapReduce 来对比。主要的函数是 ``CompareMapReduce()`` ，里面有两种实现和对时间的统计。程序结构如下： ::

    mapScoopTime = tme.time()
    #Run SCOOP MapReduce
    mapScoopTime = time.time() – mapScoopTime

    mapPythonTime = time.time()
    #Run serial MapReduce
    mapPythonTime = time.time() - mapPythonTime

在输出中，我们打印了执行时间： ::

   futures.map in SCOOP executed in 8.459s with result: 332833500
   map Python executed in: 10.034s with result: 332833500

为了得到比较明显的时间比较，我们在 ``simulatedWordload`` 函数中引入了 ``time.sleep`` 来延长计算时间。 ::

    def simulateWorkload(inputData, chose=None):
        time.sleep(0.01)
        return sum(inputData)

SCOOP 版本的 MapReduce 如下： ::

    res = futures.mapReduce(
        simulateWorkload,
        operator.add,
        list([a] * a for a in range(1000)),
    )

``futures.mapReduce`` 函数需要以下参数：

- ``simulateWork`` : 这是要执行的 Futures，注意这个 callable 必须有返回值。
- ``operator.add`` : 此函数将会在 reduce 操作的时候调用，必须接收两个参数，返回一个值。
- ``list(...)`` : 一个可迭代对象，其中每一个元素都会传给 callable 对象作为 Future。

使用 Python 内置函数实现的 MapReduce 如下： ::

    res = sum(map(simulateWorkload,
                  list([a] * a for a in range(1000))))
 
Python 内置的 ``map()`` 函数接受两个参数： ``simulateWorkload`` 函数和可迭代的 ``list()`` 对象。Reduce 操作我们只是简单地用 Python 内置的 ``sum()`` 函数。
