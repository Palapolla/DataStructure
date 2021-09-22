# ให้เขียนคลาสของ Doubly Linked List ซึ่งมีเมท็อดดังนี้

# 1. def __init__(self): สำหรับสร้าง linked list

# 2. def __str__(self): return s แสดง ค่าใน linked list

# 3. def str_reverse(self): return s แสดง ค่าใน linked list จากหลังมาหน้า

# 4. def isEmpty(self): return list นั้นว่างหรือไม่

# 5. def append(self, data): add node ที่มี data เป็น parameter ข้างท้าย linked list

# 6. def insert(self, index, data): insert data ใน index ที่กำหนด

# 7. def remove(self, data): remove & return node ที่มี data

#  - การแทรกในที่นี้ จะเป็นการนำข้อมูลใหม่ที่ต้องการมาใส่แทนที่ตำแหน่งของข้อมูลเดิมและย้ายข้อมูลเดิมไปต่อหลังข้อมูลใหม่ 

# คำแนะนำเพิ่มเติม เพื่อความง่ายในการเขียนโค้ดและไม่ต้องเขียนspecial caseเยอะๆ ให้ลองใช้ Dummy Node 
# ดูนะครับ(หากสงสัยการใช้งาน Dummy Node สอบถามพี่ๆTA หรือ https://youtu.be/XgUIjTQ1HjA )

# โดยรูปแบบ Input มีดังนี้
# 1. append       ->  A
# 2. add_before -> Ab
# 3. insert          ->   I
# 4. remove       ->  R

### Class ###
class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

class DoublyLinkedList:
    def __init__(self):
        self.head = Node(None, None, None)
        self.tail = Node(None, self.head, None)
        self.head.next = self.tail
        self.size = 0

    def __str__(self):
        curr = self.head.next
        s = ""
        while curr is not self.tail:
            s += str(curr.data) + " "
            curr = curr.next

        if s == "":
            return ""
        else:
            return "->".join(s.split())

    def str_reverse(self):
        curr = self.tail.prev
        s = ""
        while curr is not self.head:
            s += str(curr.data) + " "
            curr = curr.prev

        if s == "":
            return ""
        else:
            return "->".join(s.split())

    def isEmpty(self):
        return self.size == 0

    def append(self, data):
        newNode = Node(data, self.tail.prev, self.tail)
        self.tail.prev.next = newNode
        self.tail.prev = newNode
        self.size += 1

    def insert(self, index, data):
        if index >= 0 and index <= self.size:
            curr = self.head
            for i in range(index):
                curr = curr.next
            newNode = Node(data, curr, curr.next)
            curr.next.prev = newNode
            curr.next = newNode
            self.size += 1
        else:
            print("Data cannot be added")

    def remove(self, data):
        try:
            index = -1
            curr = self.head
            while curr.data != data:
                index += 1
                curr = curr.next
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
            self.size -= 1
            print("removed : {} from index : {}".format(data, index))
        except AttributeError:
            print("Not Found!")


i = input("Enter Input : ").split(',')

l = DoublyLinkedList()
for cmd in i:
    oper = cmd.split()[0]
    if oper == "A":
        param = cmd.split()[1]
        l.append(param)

    elif oper == "Ab":
        param = cmd.split()[1]
        l.insert(0, param)

    elif oper == "I":
        param = cmd.split()[1]
        position, data = param.split(':')
        l.insert(int(position), data)
        if int(position) >= 0 and int(position) <= l.size:
            print("index = {} and data = {}".format(position, data))

    elif oper == "R":
        param = cmd.split()[1]
        l.remove(param)

    print("linked list : {}".format(l))
    print("reverse : {}".format(l.str_reverse()))