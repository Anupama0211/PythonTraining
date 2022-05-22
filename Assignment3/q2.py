"""
Use map() to get True for each value greater than 10 in a list of integers, else False
•	[1,2,34,2,56] => [False, False, True, False, True]
"""

if __name__ == "__main__":
    print(list(map(lambda num: num > 10, [1, 2, 34, 2, 56])))
