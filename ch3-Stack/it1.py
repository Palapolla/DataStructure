# ให้น้องๆเขียนโปรแกรมโดยรับ input 2 แบบ โดยใช้ STACK ในการแก้ปัญหา



# A  <value>  ให้นำ value ไปใส่ใน STACK และทำการแสดงผล Size ปัจจุบันของ STACK

# P                 ให้ทำการแสดงผลของvalueที่อยู่ท้ายสุดและindexของvalueนั้นจากนั้นทำการ Pop_Stack ถ้าหากไม่มี value อยู่ใน Stack ให้แสดงผลเป็น  -1

# *** ในตอนสุดท้ยถ้าหากใน Stack ยังมี Value อยู่ให้แสดงผลออกมา  ถ้าหากไม่มีแล้วให้แสดงคำว่า  Empty

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
        s = 'Value in Stack = '
        if self.isEmpty():
            return s+"Empty"
        else:
            for ele in self.items:
                s += str(ele)+' '
            return s
    def push(self, i):
        self.items.append(i)
        return "Add = "+str(i)+" and Size = "+str(self.size())

    def pop(self):
        if self.isEmpty():
            return -1
        else:
            s = "Pop = "+str(self.peek())+" and Index = "+str(self.size()-1)
            self.items.pop()
            return  s

    def peek(self):
        return self.items[-1]

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

s = Stack()
x = [n for n in input("Enter Input : ").split(',')]
for i in range(len(x)):
    if x[i][0] == "A":
        print(s.push(x[i][2:]))
    if x[i][0] == "P":
        print(s.pop())
print(s)

