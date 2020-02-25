如何为一个进程命名
==================

在上一节的例子中，我们创建了一个进程，并为其分配了目标函数和函数变量。然而如果能给进程分配一个名字，那么debug的时候就更方便了。

|how|
-----

命名进程的方法和前一章中介绍的命名线程差不多（参考第二章，基于线程的并行，第四节，如何确定当前的线程）。

下面的代码在主程序中创建了一个有名字的进程和一个没有名字的进程，目标函数都是 ``foo()`` 函数。 ::

        # 命名一个进程
        import multiprocessing
        import time

        def foo():
            name = multiprocessing.current_process().name
            print("Starting %s \n" % name)
            time.sleep(3)
            print("Exiting %s \n" % name)

        if __name__ == '__main__':
            process_with_name = multiprocessing.Process(name='foo_process', target=foo)
            process_with_name.daemon = True  # 注意原代码有这一行，但是译者发现删掉这一行才能得到正确输出
            process_with_default_name = multiprocessing.Process(target=foo)
            process_with_name.start()
            process_with_default_name.start()

运行上面的代码，打开终端输入:  ::

    python naming_process.py

输出的结果如下： ::

        $ python naming_process.py
        Starting foo_process
        Starting Process-2
        Exiting foo_process
        Exiting Process-2

|work|
------

这个过程和命名线程很像。命名进程需要为进程对象提供 ``name`` 参数： ::

    process_with_name = multiprocessing.Process(name='foo_process', target=foo)

在本例子中，进程的名字就是 ``foo_function`` 。如果子进程需要知道父进程的名字，可以使用以下声明： ::

    name = multiprocessing.current_process().name

然后就能看见父进程的名字。    
