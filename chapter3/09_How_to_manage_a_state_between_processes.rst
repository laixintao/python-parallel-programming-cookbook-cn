如何在进程之间管理状态
======================

Python的多进程模块提供了在所有的用户间管理共享信息的管理者(Manager)。一个管理者对象控制着持有Python对象的服务进程，并允许其它进程操作共享对象。

管理者有以下特性：

- 它控制着管理共享对象的服务进程
- 它确保当某一进程修改了共享对象之后，所有的进程拿到额共享对象都得到了更新

|how|
-----

下面来看一个再进程之间共享对象的例子：

1. 首先，程序创建了一个管理者的字典，在 ``n`` 个 ``taskWorkers`` 之间共享，每个worker更新字典的某一个index。
2. 所有的worker完成之后，新的列表打印到 ``stdout`` :   ::

        import multiprocessing

        def worker(dictionary, key, item):
           dictionary[key] = item
           print("key = %d value = %d" % (key, item))

        if __name__ == '__main__':
            mgr = multiprocessing.Manager()
            dictionary = mgr.dict()
            jobs = [multiprocessing.Process(target=worker, args=(dictionary, i, i*2)) for i in range(10)]
            for j in jobs:
                j.start()
            for j in jobs:
                j.join()
            print('Results:', dictionary)

（译者注: 源代码中少了一行print，译者加上了，能得到和书中输出一样的结果）

运行结果如下： ::

		$ python manager.py
		key = 0 value = 0
		key = 3 value = 6
		key = 2 value = 4
		key = 1 value = 2
		key = 4 value = 8
		key = 5 value = 10
		key = 8 value = 16
		key = 6 value = 12
		key = 7 value = 14
		key = 9 value = 18
		Results: {0: 0, 3: 6, 2: 4, 1: 2, 4: 8, 5: 10, 8: 16, 6: 12, 7: 14, 9: 18}

|work|
------

我们在先声明了一个manager： ::

    mgr = multiprocessing.Manager()

下面一行创建了 ``dictionary`` 类型的一个数据结构： ::

    dictionary = mgr.dict()

然后，启动多进程： ::

    jobs = [multiprocessing.Process(target=worker, args=(dictionary, i, i*2)) for i in range(10)]
    for j in jobs:
        j.start()

这里，目标函数 ``taskWorker`` 往字典中添加一个item： ::

        def worker(dictionary, key, item):
           dictionary[key] = item

最后，我们得到字典所有的值并打印出来： ::

    for j in jobs:
        j.join()
    print('Results:', dictionary)

