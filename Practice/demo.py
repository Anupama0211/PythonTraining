sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
print(sampleDict["class"]["student"]["marks"]["history"])
print(sampleDict.get)
# d1 = {1: 2, 3: 4}
# d2 = {3: 5, 6: 7}


# d3={1:2, 3:[4,5], 6:7}
# learn ContextLib

def mySum(*args):
    print(type(args))
    return sum(args)


# Driver code

if __name__ == "__main__":
    print(mySum(1, 2, 3, 4, 5))
    print(mySum(10, 20))
    d1 = {1: 2, 3: 4}
    d2 = {3: 5, 6: 7}
    for k, v in d1.items():
        if k in d2:
            d2[k] = [d2[k], v]
        else:
            d2[k] = v
    print(list(d2))
    l = [('Aisha', 11), ('Aisha', 33), ('Will', 50), ('Root', 65)]
    print(sorted(l))
    m=zip([12,23,2,4,48],[22,22,222,222])
    print(list(m))
    # d3={1:2, 3:[4,5], 6:7}
    # learn ContextLib
