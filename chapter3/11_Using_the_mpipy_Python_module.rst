使用Python的mpi4py模块
======================

Python 提供了很多MPI模块写并行程序。其中 ``mpi4py`` 是一个又有意思的库。它在MPI-1/2顶层构建，提供了面向对象的接口，紧跟C++绑定的 MPI-2。MPI的C语言用户可以无需学习新的接口就可以上手这个库。所以，它成为了Python中最广泛使用的MPI库。

此模块包含的主要应用有：

- 点对点通讯
- 集体通讯
- 拓扑

|ready|
-------

在Windows中安装 ``mpi4py`` 的过程如下（其他操作系统可以参考 http://mpi4py.scipy.org/docs/usrman/install.html ）:

1. 从
