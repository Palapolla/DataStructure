class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


class SinglyLinkedList:
    def __init__(self):
        self.head = Node(None, None)

    def __str__(self):
        s = ''
        p = self.head.next
        while p is not None:
            s += str(p.data)
            if p.next is not None:
                s += ' -> '
            p = p.next
        return s

    def display(self):
        s = ''
        p = self.head.next
        while p is not None:
            s += str(p.data) + ' '
            p = p.next
        return s

    def size(self):
        count = 0
        p = self.head.next
        while p is not None:
            count += 1
            p = p.next
        return count

    def checkMinAndInsert(self, new_data): 
        p = self.head.next
        for index in range(self.size()):
            if new_data < p.data:
                self.insert(index, new_data)
                return
            p = p.next
        else:
            self.append(new_data)

    def isEmpty(self):
        return self.size() == 0

    def nodeAt(self, index):  # -1 is dummy , 0 is first index
        p = self.head  # dummy head
        for _ in range(-1, index):
            p = p.next
        return p

    def insert(self, index, data):
        prevNode = self.nodeAt(index - 1)
        newNode = Node(data, prevNode.next)
        prevNode.next = newNode

    def append(self, data):
        self.insert(self.size(), data)

    def pop(self, index):
        if self.isEmpty():  # check for case prevNode.next == None
            return 'No more to pop'
        if index > self.size() - 1:
            return 'out of range'

        prevNode = self.nodeAt(index - 1)
        nextNode = prevNode.next.next  # no case None.next / but nextNode can be None
        popNode = prevNode.next  # store popNode
        prevNode.next = nextNode
        return popNode  # return None or Node

# CAUTION! this is not a real radixSort...
# it's sort inside it's own data.
def radixSort(linkedList):
    state = False
    time = 0
    size = linkedList.size()
    zero_Linked = SinglyLinkedList()     # I lazy to optimize code to array :P
    one_Linked = SinglyLinkedList()      # make sure that programming has no bug for first time test
    two_Linked = SinglyLinkedList()
    three_Linked = SinglyLinkedList()
    four_Linked = SinglyLinkedList()
    five_Linked = SinglyLinkedList()
    six_Linked = SinglyLinkedList()
    seven_Linked = SinglyLinkedList()
    eight_Linked = SinglyLinkedList()
    night_Linked = SinglyLinkedList()

    for d in range(1000):
        for _ in range(size):
            popNode = linkedList.pop(0)

            originalData = popNode.data
            if originalData >= 0:
                calculatedData = originalData // 10 ** d
            else:
                calculatedData = -originalData // 10 ** d

            if calculatedData % 10 == 0:
                zero_Linked.checkMinAndInsert(originalData)
            elif calculatedData % 10 == 1:
                one_Linked.checkMinAndInsert(originalData)
            elif calculatedData % 10 == 2:
                two_Linked.checkMinAndInsert(originalData)
            elif calculatedData % 10 == 3:
                three_Linked.checkMinAndInsert(originalData)
            elif calculatedData % 10 == 4:
                four_Linked.checkMinAndInsert(originalData)
            elif calculatedData % 10 == 5:
                five_Linked.checkMinAndInsert(originalData)
            elif calculatedData % 10 == 6:
                six_Linked.checkMinAndInsert(originalData)
            elif calculatedData % 10 == 7:
                seven_Linked.checkMinAndInsert(originalData)
            elif calculatedData % 10 == 8:
                eight_Linked.checkMinAndInsert(originalData)
            elif calculatedData % 10 == 9:
                night_Linked.checkMinAndInsert(originalData)

        print('------------------------------------------------------------')
        print('Round :', d + 1)
        print('0 :', zero_Linked.display())
        print('1 :', one_Linked.display())
        print('2 :', two_Linked.display())
        print('3 :', three_Linked.display())
        print('4 :', four_Linked.display())
        print('5 :', five_Linked.display())
        print('6 :', six_Linked.display())
        print('7 :', seven_Linked.display())
        print('8 :', eight_Linked.display())
        print('9 :', night_Linked.display())

        if not zero_Linked.isEmpty() and one_Linked.isEmpty() and two_Linked.isEmpty() and \
                three_Linked.isEmpty() and four_Linked.isEmpty() and five_Linked.isEmpty() and \
                six_Linked.isEmpty() and seven_Linked.isEmpty() and eight_Linked.isEmpty() and night_Linked.isEmpty():
            state = True

        # return back to linkedlist
        while not zero_Linked.isEmpty(): linkedList.append(zero_Linked.pop(0).data)
        while not one_Linked.isEmpty(): linkedList.append(one_Linked.pop(0).data)
        while not two_Linked.isEmpty(): linkedList.append(two_Linked.pop(0).data)
        while not three_Linked.isEmpty(): linkedList.append(three_Linked.pop(0).data)
        while not four_Linked.isEmpty(): linkedList.append(four_Linked.pop(0).data)
        while not five_Linked.isEmpty(): linkedList.append(five_Linked.pop(0).data)
        while not six_Linked.isEmpty(): linkedList.append(six_Linked.pop(0).data)
        while not seven_Linked.isEmpty(): linkedList.append(seven_Linked.pop(0).data)
        while not eight_Linked.isEmpty(): linkedList.append(eight_Linked.pop(0).data)
        while not night_Linked.isEmpty(): linkedList.append(night_Linked.pop(0).data)

        if state is True:
            break
        time += 1
    return linkedList, time


inp = [int(i) for i in input('Enter Input : ').split()]

L = SinglyLinkedList()
L_Origin = SinglyLinkedList()

for i in inp:
    L.append(i)
    L_Origin.append(i)

time = 0
radixLinked, time = radixSort(L)
print('------------------------------------------------------------')
print(time, 'Time(s)')
print('Before Radix Sort :', L_Origin)
print('After  Radix Sort :', radixLinked)