# Jordan Gelber
# February 7, 2020
# CS 371: Algorithm Design and Analysis
# Gale-Shapely Stable Matching Implementation

# This program computes a stable matching using an implementation of the Gale-Shapely
# algorithm. The program is given a user input in the form below:
# n
# mX wA wB
# mY wB wA
# wA mY mX
# wB mY mX
# Where n is the total number of pairs and the next n lines have each man's name followed
# by n women in the man's preference order then, the next n lines have each woman's name
# followed by the woman's preference order of n men.



# This function computes and returns stable matching between men and women using a dictionary
# of each woman's preferences in a dictonary structure, a dictonary of each man's preferences
# in a stack structure, and a stack of all single men.
def stableMarriage(womenDict, menDict, singleMen):
    wPairs = {}
    mPairs = {}
    # While there are still single men, pop the top single man from the stack and pop his top prefered
    # woman from his stack. When there no single men left, return the men pairs dictionary.
    while singleMen:
        singleMan = singleMen.pop()
        woman = menDict[singleMan].pop()
        # If the woman is already engaged, fetch her fiance from the women pairs dictionary
        if woman in wPairs:
            fiance = wPairs[woman]
            # If the woman prefers the single man to her fiance, delete the unwanted pairing, pair
            # the single man and woman, and push the fiance onto the stack as the next single man.
            if int(womenDict[woman][singleMan]) < int(womenDict[woman][fiance]):
                del wPairs[woman]
                del mPairs[fiance]
                wPairs[woman] = singleMan
                mPairs[singleMan] = woman
                singleMen.append(fiance)
            # If the woman prefers her fiance to the single man, push the single man back onto the
            # stack, making him the next single man to propose to his next most-prefered woman.
            else:
                singleMen.append(singleMan)
        # If the woman is not already enganged, pair the single man and woman.
        else:
            wPairs[woman] = singleMan
            mPairs[singleMan] = woman
    return mPairs

# This function orgnizes the male input returning a dictionary of men and their preferences in a stack,
# a stack of all single men, and a list of men in order.
def inputMen(numPairs):
    singleMen = []
    menDict = {}
    # For each man in the given number of pairs, organize the input by creating a dictonary
    # of each man as the key and a stack of that man's preferences as the value.
    for i in range(numPairs):
        preferences = input().split()
        tempList = []
        # Run through each element of the preferences list.
        for j in reversed(range(len(preferences))):
            # Use the first element of the preferences list, the i-th man's name, as his dictionary key.
            if j==0:
                menDict[preferences[j]] = ""
            # For each element of the preferences list after the first, append to a temporary list.
            else:
                tempList.append(preferences[j])
        menDict[preferences[0]] = tempList
        singleMen.append(preferences[0])
        del tempList
    menOrder = singleMen.copy() # remember order of men for printing purposes
    return menDict, singleMen, menOrder

# This function orgnizes the female input returning a dictionary of women and their preferences
# as a dictionary of each man as a key and the woman's preference rank for him.
def inputWomen(numPairs):
    womenDict = {}
    # For each woman in the given number of pairs, organize the input by creating a
    # dictionary of each woman as the key and a dictionary for each man.
    for i in range(numPairs):
        pref = input().split()
        tempDict = {}
        # Run through each element of the preferences list.
        for j in range(len(pref)):
            # Use the first element of the preferences list, the i-th woman's name, as her dictionary key.
            if j==0:
                womenDict[pref[j]] = ""   # create a new dictionary key for the i-th woman
            # For each element of the preferences list after the first, create a temporary dictonary with a
            # key for every man and his rank on the woman's list as the value.
            else:
                tempDict[pref[j]] = j
        womenDict[pref[0]] = tempDict
        del tempDict
    return womenDict

# This function prints any stable pairing, such as ((m1-w1), (m2-w2)), in this form:
# m1 w1
# m2 w2
def printAnswer(stablePairs, menOrder):
    for man in menOrder:
        woman = stablePairs[man]
        print(man, woman)

# The main function of this program calls each function in order to collect the user input
# then, compute and print a stable matching of the given input.
def main():
    numPairs = int(input())
    menDict, singleMen, menOrder = inputMen(numPairs)
    womenDict = inputWomen(numPairs)
    stablePairs = stableMarriage(womenDict, menDict, singleMen)
    printAnswer(stablePairs, menOrder)

main()
