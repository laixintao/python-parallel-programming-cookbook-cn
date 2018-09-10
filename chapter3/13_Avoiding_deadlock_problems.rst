避免死锁问题
============

我们经常需要面临的一个问题是死锁，这是两个或多个进程都在阻塞并等待对方释放自己想要的资源的情况。 ``mpi4py`` 没有提供特定的功能来解决这种情况，但是提供了一些程序员必须遵守的规则，来避免死锁问题。

|how|
-----

让我们先分析下面的Python代码，下面的代码中介绍了一种典型的死锁问题；我们有两个进程，一个 ``rank`` 等于1，另一个 ``rank`` 等于5，他们互相通讯，并且每一个都有发送和接收的函数。 ::

        from mpi4py import MPI
        comm=MPI.COMM_WORLD
        rank = comm.rank
        print("my rank is : " , rank)

        if rank==1:
            data_send= "a"
            destination_process = 5
            source_process = 5
            data_received=comm.recv(source=source_process)
            comm.send(data_send,dest=destination_process)
            print("sending data %s " %data_send + "to process %d" %destination_process)
            print("data received is = %s" %data_received)

        if rank==5:
            data_send= "b"
            destination_process = 1
            source_process = 1
            data_received=comm.recv(source=source_process)
            comm.send(data_send,dest=destination_process)            
            print("sending data %s :" %data_send + "to process %d" %destination_process)
            print("data received is = %s" %data_received)

|work|
------

如果我们尝试运行这个程序（只有两个进程足够了），会发现这两个进程都不会完成： ::

        $ mpiexec -n 9 python deadLockProblems.py
        ('my rank is : ', 8)
        ('my rank is : ', 3)
        ('my rank is : ', 2)
        ('my rank is : ', 7)
        ('my rank is : ', 0)
        ('my rank is : ', 4)
        ('my rank is : ', 6)

此时连个进程都在等待对方，都被阻塞住了。会发生这种情况是因为MPI的 ``comm.recv()`` 函数和 ``comm.send()`` 函数都是阻塞的。它们的调用者都在等待它们完成。对 ``comm.send()`` MPI来说，只有数据发出之后函数才会结束，对于 ``comm.recv()`` 函数来说，只有接收到数据函数才会结束。为了解决这个问题，我们可以将这连个函数这样写： ::

   if rank==1:
       data_send= "a"
       destination_process = 5
       source_process = 5
       comm.send(data_send,dest=destination_process)
       data_received=comm.recv(source=source_process)
   if rank==5:
       data_send= "b"
       destination_process = 1
       source_process = 1
       data_received=comm.recv(source=source_process)
       comm.send(data_send,dest=destination_process)

虽然这个解决方法从逻辑上纠正了，但是并不保证一定可以避免死锁问题。鉴于通讯是发生在buffer的， ``comm.send()`` 函数将要发送的数据完全拷贝到buffer里，只有buffer里有完整的数据之后程序才能继续运行。否则，依然会产生死锁：发送者不能发送，因为buffer已经提交但是接收到不能接收者不能接收数据，因为它被 ``comm.send()`` 阻塞住了。因此，我们可以交换一下发送者和接收者的顺序来解决这个问题。 ::

   if rank==1:
       data_send= "a"
       destination_process = 5
       source_process = 5
       comm.send(data_send,dest=destination_process)
       data_received=comm.recv(source=source_process)
   if rank==5:
       data_send= "b"
       destination_process = 1
       source_process = 1
       comm.send(data_send,dest=destination_process)
       data_received=comm.recv(source=source_process)

最后，我们得到正确的输出如下： ::

        $ mpiexec -n 9 python deadLockProblems.py
        ('my rank is : ', 7)
        ('my rank is : ', 0)
        ('my rank is : ', 8)
        ('my rank is : ', 1)
        sending data a to process 5
        data received is = b
        ('my rank is : ', 5)
        sending data b :to process 1
        data received is = a
        ('my rank is : ', 2)
        ('my rank is : ', 3)
        ('my rank is : ', 4)
        ('my rank is : ', 6)

|more|
------

此并非是解决死锁问题的唯一方案。举个例子，有一个特定的函数统一了向一特定进程发消息和从一特定进程接收消息的功能，叫做 ``Sendrecv`` ::

    Sendrecv(self, sendbuf, int dest=0, int sendtag=0, recvbuf=None, int source=0, int recvtag=0, Status status=None)

可以看到，这个函数的参数同 ``comm.send()`` MPI 以及 ``comm.recv()`` MPI 相同。同时在这个函数里，整个函数都是阻塞的，相比于交给子系统来负责检查发送者和接收者之间的依赖，可以避免死锁问题。用这个方案改写之前的例子如下： ::

        if rank==1:
            data_send= "a"
            destination_process = 5
            source_process = 5
            data_received=comm.sendrecv(data_send,dest=destination_process,source =source_process)
        if rank==5:
            data_send= "b"
            destination_process = 1
            source_process = 1
            data_received=comm.sendrecv(data_send,dest=destination_process, source=source_process)
