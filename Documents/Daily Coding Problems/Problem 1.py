

# Good morning! Here's your coding interview problem for today.
# This problem was recently asked by Google.
# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
# Bonus: Can you do this in one pass?


# inputList = [10, 15, 3, 7]
# k = 17

def check_sum_in_list(inputList,k):
    listLength = len(inputList)
    
    #These loops will create every combination of two values in the input list
    #Using list comprehensions here may be quicker for large data sets
    #However, this is more clear, and will exit early if a match is found
    for i in range(listLength):
        for j in range(i+1,listLength):
            if k == (inputList[i]+inputList[j]):
                return True
    return False

check_sum_in_list([10, 15, 3, 7],17)
check_sum_in_list([10, 15, 3, 7],19)
