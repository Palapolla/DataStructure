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
    lev_result = {0:[],1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[],10:[]}

    def __init__(self):
        self.root = Node(None)

    def insert(self, data, node = None):
        if  self.root.data is None:
            self.root = Node(data)
            self.lev_result.append(data)
        else:
            node = self.root
            while True:
                
                if data < node.data:
                    if node.left is None:
                        self.lev_result.append(data)
                        node.left = Node(data)
                        break
                    node = node.left
                else:
                    if node.right is None:
                        self.lev_result.append(data)
                        node.right = Node(data)
                        break
                    node = node.right
        return self.root
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
    
    def levelorder(self, node,result,level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            self.lev_result[level].append(node.data)
            self.printTree(node.left, level + 1)
        return result


    def inorder(self,node, result):
        if node.left is not None:
            self.inorder(node.left,result)
        if node.data is not None:
            result.append(node.data)
        if node.right is not None:
            self.inorder(node.right,result)
        return result

    def preorder(self,node, result):
        if node.data is not None:
            result.append(node.data)
        if node.left is not None:
            self.preorder(node.left,result)
        if node.right is not None:
            self.preorder(node.right,result)
        return result

    def postorder(self,node, result):
        if node.left is not None:
            self.postorder(node.left,result)
        if node.right is not None:
            self.postorder(node.right,result)
        if node.data is not None:
            result.append(node.data)
        return result

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)

T.printTree(root)
print(' --- Tree traversal ---')
re = T.levelorder(root,[])
print('Level order : ',*re,sep=' ')
re = T.preorder(root,[])
print('Preorder : ',*re,sep=' ')
re = T.inorder(root,[])
print('Inorder : ',*re,sep=' ')
re = T.postorder(root,[])
print('Postorder : ',*re,sep=' ')
