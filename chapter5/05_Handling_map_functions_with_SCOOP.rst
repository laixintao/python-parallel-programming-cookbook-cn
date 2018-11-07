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
