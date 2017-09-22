使用Asyncio和Futures
====================

Asyncio 模块的另一个重要的组件是 ``Future`` 类。它和 ``concurrent.futures.Futures`` 很像，但是针对Asyncio的事件循环做了很多定制。 ``asyncio.Futures`` 类代表还未完成的结果（有可能是一个Exception）。所以综合来说，它是一种抽象，代表还没有做完的事情。

实际上，必须处理一些结果的回调函数被加入到了这个类的实例中。

|ready|
-------

要操作Asyncio中的 ``Future`` ，必须进行以下声明： ::

    import asyncio
    future = asyncio.Future()

基本的方法有： 

- ``cancel()``: 取消future的执行，调度回调函数
- ``result()``: 返回future代表的结果
- ``exception()``: 返回future中的Exception
- ``add_done_callback(fn)``: 添加一个回调函数，当future执行的时候会调用这个回调函数
- ``remove_done_callback(fn)``: 从“call whten done”列表中移除所有callback的实例
- ``set_result(result)``: 将future标为执行完成，并且设置result的值
- ``set_exception(exception)``: 将future标为执行完成，并设置Exception

|how|
-----



