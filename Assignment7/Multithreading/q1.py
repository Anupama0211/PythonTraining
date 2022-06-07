"""
1.	For below given functions and the list ‘ar’ write a program using multithreading which will give following output.
Output:
Square is :  1
Square is :  4
Square is :  9
Cube is :  1
Cube is :  8
Cube is :  27

"""

import time
from threading import Thread


def square(num):
    for n in num:
        time.sleep(1)
        print(' Square is : ', n * n)


def cube(nums):
    for num in nums:
        time.sleep(1)
        print(" Cube is : ", num * num * num)


ar = [1, 2, 3]

square_thread = Thread(target=square, args=(ar,))
cube_thread = Thread(target=cube, args=(ar,))

square_thread.start()
square_thread.join()

cube_thread.start()
cube_thread.join()
