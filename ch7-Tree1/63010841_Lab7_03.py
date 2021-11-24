# ให้น้องรับ input เป็น list กับ k และจากนั้นให้สร้าง Binary Search Tree จาก list ที่รับเข้ามา 
# และหาว่าใน Binary Search Tree นั้นมีกี่ Node ที่มีค่าน้อยกว่าหรือเท่ากับ k

from typing import Counter


class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    # left nodes are less than root
    # right nodes are more than root
    counter = 0

    def __init__(self):
        self.root = Node(None)

    def insert(self, data, node = None):
        if  self.root.data is None:
            self.root = Node(data)
        else:
            node = self.root
            while True:
                if data < node.data:
                    if node.left is None:
                        node.left = Node(data)
                        break
                    node = node.left
                else:
                    if node.right is None:
                        node.right = Node(data)
                        break
                    node = node.right
        return self.root
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def find_lessthan_or_equal_to_k(self,node,k):
        if node != None:
            if node.data <= k:
                self.counter += 1
            self.find_lessthan_or_equal_to_k(node.right,k)
            self.find_lessthan_or_equal_to_k(node.left,k)
        return self.counter
        # node = self.root
        # counter = 0
        # #left side
        # while True:
        #     if node is None:
        #         break
        #     if node.data <= k:
        #         counter += 1
        #     node = node.left
        # #right side
        # while True:
        #     if node is None:
        #         break
        #     if node.data <= k:
        #         counter += 1
        #     node = node.right
        # return counter
        



T = BST()
inp = input('Enter Input : ').split('/')
dat = [int(x) for x in inp[0].split(' ')]
k = int(inp[1])
for i in dat:
    root = T.insert(i)
T.printTree(root)
print("--------------------------------------------------")
print(T.find_lessthan_or_equal_to_k(root,k))
