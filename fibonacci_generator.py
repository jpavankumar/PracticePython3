#!/usr/local/bin/python3.4 -tt

def fibonacci(a,b):
    while(True):
        a, b = b , a + b
        yield a


f = fibonacci(1,10)
for num in f:
    if ( num > 10000 ):
        break
    print(num,end=' ')