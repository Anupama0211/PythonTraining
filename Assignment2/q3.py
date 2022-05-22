if __name__ == "__main__":
    sentence = input("Input: ")
    countUpper = 0
    countLower = 0
    for character in sentence:
        if character.isupper():
            countUpper += 1
        elif character.islower():
            countLower += 1
    print("UPPER CASE ", countUpper)
    print("LOWER CASE ", countLower)
