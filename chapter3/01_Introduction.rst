介绍
====

在之前的章节中，我们见识了如何用线程实现并发的应用。本章节将会介绍基于进程的并行。本章的重点将会集中在Python的 ``multiprocessing`` 和 ``mpi4py`` 这两个模块上。

``multiprocessing`` 是Python标准库中的模块，实现了共享内存机制，也就是说，可以让运行在不同处理器核心的进程能读取共享内存。

``mpi4py`` 库实现了消息传递的编程范例（设计模式）。简单来说，就是进程之间不靠任何共享信息来进行通讯（也叫做shared nothing），所有的交流都通过传递信息代替。

这方面与使用共享内存通讯，通过加锁或类似机制实现互斥的技术行成对比。在信息传递的代码中，进程通过 ``send()`` 和 ``receive`` 进行交流。

在Python多进程的官方文档中，明确指出 ``multiprocessing`` 模块要求，使用此模块的函数的main模块对子类来说必须是可导入的（ https://docs.python.org/3.3/library/multiprocessing.html ）。

``__main__`` 在IDLE中并不是可以导入的，即使你在IDLE中将文件当做一个脚本来运行。为了能正确使用此模块，本章我们将在命令行使用下面的命令运行脚本： ::

    python multiprocessing example.py

这里， ``multiprocessing_example.py`` 是脚本的文件名。本章使用的解释器是Python3.3（实际上使用Python2.7也是可以的）。

（译者注，抱歉，这段译者无法理解原文和Python文档的意思。不过通过实验，我发现要多进程运行一个函数，这个函数必须从外部文件导入。比如说下面这样就不行： ::

		>>> from multiprocessing import Pool
		>>> p = Pool(5)
		>>> def f(x):
		...     return x*x
		...
		>>> p.map(f, [1,2,3])
		Process PoolWorker-1:
		Process PoolWorker-2:
		Process PoolWorker-3:
		Traceback (most recent call last):
		AttributeError: 'module' object has no attribute 'f'
		AttributeError: 'module' object has no attribute 'f'
		AttributeError: 'module' object has no attribute 'f'

上面脚本来自Python官网文档。如果稍作修改，将需要多进程运行的目标函数放到文件里导入运行，就没有问题了： ::

		In [1]: from multiprocessing import Pool

		In [2]: p = Pool(5)

		In [4]: import func

		In [5]: p.map(func.f, [1,2,3])
		Out[5]: [1, 4, 9]

译者注结束）
