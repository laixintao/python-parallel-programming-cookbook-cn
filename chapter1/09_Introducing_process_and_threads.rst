介绍线程和进程
==============

进程是应用程序的一个执行实例，比如，在桌面上双击浏览器图标将会运行一个浏览器。线程是一个控制流程，可以在进程内与其他活跃的线程同时执行。“控制流程”指的是顺序执行一些机器指令。进程可以包含多个线程，所以开启一个浏览器，操作系统将创建一个进程，并开始执行这个进程的主线程。每一个线程将独立执行一系列的指令（通常就是一个函数），并且和其他线程并行执行。然而，同一个进程内的线程可以共享一些地址空间和数据结构。线程也被称作“轻量进程”，因为它和进程有许多共同点，比如都是可以和其他控制流程同时运行的控制流程，说它“轻量”是因为实现一个进程比线程要繁重的多。重申一遍，不同于进程，多个线程可以共享很多资源，特别是地址空间和数据结构等。

总结一下：

- 进程可以包含多个并行运行的线程。
- 通常，操作系统创建和管理线程比进程更能节省CPU的资源。线程用于一些小任务，进程用于繁重的任务——运行应用程序。
- 同一个进程下的线程共享地址空间和其他资源，进程之间相互独立。

在深入研究通过线程和进程管理并行的Python模块之前，我们先来看一下Python中是如何使用这两者的。
