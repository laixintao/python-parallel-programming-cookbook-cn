如何在后台运行一个进程
======================

如果需要处理比较巨大的任务，又不需要人为干预，将其作为后台进程执行是个非常常用的编程模型。此进程又可以和其他进程并发执行。通过Python的multiprocessing模块的后台进程选项，我们可以让进程在后台运行。

|how|
-----

运行后台进程，可以参照以下代码： ::

        import multiprocessing
        import time

        def foo():
            name = multiprocessing.current_process().name
            print("Starting %s " % name)
            time.sleep(3)
            print("Exiting %s " % name)

        if __name__ == '__main__':
            background_process = multiprocessing.Process(name='background_process', target=foo)
            background_process.daemon = True
            NO_background_process = multiprocessing.Process(name='NO_background_process', target=foo)
            NO_background_process.daemon = False
            background_process.start()
            NO_background_process.start()

运行上面的脚本，需要使用下面的命令： ::

    python background_process.py

最后的输出如下： ::

        $ python background_process.py
        Starting NO_background_process
        Exiting NO_background_process

|work|
------

为了在后台运行进程，我们设置 ``daemon`` 参数为 ``True`` ::

    background_process.daemon = True

在非后台运行的进程会看到一个输出，后台运行的没有输出，后台运行进程在主进程结束之后会自动结束。

|more|
------

注意，后台进程不允许创建子进程。否则，当后台进程跟随父进程退出的时候，子进程会变成孤儿进程。另外，它们并不是Unix的守护进程或服务（daemons or services），所以当非后台进程退出，它们会被终结。
