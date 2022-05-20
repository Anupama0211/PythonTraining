if __name__ == "__main__":
    numbers=input("Input: ")
    listOfNumbers=[int(num) for num in numbers.split(",")]
    print(listOfNumbers)
    tupleOfNumbers=tuple(listOfNumbers)
    print(tupleOfNumbers)
