#!/usr/local/bin/python3.4 -tt

def reverse_generator(iterList):
    if len(iterList) > 0:
        num = iterList.pop()
        yield num
    else:
        raise StopIteration()
    
def giveme(iterList):
    if True:
        print ("length is",len(iterList))
        yield iterList.pop()
        raise StopIteration
        print ("length is",len(iterList))
        yield iterList.pop()
        print ("length is",len(iterList))
        yield iterList.pop()

#print(sum(reverse_iter([1,2,3,4,5,6,7,8])))
#for num in reverse_generator([1,2,3,4,5,6,7,8]):
#    print(num,end=' ')
x = giveme([1,2,3,4,5,6,7])
print(next(x))
print(next(x))
print(next(x))
print(next(x))
