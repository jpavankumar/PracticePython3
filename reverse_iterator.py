#!/usr/local/bin/python3.4 -tt

class reverse_iter:
    def __init__(self,iterList):
        self.iterList = iterList
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if len(self.iterList) > 0:
            num = self.iterList.pop()
            return num
        else:
            raise StopIteration()

#print(sum(reverse_iter([1,2,3,4,5,6,7,8])))
for num in reverse_iter([1,2,3,4,5,6,7,8]):
    print(num,end=' ')