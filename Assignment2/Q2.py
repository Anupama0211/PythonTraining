if __name__ == "__main__":
    string =input("Input:")
    setOfWords=set(string.split())
    sortedWords=list(setOfWords)
    sortedWords.sort()
    print(" ".join(sortedWords))