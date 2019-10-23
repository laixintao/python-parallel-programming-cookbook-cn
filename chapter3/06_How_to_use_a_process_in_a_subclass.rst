如何在子类中使用进程
====================

实现一个自定义的进程子类，需要以下三步：

- 定义 ``Process`` 的子类
- 覆盖 ``__init__(self [,args])`` 方法来添加额外的参数
- 覆盖 ``run(self, [.args])`` 方法来实现 ``Process`` 启动的时候执行的任务

创建 ``Porcess`` 子类之后，你可以创建它的实例并通过 ``start()`` 方法启动它，启动之后会运行 ``run()`` 方法。

|how|
-----

我们将使用子类的形式重写之前的例子： ::

		# -*- coding: utf-8 -*-
		# 自定义子类进程
		import multiprocessing

		class MyProcess(multiprocessing.Process):
			def run(self):
				print ('called run method in process: %s' % self.name)
				return
		 
		if __name__ == '__main__':
			jobs = []
			for i in range(5):
				p = MyProcess()
				jobs.append(p)
				p.start()
				p.join()

输入以下命令运行脚本： ::

    python subclass_process.py

运行结果如下： ::

		$ python subclass.py
		called run method in process: MyProcess-1
		called run method in process: MyProcess-2
		called run method in process: MyProcess-3
		called run method in process: MyProcess-4
		called run method in process: MyProcess-5

|work|
------

每一个继承了 ``Process`` 并重写了 ``run()`` 方法的子类都代表一个进程。此方法是进程的入口： ::

        class MyProcess(multiprocessing.Process):
            def run(self):
                print ('called run method in process: %s' % self.name)
                return

在主程序中，我们创建了一些 ``MyProcess()`` 的子类。当 ``start()`` 方法被调用的时候进程开始执行： ::

        p = MyProcess()
        p.start()

``join()`` 命令可以让主进程等待其他进程结束最后退出。
