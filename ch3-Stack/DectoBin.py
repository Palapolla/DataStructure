# จงเขียนโปรแกรมโดยใช้ stack เพื่อรับตัวเลขฐาน 10 แล้วเปลี่ยนเป็นเลขฐาน 2 แล้วให้แสดงผลดังตัวอย่าง

# class Stack :

#     ### Enter Your Code Here ###

# def dec2bin(decnum):

#     s = Stack()

#     ### Enter Your Code Here ###

# print(" ***Decimal to Binary use Stack***")

# token = input("Enter decimal number : ")

# print("Binary number : ",end='')

# print(dec2bin(int(token)))



class Stack:
    """ class Stack 
        default : empty stack / Stack([...])
    """
    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def __str__(self):
        s = ''
        if self.isEmpty():
            return s+"Empty"
        else:
            for ele in self.items[::-1]:
                s += str(ele)
            return s
    def push(self, i):
        self.items.append(i)

    def pop(self):
        self.items.pop()

    def peek(self):
        return self.items[-1]

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

def dec2bin(decnum):

    if decnum >=1:
        s.push(decnum%2)
        dec2bin(decnum//2)
    return s

        

s = Stack()
print(" ***Decimal to Binary use Stack***")

token = input("Enter decimal number : ")

print("Binary number : ",end='')

print(dec2bin(int(token)))