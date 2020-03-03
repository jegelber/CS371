# Runtime: O(nlogn)
def sortAndCount(L):
    # Base Case: If the length of the list is 1, there are no
    # inversions, return 0 inversions and the list.
    if len(L) == 1:
        return (0, L)
    # Else, the list is longer than 1.
    else:
        # Split the list into two equal parts. A being the first
        # half and B being the second.
        A = L[:len(L)//2]
        B = L[len(L)//2:]
        # Recursively run the function on each part of the list,
        # returning the number of inversions in each part and
        # the sorted list.
        (invA, A) = sortAndCount(A)
        (invB, B) = sortAndCount(B)
        # Merge the two sorted lists using the mergeAndCount function,
        # returning the number of inversions and merged list.
        (inv, L) = mergeAndCount(A, B)
        # Return the total number of inversions and the merged, sorted list.
        return (invA + invB + inv, L)

# mergeAndCount sorts lists A and B and returns the number of inversions
# in the lists and the lists merged into one list.
# Runtime: O(n)
def mergeAndCount(A, B):
    # Initialize the empty mergedList return list to empty.
    mergedList = []
    # Initialize the inversion count and list pointers to 0.
    # i points to the current place in A, while j points
    # to the current place in B.
    invCount = 0
    i = 0
    j = 0
    # While the pointers have not reached the end of either list.
    while i < len(A) and j < len(B):
        # If the smaller current element is in B, append the element to the
        # return list, add the number elements in A that have not yet been
        # incremented to the inversion count, and increment j.
        if B[j] < A[i]:
            mergedList.append(B[j])
            invCount += len(A)-i
            j+=1
        # Else, the smaller current element is in A, append the element to the
        # return list and increment i.
        else:
            mergedList.append(A[i])
            i+=1
    # If i has not reached the end of A, append the rest of A
    # to the return list.
    if i != len(A):
        mergedList.extend(A[i:])
    # Else j has not reached the end of B, append the rest of
    # B to the return list.
    else:
        mergedList.extend(B[j:])
    # Return the final inversion count and merged list.
    return (invCount, mergedList)

# Runs the sortAndCount funtion on the user's inputed
# list. Make sure to run program with python3 to
# ensure the input function works correctly.
def main():
    # Initialize the empty input list.
    inputList = []
    # Read in the number of elements in the list as well
    # as the list of integers.
    n = int(input())
    inputList = list(map(int, input().rstrip().split()))
    # Calculate the number of inversions and sorted list.
    inversions, sortedList = sortAndCount(inputList)
    # Print the number of inversions.
    print(inversions)

# Run main.
main()
