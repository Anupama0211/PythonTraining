def targetSum(listOfNumbers,result):
    dict={}
    for number in listOfNumbers:
        target=result-number
        if(target in dict):
            return [dict[target],listOfNumbers.index(number),]
        else:
            dict[number]=listOfNumbers.index(number)





if __name__ == "__main__":
    print(targetSum([3,2,4],6))