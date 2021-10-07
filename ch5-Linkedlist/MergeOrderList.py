# จงเขียนฟังก์ชั่นสำหรับการ Merge LinkList 2 ตัวเข้าด้วยกันโดยห้ามสร้าง Class LinkList จะมีแต่ Class Node ซึ่งเก็บค่า value ของตัวเองและ Node ถัดไป โดยมีฟังก์ชั่นดังนี้

# createList() สำหรับการสร้าง LinkList ที่รับ List เข้ามาโดยจะ return Head ของ Linklist

# printList() สำหรับการ print LinkList โดยจะรับค่าเป็น head ของ Linklist และจะทำการ print ทุกตัวที่อยู่ใน Linklist ต่อจาก head จนครบทุกตัว

# mergeOrderList() สำหรับการ merge linklist 2 ตัวเข้าด้วยกันโดยให้นำมาต่อกันโดยเรียงตามค่า value โดยที่ให้รับ parameter 2 ตัว และจะ return Head ของ Linklist ที่ทำการ merge แล้ว

# ****ห้ามใช้ sort() หากพบข้อนี้จะไม่ได้คะแนน****

# ****ห้ามสร้าง Class LinkList****


class node:
    def __init__(self,data,next = None ):
        self.data = data
        self.next = next
        
    def __str__(self):
        return str(self.data)

def createList(l=[]):
    p = node(int(l.pop(0)))
    H = p
    while len(l) > 0:
        p.next = node(int(l.pop(0)))
        p = p.next
    return H


def printList(H):
    s = ''
    p = H
    s = s + str(H) + ' '
    p = p.next
    while p != None:
        s = s + str(p) + ' '
        p = p.next
    print(s)

def mergeOrderesList(p,q):
    data = []
    while p != None:
        data.append(p.data)
        p = p.next
    while q != None:
        data.append(q.data)
        q = q.next
    s_data = ImSortButNotThatSort(data,len(data))
    p = node(int(s_data.pop(0)))
    H = p
    while len(s_data)>0:
        p.next = node(int(data.pop(0)))
        p = p.next
    return H

def ImSortButNotThatSort(data,n):
    for i in range(n-1):
        for j in range(n-1-i):
            if data[j]>data[j+1]:
                a = data[j]
                data[j] = data[j+1]
                data[j+1] = a
    return data


#################### FIX comand ####################   
# input only a number save in L1,L2

n = input('Enter 2 Lists : ').split(' ')
L1 = [int(x) for x in n[0].split(',')]
L2 = [int(x) for x in n[1].split(',')]
LL1 = createList(L1)
LL2 = createList(L2)
print('LL1 : ',end='')
printList(LL1)
print('LL2 : ',end='')
printList(LL2)
m = mergeOrderesList(LL1,LL2)
print('Merge Result : ',end='')
printList(m)