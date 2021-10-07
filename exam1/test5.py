# ให้สร้าง class Rational เพื่อรันแล้วได้ผลลัพธ์ตามตัวอย่าง

# แก้ไข code ภายใน class Rational เท่านั้น

# class Rational:
    
# print(" *** Rational Calculator ***")
# print(" *        A = n1/d1        *")
# print(" *        B = n2/d2        *")
# print(" ***************************\n")
                        
# str_input = input("Enter n1 d1 n2 d2 : ")
# n1, d1, n2, d2 = [int(e) for e in str_input.split()]
# A = Rational(n1,d1)     # A = n1/d1
# B = Rational(n2,d2)     # B = n2/d2
# C = Rational()          # C = 1/1      
# print("A=",A,"B=",B)        # method __str__
# print("A < B ==> ",A<B)     # method __lt__
# print("A > B ==> ",A>B)     # method __gt__
# print("A <= B ==> ",A<=B)   # method __ge__
# print("A >= B ==> ",A>=B)   # method __ge__
# print("A == B ==> ",A==B)   # method __eq__
# print("A != B ==> ",A!=B)   # method __ne__
# print("A + B ==> ",A+B)     # method __add__
# print("A - B ==> ",A-B)     # method __sub__
# print("A * B ==> ",A*B)     # method __mul__
# print("A / B ==> ",A/B)     # method __truediv__
# print("A // B ==> ",A//B)     # method __floordiv__
# print("A + C ==> ",A+C)  

# ห้าม import library ใดๆ

#  *** Rational Calculator ***
#  *        A = n1/d1        *
#  *        B = n2/d2        *
#  ***************************

# Enter n1 d1 n2 d2 : 1 2 1 3
# A =  1/2 	B=  1/3 	C =  1
# A < B ==>  FALSE
# A > B ==>  TRUE
# A <= B ==>  FALSE
# A >= B ==>  TRUE
# A == B ==>  FALSE
# A != B ==>  TRUE
# A + B ==>  5/6
# A - B ==>  1/6
# A * B ==>  1/6
# A / B ==>  3/2
# A // B ==>  1
# A + C ==>  3/2


#  *** Rational Calculator ***
#  *        A = n1/d1        *
#  *        B = n2/d2        *
#  ***************************

# Enter n1 d1 n2 d2 : 2 4 1 3
# A =  2/4 	B=  1/3 	C =  1
# A < B ==>  FALSE
# A > B ==>  TRUE
# A <= B ==>  FALSE
# A >= B ==>  TRUE
# A == B ==>  FALSE
# A != B ==>  TRUE
# A + B ==>  5/6
# A - B ==>  1/6
# A * B ==>  1/6
# A / B ==>  3/2
# A // B ==>  1
# A + C ==>  3/2

#  *** Rational Calculator ***
#  *        A = n1/d1        *
#  *        B = n2/d2        *
#  ***************************

# Enter n1 d1 n2 d2 : 15 20 35 40
# A =  15/20 	B=  35/40 	C =  1
# A < B ==>  TRUE
# A > B ==>  FALSE
# A <= B ==>  TRUE
# A >= B ==>  FALSE
# A == B ==>  FALSE
# A != B ==>  TRUE
# A + B ==>  13/8
# A - B ==>  -1/8
# A * B ==>  21/32
# A / B ==>  6/7
# A // B ==>  0
# A + C ==>  7/4



class Rational:
    def __init__(self,n=None,d=None):
        if n == None:
            self.n = 1
        if d == None:
            self.d = 1
        else:
            self.n = n
            self.d = d
    
    def __str__(self):
        if self.n==self.d:
            return '1'
        return str(self.n)+'/'+str(self.d)

    def divide(self):
        if self.n==self.d:
            return 1
        else:
            return self.n/self.d

    def __lt__(self,other):
        return str(self.divide() < other.divide()).upper()

    def __gt__(self,other):
        return str(self.divide() > other.divide()).upper()

    def __le__(self,other):
        return str(self.divide() <= other.divide()).upper()

    def __ge__(self,other):
        return str(self.divide() >+ other.divide()).upper()

    def __eq__(self, other):
        return str(self.divide() == other.divide()).upper()
    
    def __ne__(self, other):
        return str(self.divide() != other.divide()).upper()
    
    def __add__(self,other):
        ans = (self.n*other.d +self.d*other.n)
        ans2 = self.d*other.d
        if isinstance(self.divide(), int) and isinstance(other.divide(),int):
            return self.divide()+other.divide()
        elif ans%ans2 == 0:
            return str(int(ans/ans2))
        else:
            return str(ans)+'/'+str(ans2)
    
    def __sub__(self,other):
        ans = (self.n*other.d -self.d*other.n)
        ans2 = self.d*other.d
        if isinstance(self.divide(), int) and isinstance(other.divide(),int):
            return self.divide()-other.divide()
        elif ans%ans2 == 0:
            return str(int(ans/ans2))
        else:
            return str(ans)+'/'+str(ans2)
    
    def __mul__(self,other):
        ans = (self.n*other.n)
        ans2 = self.d*other.d
        if isinstance(self.divide(), int) and isinstance(other.divide(),int):
            return self.divide()*other.divide()
        elif ans%ans2 == 0:
            return str(int(ans/ans2))
        else:
            return str(ans)+'/'+str(ans2)
    
    def __truediv__(self,other):
        ans = (self.n*other.d)
        ans2 = self.d*other.n
        if isinstance(self.divide(), int) and isinstance(other.divide(),int):
            return self.divide()/other.divide()
        elif ans%ans2 == 0:
            return str(int(ans/ans2))
        else:
            return str(ans)+'/'+str(ans2)

    def __floordiv__(self,other):
        return int(self.divide()//other.divide())

    
print(" *** Rational Calculator ***")
print(" *        A = n1/d1        *")
print(" *        B = n2/d2        *")
print(" ***************************\n")
                        
str_input = input("Enter n1 d1 n2 d2 : ")
n1, d1, n2, d2 = [int(e) for e in str_input.split()]
A = Rational(n1,d1)     # A = n1/d1
B = Rational(n2,d2)     # B = n2/d2
C = Rational() 
# A = A.divide()
# B = B.divide()   
# C = C.divide()      # C = 1/1      
print("A = ",A,"        B= ",B,"        C = ",C)        # method __str__
print("A < B ==> ",A<B)     # method __lt__
print("A > B ==> ",A>B)     # method __gt__
print("A <= B ==> ",A<=B)   # method __ge__
print("A >= B ==> ",A>=B)   # method __ge__
print("A == B ==> ",A==B)   # method __eq__
print("A != B ==> ",A!=B)   # method __ne__
print("A + B ==> ",A+B)     # method __add__
print("A - B ==> ",A-B)     # method __sub__
print("A * B ==> ",A*B)     # method __mul__
print("A / B ==> ",A/B)     # method __truediv__
print("A // B ==> ",A//B)     # method __floordiv__
print("A + C ==> ",A+C)        