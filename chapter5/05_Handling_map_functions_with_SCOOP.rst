通过 SCOOP 使用 map 函数
========================

当处理 list 或其他类型的序列时，一种很常用的操作是对序列中的每一个元素都执行相同的操作，然后收集结果。举例说，通过 Python IDLE 可以对一个 list 这样更新： ::

   >>>items = [1,2,3,4,5,6,7,8,9,10]
   >>>updated_items = []
   >>>for x in items:
   >>>    updated_items.append(x*2)
   >>> updated_items
   >>>  [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

这是比较常见的一个操作，但是 Python 内置了一些功能可以更优雅地完成类似操作。

Python 的函数 ``map(aFunction, aSequence)`` 将在序列的每一个元素上调用传入的函数，并将结果以 list 的形式返回。用这个函数完成上面的操作： ::

   >>>items = [1,2,3,4,5,6,7,8,9,10]
   >>>def multiplyFor2(x):return x*2
   >>>print(list(map(multiplyFor2,items)))
   >>>[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

这里，我们将自定义的 ``multiplyFor2`` 函数传给 ``map`` . 它将对 ``items`` 中所有的元素执行此函数，最后以 list 的形式返回结果。

我们也可以将 lambda 函数（不用绑定变量名的匿名函数）当做参数传给 ``map`` 函数。这段代码就变成以下这样: ::

   >>>items = [1,2,3,4,5,6,7,8,9,10]
   >>>print(list(map(lambda x:x*2,items)))
   >>>[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

内置的 map 函数比手动写 for 循环的性能更高。

|ready|
-------


