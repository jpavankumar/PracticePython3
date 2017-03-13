#!/usr/local/bin/python3.4 -tt
    
dictOfParentheses = {
                        '}' : '{',
                        ')' : '(',
                        ']' : '[',
                        '>' : '<',
                    }

def isBalenced(testStr):
    if not testStr:
        return True
    
    listOfSymbols = []
    for ch in testStr:
        if ch in dictOfParentheses.values():
            listOfSymbols.append(ch)
        elif ch in dictOfParentheses.keys():
             lastCh = listOfSymbols.pop()
             if lastCh != dictOfParentheses.get(ch):
                 return False
    
    if len(listOfSymbols) != 0:
        return False
    
    return True

def main():
    testStr = input("Enter the string to test for balanced parentheses:")
    if isBalenced(testStr):
        print(testStr,"have balanced parentheses")
    else:
        print(testStr,"doesn't have balanced parentheses")

if __name__ == '__main__': 
    main()