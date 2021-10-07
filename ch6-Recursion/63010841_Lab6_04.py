a = [] # tower a
b = [] # tower b
c = [] # tower c

# pop from start tower and insert to [0] of destination tower
def pop_and_append(start, dest):
    global a
    global b
    global c
    if start == 'A':
        x = a.pop(0)
    elif start == 'B':
        x = b.pop(0)
    else:
        x = c.pop(0)
    if dest == 'A':
        a.insert(0, x)
    elif dest == 'B':
        b.insert(0, x)
    else:
        c.insert(0, x)


def show_tower(maxn, row):
    global a
    global b
    global c
    acp = a[::-1]
    bcp = b[::-1]
    ccp = c[::-1]
    if row == 0:
        return
    if row == maxn:
        print('|  |  |')
    if len(a) >= row:
        print("{}  ".format(acp[row-1]), end="")
    else:
        print('|  ', end="")
    if len(b) >= row:
        print("{}  ".format(bcp[row-1]), end="")
    else:
        print('|  ', end="")
    if len(c) >= row:
        print("{}".format(ccp[row-1]), end="")
    else:
        print('|', end="")
    if row != 0:
        print()
    show_tower(maxn, row-1)




def move(n, start, filler, dest, maxn):
    if n == 1:
        print("move {} from  {} to {}".format(n,start,dest))
        pop_and_append(start, dest)
        show_tower(maxn, maxn)
    else:
        move(n-1, start, dest, filler, maxn)
        print("move {} from  {} to {}".format(n,start,dest))
        pop_and_append(start, dest)
        show_tower(maxn, maxn)
        move(n-1, filler, start, dest, maxn)

# initial tower a from user input.
def init_tower_a(num, range):
    global a
    if num <= range:
        a.append(num)
        init_tower_a(num+1, range)



n = int(input("Enter Input : "))
init_tower_a(1, n)
show_tower(n, n)
move(n, 'A', 'B', 'C', n)