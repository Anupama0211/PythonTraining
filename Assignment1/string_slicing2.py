def slice(my_data):
    print(my_data[3:])
    print(my_data[:6])
    print(my_data[12])
    print(my_data[:7:3])
    print(my_data[-1:-17])
    print(my_data[8::3])
    print(len(my_data))


if __name__ == "__main__":
    my_data = "Welcome to my blog"
    slice(my_data)
