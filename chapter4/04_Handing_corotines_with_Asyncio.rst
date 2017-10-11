使用Asyncio管理协程
===================

在上文提到的例子中，我们看到当一个程序变得很大而且复杂时，将其划分为子程序，每一部分实现特定的任务是个不错的方案。子程序不能单独执行，只能在主程序的请求下执行，主程序负责协调使用各个子程序。协程就是子程序的泛化。和子程序一样的事，协程只负责计算任务的一步；和子程序不一样的是，协程没有主程序来进行调度。这是因为协程通过管道连接在一起，没有监视函数负责顺序调用它们。在协程中，执行点可以被挂起，可以被从之前挂起的点恢复执行。通过协程池就可以插入到计算中：运行第一个任务，直到它返回(yield)执行权，然后运行下一个，这样顺着执行下去。

这种插入的控制组件就是前文介绍的事件循环。它持续追踪所有的协程并执行它们。

协程的另外一些重要特性如下：

- 协程可以有多个入口点，并可以yield多次
- 协程可以将执行权交给其他协程

yield表示协程在此暂停，并且将执行权交给其他协程。因为协程可以将值与控制权一起传递给另一个协程，所以“yield一个值”就表示将值传给下一个执行的协程。

|ready|
-------

使用Asyncio定义协程非常简单，只需要一个装饰器即可： ::

        import asyncio

        @asyncio.coroutine
        def coroutine_function(function_arguments):
            # DO_SOMETHING

|how|
-----

在这个例子中，我们将看到如何使用Asyncio的协程来模拟有限状态机。有限状态机(finite state machine or automaton, FSA)是一个数学模型，不仅在工程领域应用广泛，在科学领域也很著名，例如数学和计算机科学等。我们要模拟的状态机如下图所示：

.. image:: ../images/finite-state-machine.png

在上图中，可以看到我们的系统有 **S1**, **S2**, **S3**, **S4** 四个状态, **0** 和 **1** 是状态机可以从一个状态到另一个状态的值（这个过程叫做转换）。例如在本实验中，只有当只为1的时候， **S0** 可以转换到 **S1** ，当只为0的时候， **S0** 可以转换到 **S2** .Python代码如下，状态模拟从 **S0** 开始，叫做 **初始状态** ，最后到 **S4** ，叫做 **结束状态** 。 ::

        # Asyncio Finite State Machine
        import asyncio
        import time
        from random import randint


        @asyncio.coroutine
        def StartState():
            print("Start State called \n")
            input_value = randint(0, 1)
            time.sleep(1)
            if (input_value == 0):
                result = yield from State2(input_value)
            else:
                result = yield from State1(input_value)
            print("Resume of the Transition : \nStart State calling " + result)

        @asyncio.coroutine
        def State1(transition_value):
            outputValue =  str("State 1 with transition value = %s \n" % transition_value)
            input_value = randint(0, 1)
            time.sleep(1)
            print("...Evaluating...")
            if input_value == 0:
                result = yield from State3(input_value)
            else :
                result = yield from State2(input_value)
            result = "State 1 calling " + result
            return outputValue + str(result)

        @asyncio.coroutine
        def State2(transition_value):
            outputValue =  str("State 2 with transition value = %s \n" % transition_value)
            input_value = randint(0, 1)
            time.sleep(1)
            print("...Evaluating...")
            if (input_value == 0):
                result = yield from State1(input_value)
            else :
                result = yield from State3(input_value)
            result = "State 2 calling " + result
            return outputValue + str(result)

        @asyncio.coroutine
        def State3(transition_value):
            outputValue = str("State 3 with transition value = %s \n" % transition_value)
            input_value = randint(0, 1)
            time.sleep(1)
            print("...Evaluating...")
            if (input_value == 0):
                result = yield from State1(input_value)
            else :
                result = yield from EndState(input_value)
            result = "State 3 calling " + result
            return outputValue + str(result)

        @asyncio.coroutine
        def EndState(transition_value):
            outputValue = str("End State with transition value = %s \n" % transition_value)
            print("...Stop Computation...")
            return outputValue

        if __name__ == "__main__":
            print("Finite State Machine simulation with Asyncio Coroutine")
            loop = asyncio.get_event_loop()
            loop.run_until_complete(StartState())

运行代码，我们可以看到类似以下输出（译注，运行结果随机，这里为译者运行的三次结果）. ::

		$ python3 coroutines.py
		Finite State Machine simulation with Asyncio Coroutine
		Start State called

		...Evaluating...
		...Evaluating...
		...Evaluating...
		...Evaluating...
		...Evaluating...
		...Evaluating...
		...Stop Computation...
		Resume of the Transition :
		Start State calling State 2 with transition value = 0
		State 2 calling State 1 with transition value = 0
		State 1 calling State 2 with transition value = 1
		State 2 calling State 1 with transition value = 0
		State 1 calling State 2 with transition value = 1
		State 2 calling State 3 with transition value = 1
		State 3 calling End State with transition value = 1

		$ python3 coroutines.py
		Finite State Machine simulation with Asyncio Coroutine
		Start State called

		...Evaluating...
		...Evaluating...
		...Stop Computation...
		Resume of the Transition :
		Start State calling State 2 with transition value = 0
		State 2 calling State 3 with transition value = 1
		State 3 calling End State with transition value = 1

		$ python3 coroutines.py
		Finite State Machine simulation with Asyncio Coroutine
		Start State called

		...Evaluating...
		...Evaluating...
		...Evaluating...
		...Evaluating...
		...Evaluating...
		...Evaluating...
		...Evaluating...
		...Stop Computation...
		Resume of the Transition :
		Start State calling State 1 with transition value = 1
		State 1 calling State 2 with transition value = 1
		State 2 calling State 1 with transition value = 0
		State 1 calling State 3 with transition value = 0
		State 3 calling State 1 with transition value = 0
		State 1 calling State 2 with transition value = 1
		State 2 calling State 3 with transition value = 1
		State 3 calling End State with transition value = 1 

|work|
------

每一个状态都由装饰器装饰： ::

    @asyncio.coroutine

例如， **S0** 的定义如下所示： ::

        @asyncio.coroutine
        def StartState():
            print("Start State called \n")
            input_value = randint(0, 1)
            time.sleep(1)
            if (input_value == 0):
                result = yield from State2(input_value)
            else:
                result = yield from State1(input_value)
            print("Resume of the Transition : \nStart State calling " + result)

通过 ``random`` 模块的 ``randint(0, 1)`` 函数生成了 ``input_value`` 的值，决定了下一个转换状态。此函数随机生成1或0： ::

    input_value = randint(0, 1)

得到 ``input_value`` 的值之后，通过 ``yield from`` 命令调用下一个协程。 ::

     if (input_value == 0):
         result = yield from State2(input_value)
     else:
         result = yield from State1(input_value)

``result`` 是下一个协程返回的string，这样我们在计算的最后就可以重新构造出计算过程。

启动事件循环的代码如下： ::

        if __name__ == "__main__":
            print("Finite State Machine simulation with Asyncio Coroutine")
            loop = asyncio.get_event_loop()
            loop.run_until_complete(StartState())
