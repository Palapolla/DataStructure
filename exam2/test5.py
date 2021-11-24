# จงสร้าง class singly linked list (อาจใช้ตัวอย่างจาก ข้อ 2 ได้)

# เขียนโปรแกรมเพื่อหาค่าเฉลี่ยเลขคณิต (mean) และ ค่ามัธยฐาน (median)  และแสดงผลดังตัวอย่าง 
# โดยให้ใช้โครงสร้างข้อมูลแบบ LinkedList สำหรับเก็บค่าเท่านั้น



# ***ห้ามใช้ function sorted() และการจัดการข้อมูลด้วยชนิดข้อมูล list ของ python ***



# หมายเหตุ คำสั่งในการแสดงผลเลขทศนิยม



# num = 20.4564
# print("float = %.2f" % num)


# output



# float = 20.46



# ตัวอย่างการใช้งาน

# inputlist = [int(e) for e in input('Enter numbers : ').split()]
# l = LinkedList()

# print("Output :")
# print(l)
# print('Amount of value =',len(l))
# findMean(l)
# findMedian(l)




# ตัวอย่าง output 

# Enter numbers : 7 9 3 2 1 2 3 4 8 9 3 15

# Output :

# Linked value : 1 2 2 3 3 3 4 7 8 9 9 15

# Amount of value = 12

# Mean = 5.5

# Median = 3.5

 

# Enter numbers : 7 6 74 44 6 37 55 35 3 31 3 10

# Output :

# Linked value : 3 3 6 6 7 10 31 35 37 44 55 74

# Amount of value = 12

# Mean = 25.92

# Median = 20.5

 

# Enter numbers : 7 74 44 6 37 55 35 31 3 10 22 12

# Output :

# ﻿Linked value : 3 6 7 10 12 22 31 35 37 44 55 74


# Amount of value = 12

# Mean = 28.00

# Median = 26.50





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

    def getvalue(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head,str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

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

    def sortList(self):  
        cur = self.head  
        index = None  
        if(self.head == None):  
            return  
        else:  
            while(cur != None):  
                index = cur.next  
                while(index != None):  
                    if(cur.value > index.value):  
                        temp = cur.value  
                        cur.value = index.value  
                        index.value = temp  
                    index = index.next  
                cur = cur.next  
#13
def findMean(l):
    n = len(l)
    sum = 0
    cur = l.head
    for i in range(n):
        sum += cur.value
        if cur.next != None:
            cur = cur.next
    print('Mean = %.2f'%(sum/n))
    


def findMedian(l):
    n = len(l)
    medPos = n/2
    # print(medPos)
    # print(l.nodeAt(int(medPos)).value)
    if n%2 == 0:
        print('Median = %.2f' %((l.nodeAt(int(medPos)).value+l.nodeAt(int(medPos)-1).value)/2))
    else:
        print('Median = %.2f' %(l.nodeAt(int(medPos)).value))
    


inputlist = [int(e) for e in input('Enter numbers : ').split()]
l = LinkedList()
for i in inputlist:
    l.append(i)
print("Output :")
l.sortList()
print(l)
print('Amount of data =',len(l))
findMean(l)
findMedian(l)
