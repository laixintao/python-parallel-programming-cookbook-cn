# -*- coding: utf-8 -*-

""" Concurrent.Futures Pooling - Chapter 4 Asynchronous Programming """

import concurrent.futures
import time
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def evaluate_item(x):
    # 计算总和，这里只是为了消耗时间
    result_item = count(x)
    # 打印输入和输出结果
    print ("item " + str(x) + " result " + str(result_item))

def  count(number) :
    for i in range(0, 10000000):
    	i=i+1
    return i * number

if __name__ == "__main__":
    # 顺序执行
    start_time = time.clock()
    for item in number_list:
    	evaluate_item(item)
    print("Sequential execution in " + str(time.clock() - start_time), "seconds")
    # 线程池执行
    start_time_1 = time.clock()
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        for item in number_list:
            executor.submit(evaluate_item,  item)
    print ("Thread pool execution in " + str(time.clock() - start_time_1), "seconds")
    # 进程池
    start_time_2 = time.clock()
    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
        for item in number_list:
            executor.submit(evaluate_item,  item)
    print ("Process pool execution in " + str(time.clock() - start_time_2), "seconds")
