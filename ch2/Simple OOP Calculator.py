from typing import overload


class Calculator :

    ### Enter Your Code Here ###
    def __init__(self,x,y = None):
        self.x = x
        self.y = y

    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def __add__(self):
        return int(self.x+self.y)
        ###Enter Your Code For Add Number###

    def __sub__(self):
        return self.x-self.y
        ###Enter Your Code For Sub Number### 

    def __mul__(self):
        return self.x*self.y
        ###Enter Your Code For Mul Number###

    def __truediv__(self):
        if y != 0:
            return self.x/self.y
        else:
            return "y must not equal to 0"
        ###Enter Your Code For Div Number###

x,y = input("Enter num1 num2 : ").split(",")

x,y = Calculator(int(x)),Calculator(int(y))
x = x.getX()
y = y.getX()
print(x+y,x-y,x*y,x/y,sep="\n")
