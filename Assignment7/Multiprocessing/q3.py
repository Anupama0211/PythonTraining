"""
. Write a program to square  1, 10, 100, 1000, 10000, 100000, …, 1000000 asynchronously.
"""
import asyncio


async def square(num):
    print(num ** 2)


async def main():
    list_of_nums = [10 ** num for num in range(7)]
    for num in list_of_nums:
        await square(num)


asyncio.run(main())
