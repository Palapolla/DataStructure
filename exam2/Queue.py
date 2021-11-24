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