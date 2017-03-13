#!/usr/local/bin/python3.4 -tt
    
'''
given a array return index at which sum of all elements to the left is same as sum of all elements to right

ex: [5,7,6,1,9,3,6]
in this array at index=3 (value 1), sumof all elements to its left (5+7+6)  = sum of all elements to its right (9+3+6) = 18

'''

import sys

def returnBalencedIndex(testList):
    if not testList:
        return -1

    if not isinstance(testList, list):
        return -1
    
    try:
        testList = [ int(num) for num in testList]
    except ValueError as e:
        print("input list accepts only integers...")
        sys.exit()
    
    leftSum = 0
    rightSum = sum(testList[1:])
    
    for i in range(len(testList)):
        print('index = ', i, 'leftsum = ',leftSum, 'rightsum = ', rightSum)
        if leftSum == rightSum:
            return i
        leftSum += testList[i]
        rightSum = sum(testList[i+2:])

    return -1

def main():
    testList = input("Enter the list of numbers separated by a space:").split()
    print(returnBalencedIndex(testList),"is the balenced index")

if __name__ == '__main__': 
    main()