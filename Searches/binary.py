#Note: code is overly commented for the sake of learning
#Assumptions: integer data, no duplicates, sorted in ascending order, amount of data determined in main
#Logarithmic time algorithm - O(lg n), thanks to Interval Halving at each iteration 
#Throwing out half the data each iteration means we iterate through the loop lg n time in the worst case
#Worst case: target is not in the data, O(lg n)
#Best case: target is found in the data at the first value mid points to, Big Omega(1) - constant time



#Iterative Binary Search - to be used on sorted data
def binary_search(data, n, target):
    low = 0 #begining index of the data array
    high = n-1 #end of the data array
    #---together, low and high define the boundaries of the search space--#

    while low <= high:
        mid = (low + high) // 2 #find the middle
        #examine the value stored there
        if data[mid] == target:
            #target is the value mid points to
            return True
        if data[mid] > target:
            #target is smaller, and must be in the left half of the data
            high = mid - 1 #move the high pointer to hone in on the left half
            #--the next time through the loop, the search space is half as big--#
        if data[mid] < target:
            #target is larger, and must be in the right half of the data
            low = mid + 1 #move the low pointer to hone in on the right half
            #--the next time through the loop, the search space is half as big--#

    return False #all data has been processed, and the target not found

def main():
    data = [1, 3, 5, 8, 9, 11, 13, 15, 22, 40]
    n = len(data)
    target = 10

    is_found = binary_search(data, n, target)

    if is_found:
        print("The target was found in the data.")
    else:
        print("The target was not found in the data.")


main()



