
# ให้น้องรับ input แล้วนำ input นั้นมาสร้าง Binary Search Tree โดย input ตัวแรกสุดจะเป็น Root เสมอ

# โดยมีการป้อน input ดังนี้

# i <int> = insert data

# d <int> = delete data

# หมายเหตุ การลบนั้นจะใช้หลักการของ Inorder Successor และ จำนวน parameter มีได้มากสุด 3 ตัว

# Enter Input : d 1,i 1,d 1,i 0,i 2,i 4,i 1,i 5,i 3,d 2




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
    dat = []
    root2 =Node()

    def __init__(self):
        self.root = Node(None)

    def insert(self, data, node = None):
        self.dat.append(data)
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

    # def delete(self,dat):
    #     stat = True
    #     if dat in self.dat:
    #         self.root = Node(None)
    #         for i in range(len(self.dat)):
    #             d = self.dat[i]
    #             if d is not dat:
    #                 self.insert(d)
    #     else:   
    #             stat = False
    #             print('Error! Not Found DATA')
    #     return self.root,stat
        
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def delete(self, data):
        if self == None:
            return self
        if data < self.root.data:
            if self.root.left:
                self.root.left = self.delete(data)
            return self.root
        if data > self.root.data:
            if self.root.right:
                self.root.right = self.delete(data)
            return self.root
        if self.root.right == None:
            return self.root.left
        if self.root.left == None:
            return self.root.right
        min_larger_node = self.root.right
        while min_larger_node.left:
            min_larger_node = min_larger_node.left
        self.root.data = min_larger_node.data
        self.root.right = self.delete(min_larger_node.data)
        return self.root



T = BST()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[0] == 'i':
        print('insert',int(i[2]))
        root = T.insert(i[2])
        T.printTree(root)
    if i[0] == 'd':
        print('delete',int(i[2]))
        root = T.delete(i[2])
        if root[1]:
            T.printTree(root[0])
