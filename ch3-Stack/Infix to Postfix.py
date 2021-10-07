# การแปลงนิพจน์ infix เป็น postfix
# จะใช้ stack ในการเก็บตัวดำเนินการ
# ลำดับการแปลง infix เป็น postfix
# 1  ถ้าข้อมุลเป็นตัวถูกดำเนินการ (operand) ให้นำไปเป็นผลลัพธ์
# 2  ถ้าข้อมูลเข้าเป็นตัวดำเนินการ (operator) ให้ปฎิบัติดังนี้
#       2.1  ถ้าstack ยังว่างให้ทำการ push
#           ตัวดำเนินการเก็บลงstack
#       2.2  ถ้าstack ไม่ว่างให้ทำการเปรียบเทียบตัวดำเนินการ
#          ที่นำเข้ามากับตัวดำเนินการที่ตำแหน่ง Top ของ stack
#              2.2.1 ถ้าตัวดำเนินการที่นำเข้ามีลำดับความสำคัญมากกว่า
#                   ตัวดำเนินการที่ตำแหน่ง top ของ stack  ให้ทำการ
#                   push ตัวเนินการนั้นเก็บลงใน stack
#           2.2.2  ถ้าตัวดำเนินการที่นำเข้ามา มีลำดับความสำคัญน้อยกว่า
#                    หรือเท่ากับตัวดำเนินการที่ตำแหน่ง top ของ stack  
#                    ให้ทำการ pop ตัวดำเนินการที่ตำแหน่ง top ของ stack
#                         นำออกไปต่อท้ายนิพจน์ผลลัพธ์ และทำการเปรียบเทียบ
#                    ตัวดำเนินการที่นำเข้ามากับตัวดำเนินการที่ตำแหน่ง top
#                        ของ stack ต่อไป    จนกระทั่งตัวดำเนินการที่นำเข้ามามี
#                   ลำดับความสำคัญมากกว่าตัวดำเนินการที่ตำแหน่ง top ของ
#                   stack จึงหยุดเปรียบเทียบและให้ทำการ pushตัวดำเนินการ
#                   ที่นำเข้ามานั้นเก็บลงใน stack
# 3. ถ้าข้อมูลเข้าเป็นเครื่องหมายวงเล็บเปิด   ให้ทำการ push เครื่องหมาย
#     วงเล็บเปิดเก็บลงใน stack
# 4. ถ้าข้อมูลเข้าเป็นเครื่องหมายวงเล็บปิดให้ทำการ pop ข้อมูลออกจาก
#     stack นำออกไปเป็นผลลัพธ์โดยจะทำการ  pop  ต่อไปจนกว่าจะพบ
#     เครื่องหมายวงเล็บเปิด หลังจากนั้นให้ทิ้งเครื่องหมายวงเล็บเปิดและ
#     เครื่องหมายวงเล็บปิดคู่เดิมไป
# 5. ถ้าข้อมูลเข้าหมดให้ทำการ pop ข้อมูลออกจาก stack นำออกไปเป็น
#     ผลลัพธ์โดยทำการ pop ต่อไปจนกระทั่ง stack ว่าง
class Stack:
    """ class Stack 
        default : empty stack / Stack([...])
    """
    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def __str__(self):
        s = 'Value in Stack = '
        if self.isEmpty():
            return s+"Empty"
        else:
            for ele in self.items:
                s += str(ele)+' '
            return s
    def push(self, i):
        return self.items.append(i)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def isEmpty(self):
        return len(self.items)==0

    def size(self):
        return len(self.items)


def infix_posfix(n):
    s = Stack()
    ans = ''
    chOp = '()^*/+-'
    op = '^*/+-'
    op2 = {'(': 0,'^': 4,'*': 3,'/': 3,'+': 2,'-': 2}
    for i in n:
        if i not in chOp:    
            ans += i   
        elif i in op:
            if s.isEmpty():
                s.push(i)
            else:
                while op2.get(i) <= op2.get(s.peek()):
                    ans += s.pop()
                    if s.isEmpty():
                        break
                s.push(i)
        elif i =='(':
            s.push(i)
        elif i == ')':
            while s.peek() != '(':
                ans += s.pop()
            s.pop()  
    while not s.isEmpty():
        ans += s.pop()
    return ans

n = input('Enter Infix : ')
print('Postfix : '+infix_posfix(n))


