numberList = [4]

def insertionSort():
    newNumber = int(input())
    if (newNumber == 0):
        return
    length = len(numberList)
    for x in range(0, length):
        position = length - x
        if (newNumber > numberList[position-1]):
            numberList.insert(position, newNumber)
            print numberList
            break

        else:
            numberList.insert(position, numberList[position-1])
            numberList[position - 1] = newNumber

    insertionSort()
insertionSort()
print numberList
