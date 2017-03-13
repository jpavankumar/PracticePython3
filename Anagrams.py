#!/usr/local/bin/python3.4 -tt
    
def checkForAnagram(testStr1,testStr2):
    if type(testStr1) is not str or type(testStr2) is not str :
        print("This function expects ", str, str, " but ",type(testStr1),type(testStr2)," was passed")
        return False
    
    if len(testStr1) == 0:
        print("\"",testStr1,"\"","is not a valid string")
        return False
        
    if len(testStr2) == 0:
        print("\"",testStr2,"\"","is not a valid string")
        return False
    
    import re
    testStr1New = re.sub('\W*','',testStr1).lower()
    testStr2New = re.sub('\W*','',testStr2).lower()
    
    testStr1NewSet = set(testStr1New)
    testStr2NewSet = set(testStr2New)
    
    if testStr1NewSet.issubset(testStr2NewSet) or testStr2NewSet.issubset(testStr1NewSet):
        print(testStr1,",",testStr2,"are anagrams")
        return True
    else:
        print(testStr1,",",testStr2,"are not anagrams")
        return False
    

def main():
    testStr1 = input("Enter the first string to test for Anagram:")
    testStr2 = input("Enter the second string to test for Anagram:")
    
    areTheseAnagrams = checkForAnagram(testStr1,testStr2)

if __name__ == '__main__': 
    main()