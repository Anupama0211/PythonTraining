def oddList(listOfNumbers):
    return [oddNumber*oddNumber for oddNumber in listOfNumbers if oddNumber%2!=0]

if __name__ == "__main__":
    print(oddList([1,2,3,4,5,6,7,8,9]))