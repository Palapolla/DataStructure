# จาก class LinkedList ในข้อ 2 จงเขียน method contentEquivalence  เพื่อตรวจสอบว่า linked list 
# ที่รับเข้ามากับ linked list ของตัวมันเองมีคุณสมบัตินี้หรือไม่  โดยจะ return True ถ้ามีคุณสมบัตินี้ ถ้าไม่ใช่เป็น False

 

# โดยคุณสมบัติ content equivalence(CV) เป็นดังนี้ เมื่อ linked list มีจำนวนโหนดเท่ากันและโหนดต่าง ๆ 
# ของทั้ง 2 lists มีค่าเท่ากันทุกโหนด โดยที่ตำแหน่งของโหนดที่เก็บข้อมูลของทั้ง 2 lists อาจแตกต่างกันได้
# เช่น [1,2,4,8] กับ [4,1,2,8] มีคุณสมบัติ CV ในขณะที่ [1,2,4,8] กับ [3,4,2,8] ไม่มีคุณสมบัติ CV



# ***ห้ามใช้ function sorted() และการจัดการข้อมูลด้วยชนิดข้อมูล list ของ python ***



# การใช้งาน

 

# list1 = LinkedList()

# list2 = LinkedList()

# list.contentEquivalence(list2)



# โดยรับข้อมูลจากผู้ใช้และแสดงผลดังนี้

# ตัวอย่าง 1

# List1,List2 : a b c d, d c b a

# List1 content Equivalence List2 : True



# ตัวอย่าง 2

# List1,List2 : a b c d e, e d c b a

# List1 content Equivalence List2 : True



# ตัวอย่าง 3

# List1,List2 : a b c d e, e c b a

# List1 content Equivalence List2 : False

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
        i = 0
        p = self.head
        for j in range(0,len(self)):
            if p.value == item:
                i +=1
            p = p.next
        return i

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

    def contentEquivalence(self,other):
        if len(self)!=len(other):
            print("List1 content Equivalence List2 : False")
            return 0
        for i in range(len(self)):
            # print(self.nodeAt(i).value)
            # print(other.search(self.nodeAt(i).value))
            if other.search(self.nodeAt(i).value)>self.search(self.nodeAt(i).value) or other.search(self.nodeAt(i).value)==0 \
                or self.search(self.nodeAt(i).value)>other.search(self.nodeAt(i).value) or self.search(other.nodeAt(i).value)==0:
                print("List1 content Equivalence List2 : False")
                return 0
        print("List1 content Equivalence List2 : True")

n = input("List1,List2 : ").split(',')

l1 = n[0].split(' ')
l2 = n[1].split(' ')
while l1.count('')!=0:
    l1.remove('')

while l2.count('')!=0:
    l2.remove('')    
list1 = LinkedList()
list2 = LinkedList()
for i in l1:
    list1.append(i)
for i in l2:
    list2.append(i)


list1.contentEquivalence(list2)