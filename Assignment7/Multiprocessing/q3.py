"""
. Write a program to square  1, 10, 100, 1000, 10000, 100000, …, 1000000 asynchronously.
"""
import asyncio


async def square(num):
    print(num ** 2)


async def main():
    list = [10 ** i for i in range(7)]
    for i in list:
        await square(i)


asyncio.run(main())
