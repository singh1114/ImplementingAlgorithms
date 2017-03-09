'''
nimGame Algorithm
'''
print "Print the total number of matches\n"
matchesNumber = int(input())

whoWon(matchesNumber)

def whoWon(matchesNumber):
    # Half the number of matches
    halfMatches = int(matchesNumber/2)

    for x in range(1, halfMatches):
        matchesLeft = matchesNumber - x
        if(matchesLeft > 1):
            whoWon(matchesLeft)
        else:
            whoWon(matchesNumber)
