
# ให้น้องๆเขียนโปรแกรมโดยรับ input 2 แบบ โดยใช้ Queue ในการแก้ปัญหา



# E  <value>  ให้นำ value ไปใส่ใน Queue และทำการแสดงผล ข้อมูลปัจจุบันของ Queue

# D  ให้ทำการ Dequeue ตัวที่อยู่หน้าสุดของ Queue ออก หลังจากนั้นแสดงตัวเลขที่เอาออกมา และ แสดงผลข้อมูล
#    ปัจจุบันของ Queue

# ***และเมื่อจบการทำงานให้แสดงผลข้อมูลปัจจุบันของ Queue พร้อมกับข้อมูลที่ถูก Dequeue ทั้งหมดตามลำดับ
# ***ถ้าหากไม่มีข้อมูลใน Queue แล้วให้แสดงคำว่า  Empty



class Queue:
    def __init__(self):
        self.items = list()

    def enQueue(self, value):
        self.items.append(value)

    def size(self):
        return len(self.items)

    def is_Empty(self):
        return self.size() <= 0

    def deQueue(self):
        if not self.is_Empty():
            return self.items.pop(0)
        else:
            return 'Empty'

    def __str__(self):
        output = ""
        if not self.is_Empty():
            for item in range(len(self.items)):
                output += str(self.items[item])
                if item < len(self.items)-1:
                    output += ', '
        else:
            output = 'Empty'
        return output
    




n = input('Enter Input : ').split(',')
deq = []
q = Queue()
for i in n:
    if i[0] == 'E':
        q.enQueue(i[2:])
    elif i[0] == 'D':
        a = q.deQueue()
        if a != 'Empty':
            deq.append(a)
            print(str(deq[len(deq)-1])+' <- ',end='')
    print(q)
    
if len(deq) < 1:
    print('Empty',end='')
else:
    for j in range(len(deq)):    
        print(str(deq[j]),end='')
        if j < len(deq)-1:
            print(', ',end='')

print(' : '+str(q))