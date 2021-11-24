# # Huffman Coding in python


class TreeNode(object): 
    def __init__(self, val,freq,left = None,right = None): 
        self.val = val 
        self.left = left
        self.right = right
        self.freq = freq

    def __str__(self):
        return str(self.val)

class AVL_Tree: 
    def __init__(self):
        self.root = None
    def insert(self,root,key,freq) :
        if not root :
            return TreeNode(key,freq)
        elif freq < root.freq :
            root.left = self.insert(root.left,key,freq)
        elif freq == root.freq :
            if key < root.val :
                root.left = self.insert(root.left,key,freq)
            else :
                root.right = self.insert(root.right,key,freq)
        else:
            root.right = self.insert(root.right,key,freq)
        return root
    
    def inOrder(self,root) :
        if not root :
            return []
        s = self.inOrder(root.right) + [TreeNode(root.val,root.freq)] + self.inOrder(root.left)
        return s

    def printTree90(self,node, level = 0):
        if node != None:
            self.printTree90(node.right, level + 1)
            print('     ' * level, node)
            self.printTree90(node.left, level + 1)
            
    def printCode(self,node, code):
        s = ''
        if node:
            s = self.printCode(node.right, code + '1')
            if node.val != '*':
                s += "'" + str(node.val) + "': '" + code + "'";
            a = self.printCode(node.left, code + '0')
            if a != '':
                s += ', ' + a
        return s

    def search(self,node, data, code): 
        if not node:
            return None
            
        if data == node.val:
            return code
        if node:
            s = self.search(node.right, data, code + '1')
            if s != None:
                return s
            s = self.search(node.left, data, code + '0')
            return s

inp = list(input('Enter Input : '))
s = set(inp)

huff = AVL_Tree()

for data in s:
    huff.root = huff.insert(huff.root, data, inp.count(data))
    
data = huff.inOrder(huff.root)
temp = [data.pop()]

while len(data) != 0 or len(temp) != 1:
    if len(temp) > 1:
        if data == [] or (data[-1].freq >= temp[0].freq + temp[1].freq):
            a, b =  temp.pop(0), temp.pop(0)
            temp.append(TreeNode('*', a.freq + b.freq, a, b))
        else:
            temp.append(data.pop())
    else:
        temp.append(data.pop())

print('{' + f'{huff.printCode(temp[0], "")}' + '}')
huff.printTree90(temp[0])
print('Encoded! : ', end = '')
for key in inp:
    print(huff.search(temp[0], key, ''), end = '')