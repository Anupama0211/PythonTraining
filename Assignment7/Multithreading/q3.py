"""
Below program represent a race condition. Use Locks to avoid race condition and get final counter value as 30.
Output:
counter=10
counter=30
The final counter is 30
"""
import threading
from time import sleep

counter = 0

lock = threading.Lock()


def increase(by):
    global counter
    with lock:
        local_counter = counter
        local_counter += by
        sleep(0.1)
        counter = local_counter
        print(f'counter={counter}')


thread1 = threading.Thread(target=increase, args=(10,))
thread2 = threading.Thread(target=increase, args=(20,))

t1.start()
t2.start()

t1.join()
t2.join()

print(f'The final counter is {counter}')
