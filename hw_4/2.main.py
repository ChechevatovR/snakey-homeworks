import math
from time import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, Executor

def timed(function):
    def wrapper(*args, **kwargs):
        start = time()
        result = function(*args, **kwargs)
        end = time()
        print(f"{function.__name__}({args} {kwargs}) took {end - start} seconds")
        return result
    return wrapper

def integrate_trapesoid(f, a, step, i: int):
    return f(a + i * step) * step

def integrate(f, a, b, *, n_jobs=1, n_iter=100000, pool_class=Executor):
    pool = pool_class(n_jobs)
    step = (b - a) / n_iter
    result = pool.map(integrate_trapesoid, [f] * n_iter, [a] * n_iter, [step] * n_iter, range(n_iter))
    return sum(result)

@timed
def test_thread(n_jobs: int):
    integrate(math.cos, 0, math.pi / 2, n_jobs=n_jobs, pool_class=ThreadPoolExecutor)

@timed
def test_process(n_jobs: int):
    integrate(math.cos, 0, math.pi / 2, n_jobs=n_jobs, pool_class=ProcessPoolExecutor)

if __name__ == '__main__':
    for n_jobs in [1, 2, 4, 8, 16, 32]:
        test_thread(n_jobs)
        test_process(n_jobs)
