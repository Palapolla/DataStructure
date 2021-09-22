from collections import deque


class Queue:
    def __init__(self, list=None):
        if list == None:
            self.items = deque()
        else:
            self.items = deque(list)

    def enqueue(self, i):
        self.items.append(i)

    def dequeue(self):
        return self.items.popleft()

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


book, comm = input("Enter Input : ").split("/")
q = Queue(book.split())
comm = comm.split(",")
for i in comm:
    if i == 'D':
        q.dequeue()
    else:
        e, value = i.split()
        q.enqueue(value)
for i in q.items:
    if q.items.count(i) > 1:
        print("Duplicate")
        quit()
print("NO Duplicate")