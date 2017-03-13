#!/usr/local/bin/python3.4 -tt
        
def checkForPalindrome(testStr):
    if type(testStr) is not str:
        print("This function expects ", str," but ",type(testStr)," was passed")
        return False
    
    if len(testStr) == 0:
        print("\"",testStr,"\"","is not a palindrome")
        return False
        
    if len(testStr) == 1:
        print(testStr,"is a palindrome")
        return True
    
    i = 0
    j = len(testStr)-1
    
    while i <= j:
        if testStr[i] != testStr[j]:
            break
        i += 1
        j -= 1
    else:
        print("{} is a palindrome".format(testStr))
        return True
    print("{} is not a palindrome".format(testStr))
    return False
    
def main():
    testStr = input("Enter the string to test for palindrome:")
    isPalindeome = checkForPalindrome(testStr)

if __name__ == '__main__': 
    main()