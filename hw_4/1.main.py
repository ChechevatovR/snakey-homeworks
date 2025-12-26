from multiprocessing import Process
from threading import Thread
from time import time

def fib(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


n_workers = 10
n_fib = 35

def timed(function):
    def wrapper(*args, **kwargs):
        start = time()
        result = function(*args, **kwargs)
        end = time()
        print(f"{function.__name__} took {end - start} seconds")
        return result
    return wrapper

@timed
def test_sync():
    for i in range(n_workers):
        fib(n_fib)

@timed
def test_threads():
    workers = [Thread(target=fib, args=(n_fib, )) for i in range(n_workers)]
    for worker in workers:
        worker.start()
    for worker in workers:
        worker.join()

@timed
def test_processes():
    workers = [Process(target=fib, args=(n_fib, )) for i in range(n_workers)]
    for worker in workers:
        worker.start()
    for worker in workers:
        worker.join()

if __name__ == '__main__':
    test_sync()
    test_threads()
    test_processes()