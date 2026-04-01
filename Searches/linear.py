#Iterates an array of data looking for a target
#Assumptions: integer data, no duplicated, unsorted, amount of data determined in main
#In the worst case, touches EVERY item in the array 
#Linear time algorithm - O(n)
#The work grows in proportion to the size of the input, n
def linear_search(data, n, target):
    #---work done by these two lines is constant--#
    #---no matter how big or small n is---#
    result = False 
    index = 0  

    #--the work done by the loop increases as n increases--#
    while index < n:
        if data[index] == target:
            result = True
            index = n + 1
        index += 1


    return result  #constant time op

def main():
    data_array = [10,8,4,1,22]
    target = 40
    n = len(data_array)

    is_found = linear_search(data_array, n, target)

    if is_found:
        print("The target was found in the data.")
    else:
        print("The target was not found in the data.")


main()