#!/usr/local/bin/python3.4 -tt

class fibonacci:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.a < 10000:
            self.a , self.b = self.b , self.a + self.b
            return self.a
        else:
            raise StopIteration()

f = fibonacci(1,10)
for num in f:
    print(num,end=' ')