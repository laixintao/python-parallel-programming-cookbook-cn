from multiprocessing import Pool

p = Pool(5)

def f(x):
    return x*x

p.map(f, [1, 2, 3])
