# ให้เขียนคลาสของ Singly Linked List ซึ่งมีเมท็อดดังนี้
# 1. __init__     สร้าง Head ขึ้นมาเพื่อบอกว่าจุดเริ่มต้นของ Linked List คือตรงไหน
# 2. __str__     คืนค่าเป็นสตริงซึ่งบอกว่า Linked List เราตั้งแต่หัวไปจนท้ายมีตัวอะไรบ้าง
# 3. isEmpty    เช็คว่า Linked List ของเราว่างหรือป่าว คืนค่าเป็น True / False
# 4. append     add Item เข้า Linked List จากด้านหลัง ไม่คืนค่า
# 5. addHead  add Item เข้า Linked List จากด้านหน้า ไม่คืนค่า
# 6. search      ค้นหา Item ที่ต้องการใน Linked List คืนค่าเป็น Found / Not Found
# 7. index        ค้นหา Item ที่ต้องการใน Linked List ว่าอยู่ที่ Index ไหน คืนค่าเป็น Index (0,1,2,3,4,.....) ถ้าหากไม่มีคืนค่าเป็น -1
# 8. size           คืนค่าเป็นขนาดของ Linked List
# 9. pop            นำ Item Index ที่ pos ออกจาก Linked List คืนค่าเป็น Success / Out of Range




class LinkedList:
    class Node:
        def __init__(self, value,next = None):
            self.value = value
            if next is None :
                self.next = None
            else :
                self.next = next

    def __init__(self):
        self.head = None
        self.size_ = 0

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def __len__(self) :               
        return self.size_ 

    def isEmpty(self):
        return self.head == None

    def nodeAt(self,i) :
        p = self.head
        for j in range(0,i) :
            p = p.next
        return p

    def append(self, item):
        if self.head is None :
            p = self.Node(item)            
            self.head = p
            self.size_ += 1
        else :                         
            q = self.nodeAt(len(self)-1)
            p = self.Node(item)
            p.next = q.next
            q.next = p
            self.size_ += 1

    def addHead(self, item):
        if self.isEmpty() :
            p = self.Node(item)
            self.head = p
            self.size_ += 1
        else :
            p = self.Node(item,self.head)
            self.head = p
            self.size_ += 1


    def search(self, item):
        p = self.head
        for j in range(0,len(self)):
            if p.value == item:
                return 'Found'
            p = p.next
        return 'Not Found'

    #search and return index
    def index(self, item): 
        p = self.head
        for j in range(0,len(self)):
            if p.value  == item:
                return j
            p = p.next
        return -1

    def size(self):
        return self.size_

    def pop(self, pos):
        if self.size_>0:
            if(pos<0 and pos>0-len(self)):
                q = self.nodeAt(len(self)+pos-1)
                q.next = q.next.next
                self.size_ -= 1
                return 'Success'
            elif(pos==0):
                self.head=self.head.next
                self.size_-=1
                return 'Success'
            elif(pos>0 and pos<len(self)-1):
                q=self.nodeAt(pos-1)
                q.next=q.next.next
                self.size_-=1
                return 'Success'
            else:
                return 'Out of Range'
        else:
            return 'Out of Range'
        


L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:], L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k ==
              "Success" else ("{0} | {1}".format(k, L)))
print("Linked List :", L)
