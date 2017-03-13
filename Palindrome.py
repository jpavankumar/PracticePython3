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
    
    reverseTestStr = testStr[::-1]
    if testStr == reverseTestStr:
        print(testStr,"is a palindrome")
    else:
        print(testStr,"is not a palindrome")
        
def checkForPalindromeEx1(testStr):
    if type(testStr) is not str:
        print("This function expects ", str," but ",type(testStr)," was passed")
        return False
    
    if len(testStr) == 0:
        print("\"",testStr,"\"","is not a palindrome")
        return False
        
    if len(testStr) == 1:
        print(testStr,"is a palindrome")
        return True
    
    import re
    testStrNew = re.sub('\W*','',testStr)
    reverseTestStr = testStrNew[::-1]
    if testStrNew == reverseTestStr:
        print(testStr,"is a palindrome")
    else:
        print(testStr,"is not a palindrome")
        
def checkForPalindromeEx2(testStr):
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
    j = len(testStr) - 1
    while ( i <= j ):
        #print("i is",i,"j is",j)
        if not testStr[i].isalpha():
            i += 1
            continue
        
        if not testStr[j].isalpha():
            j -= 1
            continue
        
        if testStr[i] != testStr[i]:
            print(testStr,"is not a palindrome")
            return False
        i += 1
        j -= 1
        
    print(testStr,"is a palindrome")
    return True
    
def main():
    testStr = input("Enter the string to test for palindrome:")
    isPalindeome = checkForPalindromeEx2(testStr)

if __name__ == '__main__': 
    main()