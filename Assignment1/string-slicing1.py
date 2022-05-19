def slice(my_string):
    print(my_string[3:6])
    print(my_string[4:10])
    print(my_string)
    print(my_string[5:11])
    print(my_string[-1:-15:-1])
    print(len(my_string))

if __name__ == "__main__":
    my_string = "string slicing"
    slice(my_string)