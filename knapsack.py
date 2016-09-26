# Create a list that contain all the elements that want to be in the knapsack
elementweight = []
elementvalues = []
finalresultdict = {}
finalresultlist = []

# Now ask about how many elements are going to be in elements
totalnumber = int(raw_input())

# Take the weights and values in a list
for x in range(totalnumber):
    i = raw_input("Enter the weigth of "+str(x+1)+"th element : ")
    j = raw_input("Enter the value of "+str(x+1)+"th element : ")
    elementweight.insert(x, int(i))
    elementvalues.insert(x, int(j))

# Take the total weight of knapsack
i = int(raw_input("Enter the total weigth of knapsack : "))
knapsackweight = i

# Now ask from the user in which way he want to put element in the knapsack
print("Choose any one : ")
print("1. In order of values")
print("2. In order of weight")
print("3. In order of values/weight")

i = int(raw_input())

def findmaxvalue(elementvalues):
    # Initialize the maxvalue to first element
    # maxvalue = highest value in the elementvalues list
    maxvalue = elementvalues[0]

    # Initialize the maxindex to zero
    # maxindex = index of highest value in the elementvalues list
    maxindex = 0

    # For all the indexes in elementvalues list
    for x in range(len(elementvalues)):
        # If the next element( first element) is greater
        # then change the value of maxvalue and update the maxindex
        # x != 0 is used to reduce one test case i.e. when x = 0
        if(elementvalues[x] > maxvalue and x != 0):
            maxvalue = elementvalues[x]
            maxindex = x
    return maxindex

def findminweight(elementweight):
    minweight = elementweight[0]
    minindex = 0
    for x in range(len(elementweight)):
        if(elementweight[x] < minweight and x != 0):
            minweight = elementweight[x]
            minindex = x

    return minindex

# if the user wants to put the elements using the values
if(i == 1):
    # For all the elements in elementvalues
    for x in range(totalnumber):
        # Find the max. value in the elementvalues list
        maxindex = findmaxvalue(elementvalues)

        if(knapsackweight > elementweight[maxindex]):
            # Now we can add the element to the final result dictionary
            finalresultdict.update({'weight': elementweight[maxindex], \
            'value': elementvalues[maxindex]},)

            # Now put the created dictionary into a list for permanent saving.
            finalresultlist.insert(x, dict(finalresultdict))

            # Update the value of knapsack weight
            knapsackweight = knapsackweight - elementweight[maxindex]

            # Now remove the elements from the real arrays
            del elementweight[maxindex]
            del elementvalues[maxindex]

        else:
            break

    print(finalresultlist)

# else ifuser wants to put the elements according to the weight
elif(i == 2):
    # For all the elements in the element list
    for x in range(totalnumber):
        # Find the min. weight in the elementweight list
        minindex = findminweight(elementweight)

        if(knapsackweight > elementweight[minindex]):
            finalresultdict.update({'weight': elementweight[minindex], \
            'value': elementvalues[minindex]},)

            finalresultlist.insert(x, dict(finalresultdict))

            knapsackweight = knapsackweight - elementweight[minindex]

            del elementweight[minindex]
            del elementvalues[minindex]

        else:
            break

    print(finalresultlist)
