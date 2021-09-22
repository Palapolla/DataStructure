# จำลองการเลื่อนแถวคอยภายในเวลาที่กำหนดโดยใช้ class queue

# โดยที่มีแถวหลัก 1 แถวยาวกี่คนก็ได้

# แถวหน้า cashier 1 ยาว 5 คน โดยที่คนนี้จะใช้เวลา 3 นาทีในการคิดค่าบริการ

# แถวหน้า cashier 2 ยาว 5 คน โดยที่คนนี้จะใช้เวลา 2 นาทีในการคิดค่าบริการ

# ลูกค้าจะ move แถวทุกๆ 1 นาที โดยหากแถว 1 ว่างจะไปก่อนหากเต็มจึงไปแถว 2

# จงแสดง นาที [แถวหลัก] [แถว cashier 1] [แถว cashier 2]

# Enter people and time : HELLO_WORLD 13
# 1 ['E', 'L', 'L', 'O', '_', 'W', 'O', 'R', 'L', 'D'] ['H'] []
# 2 ['L', 'L', 'O', '_', 'W', 'O', 'R', 'L', 'D'] ['H', 'E'] []
# 3 ['L', 'O', '_', 'W', 'O', 'R', 'L', 'D'] ['H', 'E', 'L'] []
# 4 ['O', '_', 'W', 'O', 'R', 'L', 'D'] ['E', 'L', 'L'] []
# 5 ['_', 'W', 'O', 'R', 'L', 'D'] ['E', 'L', 'L', 'O'] []
# 6 ['W', 'O', 'R', 'L', 'D'] ['E', 'L', 'L', 'O', '_'] []
# 7 ['O', 'R', 'L', 'D'] ['L', 'L', 'O', '_', 'W'] []
# 8 ['R', 'L', 'D'] ['L', 'L', 'O', '_', 'W'] ['O']
# 9 ['L', 'D'] ['L', 'L', 'O', '_', 'W'] ['O', 'R']
# 10 ['D'] ['L', 'O', '_', 'W', 'L'] ['R']
# 11 [] ['L', 'O', '_', 'W', 'L'] ['R', 'D']
# 12 [] ['L', 'O', '_', 'W', 'L'] ['D']
# 13 [] ['O', '_', 'W', 'L'] ['D']


class Queue:
    def __init__(self):
        self.items = list()

    def enQueue(self, value):
        self.items.append(value)

    def size(self):
        return len(self.items)

    def is_Empty(self):
        return self.size() <= 0

    def deQueue(self):
        if not self.is_Empty():
            return self.items.pop(0)
        else:
            pass

    def __str__(self):
        if not self.is_Empty():
            return str(self.items)
        else:
            return '[]'
        
    
n = input('Enter people and time : ').split()
main = Queue()
r1 = Queue()
r2 = Queue()
t1,t2 = 1,1

#init
for i in range(len(n[0])):
    main.enQueue(n[0][i])
#start    
for i in range(int(n[1])):   
    if t1 == 3:
        t1 = 0
        r1.deQueue()
    if t2 == 2:
        t2 = 0
        r2.deQueue()

    #timer r1
    if r1.size()>0:
        t1 += 1
    #timer r2
    if r2.size()>0:
        t2 += 1
    
    if r1.size()<5 and main.size()>0:
        r1.enQueue(main.deQueue())
    elif r1.size()==5 and r2.size()<5 and main.size()>0:
        r2.enQueue(main.deQueue())

    print(str(i+1)+" "+str(main)+" "+str(r1)+" "+str(r2))


