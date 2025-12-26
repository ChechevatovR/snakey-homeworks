import os
from multiprocessing import Process, Pipe, Queue
from time import sleep
from datetime import datetime
from codecs import encode

def log(*args, **kwargs):
    print(os.getpid(), datetime.now(), *args, **kwargs)

def a(main_to_a, a_to_b):
    log('A', 'started')
    while True:
        line = main_to_a.get()
        log('A', 'Received line', line)
        line = line.lower()
        sleep(5)
        log('A', 'Sending line', line)
        a_to_b.put(line)

def b(a_to_b, b_to_main):
    log('B', 'started')
    while True:
        line = a_to_b.get()
        log('B', 'Received line', line)
        line = encode(line, 'rot13')
        log('B', 'Sending line', line)
        b_to_main.put(line)


def main(main_to_a, b_to_main):
    while True:
        line = input()
        log('main', 'stdin line', line)
        main_to_a.put(line)
        while not b_to_main.empty():
            log('main', 'Received line', b_to_main.get())


if __name__ == '__main__':
    main_to_a = Queue()
    a_to_b = Queue()
    b_to_main = Queue()

    A = Process(target=a, args=(main_to_a, a_to_b))
    B = Process(target=b, args=(a_to_b, b_to_main))
    A.start()
    B.start()
    main(main_to_a, b_to_main)
    A.join()
    B.join()