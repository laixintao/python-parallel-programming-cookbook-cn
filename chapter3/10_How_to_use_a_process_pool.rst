如何使用进程池
==============

多进程库提供了 ``Pool`` 类来实现简单的多进程任务。 ``Pool`` 类有以下方法：

- ``apply()``: 直到得到结果之前一直阻塞。
- ``apply_async()``: 这是 ``apply()`` 方法的一个变体，返回的是一个result对象。这是一个异步的操作，在所有的子类执行之前不会锁住主进程。 
- ``map()``: 这是内置的 ``map()`` 函数的并行版本。在得到结果之前一直阻塞，此方法将可迭代的数据的每一个元素作为进程池的一个任务来执行。
- ``map_async()``: 这是 ``map()`` 方法的一个变体，返回一个result对象。如果指定了回调函数，回调函数应该是callable的，并且只接受一个参数。当result准备好时会自动调用回调函数（除非调用失败）。回调函数应该立即完成，否则，持有result的进程将被阻塞。  

|how|
-----

下面的例子展示了如果通过进程池来执行一个并行应用。我们创建了有4个进程的进程池，然后使用 ``map()`` 方法进行一个简单的计算。 ::

        import multiprocessing

        def function_square(data):
            result = data*data
            return result

        if __name__ == '__main__':
            inputs = list(range(100))
            pool = multiprocessing.Pool(processes=4)
            pool_outputs = pool.map(function_square, inputs)
            pool.close()
            pool.join()
            print ('Pool    :', pool_outputs)

计算的结果如下： ::

        $ python poll.py
        ('Pool    :', [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900, 961, 1024, 1089, 1156, 1225, 1296, 1369, 1444, 1521, 1600, 1681, 1764, 1849, 1936, 2025, 2116, 2209, 2304, 2401, 2500, 2601, 2704, 2809, 2916, 3025, 3136, 3249, 3364, 3481, 3600, 3721, 3844, 3969, 4096, 4225, 4356, 4489, 4624, 4761, 4900, 5041, 5184, 5329, 5476, 5625, 5776, 5929, 6084, 6241, 6400, 6561, 6724, 6889, 7056, 7225, 7396, 7569, 7744, 7921, 8100, 8281, 8464, 8649, 8836, 9025, 9216, 9409, 9604, 9801])

|how|
-----

``multiprocessing.Pool`` 方法在输入元素上应用 ``function_square`` 方法来执行简单的计算。并行的进程数量是4： ::

    pool = multiprocessing.Pool(processes=4)

``pool.map`` 方法将一些独立的任务提交给进程池： ::

    pool_outputs = pool.map(function_square, inputs)

``input`` 是一个从 ``0`` 到 ``100`` 的list： ::

    inputs = list(range(100))

计算的结果存储在 ``pool_outputs`` 中。最后的结果打印出来： ::

    print ('Pool    :', pool_outputs)

需要注意的是， ``pool.map()`` 方法的结果和Python内置的 ``map()`` 结果是相同的，不同的是 ``pool.map()`` 是通过多个并行进程计算的。    
