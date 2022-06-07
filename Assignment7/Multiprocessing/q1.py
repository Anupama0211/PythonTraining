"""
Q1. Spawn 50 processes for 1 to 50, and cube  each no. in incremental  order using Queue
Expected output :
1
8
64
…
"""
from multiprocessing import Queue, Process


def cube(x, queue):
    queue.put(x * x * x)


if __name__ == "__main__":
    queue = Queue()

    processes = []
    for i in range(1, 51):
        process = Process(target=cube, args=(i, queue))
        process.start()
        process.join()

    while queue:
        print(queue.get())
