"""
Create function accepts arbitrary number of keyword arguments and return dictionary with keys and values swapped as
shown below
•	get_values(a=1, b=2, e=3) => {1:'a', 2:'b', 3:'e'}
•	get_values(a=1, b=2) => {1:'a', 2:'b'} """


def get_values(**kwargs) -> dict[int, str]:
    return {value: key for key, value in kwargs.items()}


if __name__ == "__main__":
    print(get_values(a=1, b=2, e=3))
    print(get_values(a=1, b=2))
