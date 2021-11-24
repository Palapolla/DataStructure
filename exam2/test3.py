# จงสร้าง class singly linked list (จากตัวอย่างในข้อ 2 หรือจะสร้างขึ้นใหม่ได้) 



# แล้วเพิ่ม method removeDup() ซึ่งเป็น method ที่ลบข้อมูลตัวซ้ำออก โดยไม่เปลี่ยนลำดับข้อมูล 



# ตัวอย่างการใช้งาน


# inputlist = [int(e) for e in input('Enter numbers : ').split()]

# l = LinkedList()
# print("Linkedlist Before removeDuplicate")
# print(l)
# print("Linkedlist After removeDuplicate")
# l.removeDup()
# print(l)


# แล้วให้แสดงผลดังตัวอย่าง



# Enter numbers : 3 5 7 9 11 7 5 20

# Linkedlist Before removeDuplicate

# Linked data : 3 5 7 9 11 7 5 20 

# Linkedlist After removeDuplicate

# Linked data : 3 5 7 9 11 20 



# Enter numbers : 45 -8 0 8 -8 7 4 2 3 1 2

# Linkedlist Before removeDuplicate

# Linked data : 45 -8 0 8 -8 7 4 2 3 1 2 

# Linkedlist After removeDuplicate

# Linked data : 45 -8 0 8 7 4 2 3 1 

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
        cur, s = self.head,"Linked data : " + str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def __len__(self) :               # เพิ่ม เมื่อ เติมข้อมูล  ลด เมื่อ นำข้อมูลออก
        return self.size_

    def  removeDup(self):
        for i in range(len(self)):
            cur = self.nodeAt(i)
            if cur == None:
                break
            # print('curr ',cur.value,"i",i)
            j = i+1
            while True:
                checker = self.nodeAt(j)
                if checker == None:
                    break
                # print("checker ",checker.value,'j',j)
                if cur.value==checker.value:
                    # print('pop',checker.value)
                    self.pop(j)
                    j = i+1
                else:
                    j +=1
                

    def isEmpty(self):
        return self.head == None

    def nodeAt(self,i) :              # หาค่าตำแหน่งของโหนด เทียบกับ อินเด็กซ์
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
        if pos<0 and pos>0-len(self):
            q = self.nodeAt(len(self)+pos-1)
            q.next = q.next.next
            self.size_ -= 1
        elif pos==0:
            self.head=self.head.next
            self.size_-=1
        elif pos>0 and pos<len(self)-1:
            q=self.nodeAt(pos-1)
            q.next=q.next.next
            self.size_-=1
        elif pos == len(self)-1:
            q=self.nodeAt(pos-1)
            q.next=None
            self.size_-=1



inputlist = [int(e) for e in input('Enter numbers : ').split()]

l = LinkedList()
for i in inputlist:
    l.append(i)
print("Linkedlist Before removeDuplicate")
print(l)
print("Linkedlist After removeDuplicate")
l.removeDup()
print(l)