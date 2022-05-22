def target_sum(list_of_numbers, result):
    dict_numbers = {}
    for number in list_of_numbers:
        target = result - number
        if target in dict_numbers:
            return [dict_numbers[target], list_of_numbers.index(number), ]
        else:
            dict_numbers[number] = list_of_numbers.index(number)


if __name__ == "__main__":
    print(target_sum([3, 2, 4], 6))
