PyCSP和通信顺序进程
===================

PyCSP 是基于通信顺序进程的一个 Python 模块。通信顺序进程是通过消息处理建立并发程序的编程范式。PyCSP 模块的特点是:

- 进程之间交换消息
- 线程之间可以共享内存
- 通过 channels 来实现交换消息

Channels 可以做：
- 进程之间传值
- 进程同步

PyCSP 允许多种不同的 channel 类型: One2One, One2Any, Any2One, Any2Any. 这些名字代表多少 readers 和 writers 可以额通过 channel 通讯。

|ready|
-------


