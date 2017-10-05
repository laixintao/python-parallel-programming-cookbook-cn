如何产生一个进程
================

“产生”（spawn）的意思是，由父进程创建子进程。父进程既可以在产生子进程之后继续异步执行，也可以暂停等待子进程创建完成之后再继续执行。Python的multiprocessing库通过以下几步创建进程：

1. 创建进程对象
2. 调用 ``start()`` 方法，开启进程的活动
3. 调用 ``join()`` 方法，在进程结束之前一直等待

|how|
-----

下面的例子创建了5个进程，每一个进程都分配了 ``foo(i)`` 函数， ``i`` 表示进程的id： ::

        # -*- coding: utf-8 -*-

        import multiprocessing

        def foo(i):
            print ('called function in process: %s' %i)
            return
         
        if __name__ == '__main__':
            Process_jobs = []
            for i in range(5):
                p = multiprocessing.Process(target=foo, args=(i,))
                Process_jobs.append(p)
                p.start()
                p.join()

执行本例需要打开命令行，到文件 ``spawn_a_process.py`` （脚本名字）所在的目录下，然后输入下面的命令执行： ::

    python spawn_a_process.py

我们会得到以下结果： ::

		$ python process_2.py
		called function in process: 0
		called function in process: 1
		called function in process: 2
		called function in process: 3
		called function in process: 4

|work|
------

按照本节前面提到的步骤，创建进程对象首先需要引入multiprocessing模块： ::

    import multiprocessing

然后，我们在主程序中创建进程对象： ::

    p = multiprocessing.Process(target=foo, args=(i,))

最后，我们调用 ``start()`` 方法启动： ::

    p.start()

进程对象的时候需要分配一个函数，作为进程的执行任务，本例中，这个函数是 ``foo()`` 。我们可以用元组的形式给函数传递一些参数。最后，使用进程对象调用 ``join()`` 方法。

如果没有 ``join()`` ，主进程退出之后子进程会留在idle中，你必须手动杀死它们。

|more|
------


这是因为，子进程创建的时候需要导入包含目标函数的脚本。通过在 ``__main__`` 代码块中实例化进程对象，我们可以预防无限递归调用。最佳实践是在不同的脚本文件中定义目标函数，然后导入进来使用。所以上面的代码可以修改为： ::

    import multiprocessing
    import target_function
    if __name__ == '__main__':
        Process_jobs = []
        for i in range(5):
            p = multiprocessing.Process(target=target_function.function,args=(i,))
            Process_jobs.append(p)
            p.start()
            p.join()

``target_function.py`` 的内容如下： ::

    def function(i):
        print('called function in process: %s' %i)
        return

输出和上面一样。
