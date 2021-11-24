class Node:
    def __init__(self, data): 
        self.data = data  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.data) 

class BinarySearchTree:

    tmp = 0
    stat = False

    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.data:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.data:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

    def parents(self,r,data):
        if r != None:
            # print(self.stat)
            # print('data',data)
            # print(r.data)
            # print('tmp',self.tmp)
            if str(r.data) == str(data):
                self.stat = True
                return self.tmp
            if self.stat != True:
                self.tmp = r.data
            self.parents(r.right,data)
            self.parents(r.left,data)
        if self.stat:
            return self.tmp
        else:
            return 'not found!!!'

                
def printTree(node, level = 0):
    if node != None:
        printTree(node.right, level + 1)
        print('     ' * level, node)
        printTree(node.left, level + 1)

# def parents(r,data):
#     global temp
#     temp = r
#     print(r)
    
#     if r != None:
#         print(r.right,r.left)
#         if r.right == data or r.left == data:
#             print('yes',r)
#             return str(r)
#         parents(r.right,data)
#         parents(r.left,data)
    

# def find_lessthan_or_equal_to_k(self,node,k):
#     if node != None:
#         if node.data <= k:
#             self.counter += 1
#         self.find_lessthan_or_equal_to_k(node.right,k)
#         self.find_lessthan_or_equal_to_k(node.left,k)
#     return self.counter
temp = 0
tree = BinarySearchTree()
data = input("Enter Input : ").split("/")
for e in data[0].split():
    tree.create(e)
printTree(tree.root)

if str(tree.root) == data[1]:
    print('\nParents of',data[1],'is none because {} is root!!!'.format(data[1]))
else:
    print('\nParents of',data[1],'is',tree.parents(tree.root,data[1]))