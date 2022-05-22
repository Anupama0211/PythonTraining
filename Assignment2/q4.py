def odd_list(list_of_numbers):
    return [oddNumber * oddNumber for oddNumber in list_of_numbers if oddNumber % 2 != 0]


if __name__ == "__main__":
    print(odd_list([1, 2, 3, 4, 5, 6, 7, 8, 9]))
