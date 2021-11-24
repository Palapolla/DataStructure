# จงเขียนฟังก์ชั่นสำหรับการ insert แบบ Binary Search Tree (BST) โดยที่ input 
# ตัวแรกจะเป็น root เสมอและจงเขียนฟังก์ชั่นสำหรับการหาค่าที่ใกล้เคียง input 
# ที่รับเข้ามาที่สุดที่อยู่ใน BST ที่ทำการ insert ครบแล้ว

# รูปแบบการรับ input จะแบ่งโดย '/'

# 1.ชุดของ BST ที่จะทำการ insert โดยตัวแรกจะเป็น root เสมอ

# 2.ค่าที่จะนำมาเปรียบเทียบกับค่าใน BST ที่ทำการ insert แล้ว

# รูปแบบ output 

# จะ printTree ทุกครั้งที่มีการ insert ค่าเข้าและเมื่อทำการ insert จบจะเรียกใช้ฟังก์ชั่น closestValue(root,value) และแสดงค่าที่ใกล้เคียงที่สุดจาก BST 

# *** ถ้าหากค่าที่รับเข้ามาเทียบมีอยู่ใน BST ให้ return ค่านั้นออกมาได้เลย และหากมีค่าที่อยู่ใกล้มากกว่า 1 จำนวนให้แสดงจำนวนที่มากที่สุดที่อยู่ใกล้ค่านั้น ***



# class Node:
#     def __init__(self, data=None):
#         self.data = data
#         self.left = None
#         self.right = None
    
#     def __str__(self):
#         return str(self.data)

# class BST:
#     closest = None
#     mem = None
#     lev_result = []
#     # left nodes are less than root
#     # right nodes are more than root
#     def __init__(self):
#         self.root = Node(None)

#     def insert(self, data, node = None):
#         if  self.root.data is None:
#             self.root = Node(data)
#             self.lev_result.append(data)
#         else:
#             node = self.root
#             while True:
                
#                 if data < node.data:
#                     if node.left is None:
#                         self.lev_result.append(data)
#                         node.left = Node(data)
#                         break
#                     node = node.left
#                 else:
#                     if node.right is None:
#                         self.lev_result.append(data)
#                         node.right = Node(data)
#                         break
#                     node = node.right
#         return self.root
    
#     def printTree(self, node, level = 0):
#         if node != None:
#             self.printTree(node.right, level + 1)
#             print('     ' * level, node)
#             self.printTree(node.left, level + 1)

#     def closest_with_k(self,node,k,mem=None):
#             if mem is None:
#                 self.mem = abs(abs(node.data)-k)
#                 self.closest_with_k(node,k,self.mem)
#             if node != None and mem is not None:
#                 if abs(abs(node.data)-k)<mem:
#                     self.mem = abs(abs(node.data)-k)
#                     self.closest = node.data
#                 self.closest_with_k(node.right,k,self.mem)
#                 self.closest_with_k(node.left,k,self.mem)
#             return self.closest

# T = BST()
# inp = input('Enter Input : ').split('/')
# dat = [int(x) for x in inp[0].split(' ')]
# k = int(inp[1])
# for i in dat:
#     root = T.insert(i)
#     T.printTree(root)
#     print("--------------------------------------------------")
# print(T.closest_with_k(root,k))

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)


class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        traversal_path = ''
        if self.root is None:
            self.root = Node(value)
        else:
            node = self.root
            while node is not None:
                if value < node.value:
                    traversal_path += 'L'
                    if node.left is None:
                        node.left = Node(value)
                        break
                    else:
                        node = node.left
                else:
                    traversal_path += 'R'
                    if node.right is None:
                        node.right = Node(value)
                        break
                    else:
                        node = node.right
        return traversal_path + '*'

    def print_tree(self, node, level=0):
        if node is not None:
            self.print_tree(node.right, level + 1)
            print('     ' * level, node)
            self.print_tree(node.left, level + 1)

    def closest_value(self, value):
        if self.root is not None:
            diff = 99999999999999999999999
            to_return = -1
            q = Queue()
            q.enqueue(self.root)
            while not q.is_empty():
                node = q.dequeue()
                if value == node.value:
                    to_return = node.value
                    break
                else:
                    if abs(value-node.value) < diff:
                        diff = abs(value-node.value)
                        to_return = node.value
                if node.left is not None:
                    q.enqueue(node.left)
                if node.right is not None:
                    q.enqueue(node.right)
            return to_return



inp = input('Enter Input : ').split('/')
lst = list(map(int, inp[0].split()))
tree = BST()
compare = int(inp[1])
for item in lst:
    tree.insert(item)
    tree.print_tree(tree.root)
    print('--------------------------------------------------')
print(f'Closest value of {compare} : {tree.closest_value(compare)}')