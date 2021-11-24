# จงสร้าง class Queue โดยใช้ linkedlist หรือ list หรือ deque แล้วเขียน method ต่อไปนี้ให้สมบูรณ์ และทำงานตามตัวอย่างได้
        
#     __str__():  ใช้สำหรับแสดงข้อมูล
     
#     __len__():  ใช้สำหรับบอกจำนวนสมาชิกข

#     enQueue(data):  ใช้สำหรับเพิ่มข้อมูลเข้าคิว
    
#     deQueue():  ใช้สำหรับนำข้อมูลออกจากคิว
    
#     isEmpty():  ตรวจสอบว่าคิวว่างหรือไม่ ถ้าว่าจะแสดงค่า True ถ้าไม่ใช้ แสดง False

class Queue:
    def __init__(self):
        self.items = list()

    def enQueue(self, value):
        self.items.append(value)

    def __len__(self):
        return len(self.items)

    def isEmpty(self):
        return len(self.items) <= 0

    def deQueue(self):
        if not self.isEmpty():
            return self.items.pop(0)
        else:
            pass

    def __str__(self):
        if not self.isEmpty():
            s = 'Queue data : '
            for ele in self.items:
                s = s+str(ele)+' '
            return s
        else:
            return 'Empty Queue'

n = int(input('Enter choice : '))
if n == 1:
    q1 = Queue()
    q1.enQueue(10)
    q1.enQueue(20)
    q1.enQueue(30)
    print(q1)
    q1.deQueue()
    q1.enQueue(40)
    print("Size of Queue :",len(q1))
    print(q1)

elif n == 2:
    q1 = Queue()
    q1.enQueue(100)
    q1.enQueue(200)
    q1.enQueue(300)
    q1.deQueue()
    print(q1)
    print("Queue is Empty :",q1.isEmpty())

elif n == 3:
    q1 = Queue()
    q1.enQueue(11)
    q1.enQueue(22)
    q1.enQueue(33)
    q1.deQueue()
    q1.deQueue()
    q1.deQueue()
    print(q1)
    print("Size of Queue :",len(q1))
    print("Queue is Empty :",q1.isEmpty())