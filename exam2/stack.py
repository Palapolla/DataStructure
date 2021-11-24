class Stack:
    """ class Stack 
        default : empty stack / Stack([...])
    """
    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def __str__(self):
        s = ''
        if self.isEmpty():
            return s+"Empty"
        else:
            for ele in self.items[::-1]:
                s += str(ele)+" "
            return s
    #push to first        
    def push(self, i):
        self.items.append(i)
    #pop first out
    def pop(self):
        self.items.pop()
    #peek first one
    def peek(self):
        return self.items[-1]

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

S = Stack()
print(S)
S.push(1)
print(S)
S.push(3)
S.push(2)
print(S)
print(S.peek())
print(S.size())
S.pop()
print(S)
