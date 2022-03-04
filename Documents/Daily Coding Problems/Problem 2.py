import timeit
import numpy as np
# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
# Follow-up: what if you can't use division?

inputList = [1, 2, 3, 4, 5]

#This answer uses no outside libraries such as numpy
#I avoided using division based on the follow up question
def method1(inputList):
    outputArray = [1]*len(inputList)
    for x in range(len(inputList)):
        for y in range(len(inputList)):
            if x!=y:
                outputArray[x]*=inputList[y]
    return outputArray


#This answer uses numpy
def method2(inputList):
    inputArray = np.array(inputList)
    outputArray = np.ones(len(inputArray),int)
    for x in range(len(inputArray)):
        #Calculate the product of all values except the one at index x
        outputArray[x] = np.product(inputArray[np.array(range(len(inputArray)))!=x])
    return outputArray

#This code checks the runtimes of the 2 methods

testcode1 = ''' 
def test(): 
    method1(inputList)
'''
testcode2 = ''' 
def test(): 
    method2(inputList)
'''
import_module = "import numpy as np"

print('Runtime method 1',timeit.timeit(stmt=testcode1))
print('Runtime method 2',timeit.timeit(stmt=testcode2, setup=import_module))
