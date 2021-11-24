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


exp = ''


def inorder(node):
    global exp
    if node is not None:
        inorder(node.left)
        exp += str(node.value) + ' '
        inorder(node.right)


def ranking(lst, to_find):
    rank = 0
    for i in range(len(lst)):
        if to_find >= lst[i]:
            rank += 1
    return rank


inp = input('Enter Input : ').split('/')
lst = list(map(int, inp[0].split()))
tree = BST()
to_find = int(inp[1])
for item in lst:
    tree.insert(item)
tree.print_tree(tree.root)
print('--------------------------------------------------')
inorder(tree.root)
rank_list = list(map(int, exp.split()))
print(f'Rank of {to_find} : {ranking(rank_list, to_find)}')