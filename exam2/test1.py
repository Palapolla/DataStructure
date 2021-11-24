# จงสร้างโครงสร้างข้อมูล Stack ที่มี method ดังต่อไปนี้ 

# __str__ สำหรบแสดงข้อมูลที่อยู่ใน stack

# push(data) สำหรับเก็บข้อมูล data   

# pop() สำหรับนำข้อมูลออก

# isEmpty() สำหรับตรวจสอบว่า stack ว่างไหม ถ้าว่าง ให้เป็น True

# size() สำหรับแสดงขนาดของ stack ว่ามีข้อมูลกี่ตัว

# peek() สำหรับแสดงค่าข้อมูลที่อยู่ที่อยู่บนสุด

# bottom() สำหรับแสดงค่าข้อมูลที่อยู่ล่างสุด

# โดยเมื่อป้อน 1 แล้วให้ทำงานคำสั่งต่อไปนี้ 

class Stack:
    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def __str__(self):
        s = 'Data in Stack is : '
        if self.isEmpty():
            return s+"Empty"
        else:
            for ele in self.items:
                s += str(ele)+" "
            return s
    #push to first        
    def push(self, i):
        self.items.append(i)
    #pop first out
    def pop(self):
        self.items.pop()
    #peek first one
    def peek(self):
        return self.items[-1]
    
    def bottom(self):
        return self.items[0]

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

n = int(input('Enter choice : '))
if n == 1:
    s1=Stack()
    s1.push(10)
    s1.push(20)
    print(s1)
    s1.pop()
    s1.push(30)
    print("Peek of stack :",s1.peek())
    print("Bottom of stack :",s1.bottom())

elif n == 2:
    s1 = Stack()
    s1.push(100)
    s1.push(200)
    s1.push(300)
    s1.pop()
    print(s1)
    print("Stack is Empty :",s1.isEmpty())

elif n == 3:
    s1 = Stack()
    s1.push(11)
    s1.push(22)
    s1.push(33)
    s1.pop()
    print(s1)
    print("Stack size :",s1.size())