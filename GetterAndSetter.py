#!/usr/local/bin/python3.4 -tt

class P(object):
    def __init__(self,x):
        print("inside init")
        self.x = x
         
    @property
    def x(self):
        print("inside x getter")
        return self.__x
   
    @x.setter
    def x(self, x):
        print("inside x setter")
        if x < 0:
            self.__x = 0
        else:
            self.__x = x

p1 = P(1001)
p1.x = 10
print(p1.x)