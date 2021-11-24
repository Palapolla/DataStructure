class Node:
    def __init__(self, data): 
        self.data = data  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.data) 

class BST:
    def __init__(self): 
        self.root = None

    def insert(self, val):  
        if self.root is None:
            root = Node(val)
            self.root = root
            return
        curr = self.root

        while True:
            if val > curr.data:
                if curr.right is None:
                    curr.right = Node(val)
                    break
                else:
                    curr = curr.right
            elif val < curr.data:
                if curr.left is None:
                    curr.left = Node(val)
                    break
                else:
                    curr = curr.left
            else:
                break
        
        return self.root

    def delete(self, r, data):
        if r is None:
            return r
        
        if data < r.data:
            r.left = self.delete(r.left, data)
        elif data > r.data:
            r.right = self.delete(r.right, data)
        else:
            if r.left is None:
                temp = r.right
                r = None
                return temp
            
            elif r.right is None:
                temp = r.left
                r = None
                return temp

            temp = self.min_value_node(r.right)

            r.data = temp.data

            r.right = self.delete(r.right, temp.data)
        
        return r
    
    def can_delete(self, data):
        if self.root is None:
            return False
        curr = self.root
        while curr is not None:
            if data == curr.data:
                return True
            elif data > curr.data:
                curr = curr.right
            else:
                curr = curr.left 
        
        return False

    def min_value_node(self, root):
        curr = root
        while curr.left is not None:
            curr = curr.left
        return curr
        

def printTree(node, level = 0):
    if node != None:
        printTree(node.right, level + 1)
        print('     ' * level, node)
        printTree(node.left, level + 1)


tree = BST()
inp = input("Enter Input : ").split(",")
for ele in inp:
    if ele[0] == 'i':
        tree.insert(int(ele[2]))
        print(f'insert {ele[2]}')
        printTree(tree.root)
    elif ele[0] == 'd':
        print(f'delete {ele[2]}')
        if tree.can_delete(int(ele[2])):
            tree.root = tree.delete(tree.root, int(ele[2]))
        else:
            print("Error! Not Found DATA")
        printTree(tree.root)