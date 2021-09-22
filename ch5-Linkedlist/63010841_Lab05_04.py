# ให้ตรวจสอบว่า linked list มีการวนซ้ำหรือไม่ และ แสดงผลลัพธ์ตามตัวอย่าง

# โดยมีการรับ input ดังนี้

# 1. append ->   A <int> คือ เพิ่มข้อมูลต่อท้าย linked list

# 2. set_next -> S <index1(int):index2(str)> คือการ set node.next ของ node index ที่1 ให้ชี้ไป node index ที่2

# ซึ่งหากไม่มี  node index ที่1 ใน linked list ให้แสดง error และหากไม่มี node index ที่2 ใน linked list ให้ทำการ append nodeใหม่เข้าไปใน linked list โดยมี value = index2

class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self, lst=None):
        self.head = None
        self.tail = None
        if lst is not None:
            for item in lst:
                self.push_back(item)

    def is_empty(self):
        return self.head is None or self.tail is None  # inspect this clause and head/tail assignment

    def size(self):
        p = self.head
        count = 0
        while p is not None:
            count += 1
            p = p.next
        return count

    def __len__(self):
        return self.size()

    def push_front(self, value):
        if self.is_empty():
            self.head = Node(value)
            self.tail = self.head
            return
        else:
            p = Node(value, self.head)
            self.head.prev = p
            self.head = p

    def push_back(self, value):
        if self.is_empty():
            self.head = Node(value)
            self.tail = self.head
            return
        else:
            new_node = Node(value, prev=self.tail)
            self.tail.next = new_node
            self.tail = new_node

    def is_in(self, value):
        if self.is_empty():
            return False
        p = self.head
        while p is not None:
            if p.value == value:
                return True
            p = p.next
        return False

    def index(self, value):
        p = self.head
        count = 0
        while p is not None:
            if p.value == value:
                return count
            count += 1
            p = p.next
        return -1

    def pop_back(self):
        if self.is_empty():
            print('List is empty')
            return -1
        last = self.tail
        self.tail = last.prev
        if self.tail is not None:
            self.tail.next = None
        last.prev = None
        if self.tail is None:  # list is now empty
            self.head = None
        return last.value

    def pop_front(self):
        if self.is_empty():
            print('List is empty')
            return -1
        first = self.head
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None
        first.next = None
        return first.value

    def traverse(self, rev=False):
        if self.is_empty():
            print('Empty linked list')
        if rev:
            p = self.tail
            out = 'The reversed list contains :'
            while p is not None:
                out += ' ' + str(p.value)
                p = p.prev
            print(out)
        else:
            p = self.head
            out = 'The list contains :'
            while p is not None:
                out += ' ' + str(p.value)
                p = p.next
            print(out)

    def remove(self, value):
        if self.is_empty() or not self.is_in(value):
            print("Value not found in list")
            return -1
        else:
            p = self.head
            while p is not None:
                if p.value == value:
                    break
                p = p.next
            if p is self.head:
                return self.pop_front()
            elif p is self.tail:
                return self.pop_back()
            else:
                prev = p.prev
                next = p.next
                val = p.value
                p.prev = None
                p.next = None
                if prev is not None:
                    prev.next = next
                if next is not None:
                    next.prev = prev
                return val

    def pop(self, pos):
        if self.is_empty() or not (0 <= pos <= self.size() - 1):
            return 'Out of Range'
        else:
            if pos == 0:
                self.pop_front()
            elif pos == self.size() - 1:
                self.pop_back()
            else:
                p = self.head
                count = 0
                while p is not None and count != pos:
                    count += 1
                    p = p.next
                prev = p.prev
                next = p.next
                p.prev = None
                p.next = None
                if prev is not None:
                    prev.next = next
                if next is not None:
                    next.prev = prev
            return 'Success'

    def insert(self, index, value):
        if index == 0 or self.is_empty():
            self.push_front(value)
        elif index >= self.size():
            self.push_back(value)
        elif index < 0:  # - case (before tail = -1)
            index = abs(index)
            count = 0
            p = self.tail
            while p is not None and count < index:
                # print(p)
                p = p.prev
                count += 1
            if p is None:
                self.push_front(value)
            else:
                # print("insertion at: ", p.prev, p, p.next)
                next = p.next
                new_node = Node(value, next, p)
                p.next = new_node
                next.prev = new_node
        else:  # + case
            count = 0
            p = self.head
            while p is not None and count != index:
                p = p.next
                count += 1
            prev = p.prev
            new_node = Node(value, p, prev)
            prev.next = new_node
            p.prev = new_node

    def setNewNextNode(self, pos1, pos2):
        if self.is_empty(): 
            print('Error! {list is empty}')
        elif not 0 <= pos1 < self.size():
            print('Error! {index not in length}:', pos1)
        elif not 0 <= pos2 < self.size():
            print('index not in length, append :', pos2)
            self.push_back(pos2)
        else:
            p = self.head
            count = 0
            while p is not None and count < pos1:
                p = p.next
                count += 1
            node1 = p
            p = self.head
            count = 0
            while p is not None and count < pos2:
                p = p.next
                count += 1
            node2 = p
            node1.next = node2
            node2.prev = node1
            print(f'Set node.next complete!, index:value = {pos1}:{node1.value} -> {pos2}:{node2.value}')

    def findLoop(self):
        mem = []
        count = 0
        p = self.head
        for _ in range(500):
            count += 1
            if p is None:
                break
            if p in mem:
                return True
            mem.append(p)
            p = p.next
        return False


    def __str__(self):
        if self.is_empty():
            return 'Empty'
        else:
            p = self.head
            out = ''
            while p is not None:
                out += str(p.value)
                if p.next is not None:
                    out += '->'
                p = p.next
            return out


n = input('Enter input : ').split(',')
l = LinkedList()
for i in n:
    oper, data = i.split()
    if oper == 'A':
        l.push_back(data)
        print(l)
    else:
        oper1, oper2 = data.split(':')
        l.setNewNextNode(int(oper1), int(oper2))
        if l.findLoop():
            print('Found Loop')
            break
else:
    print('No Loop')
    print(l)