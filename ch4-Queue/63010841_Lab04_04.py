# โรงอาหารของบริษัทแห่งหนึ่ง จะมีเจ้าหน้าที่คอยจัดแถวสำหรับการซื้ออาหาร 
# โดยจะมีหลักการคือจะดูจากแผนกของพนักงานแต่ละคนว่าอยู่แผนกไหน ถ้าหากในแถวที่ต่ออยู่มีแผนกนั้น 
# จะนำพนักงานคนนั้นแทรกไปด้านหลังของแผนกเดียวกัน ตัวอย่างเช่น
# Front | 1 2 2 2 2 3 3 3 | Rear  จาก Queue ถ้าหากมีพนักงานแผนก1เข้ามา Queue จะกลายเป็น Front | 1 1 2 2 2 2 3 3 3 | Rear

# Input :
# จะแบ่งเป็น 2 ฝั่งแบ่งด้วย /   คือ ซ้าย : เป็นแผนกของพนักงานและIDของพนักงานแต่ละคน  ขวา : จะแบ่งเป็น 2 ส่วน คือ D กับ E
# E < id >  ->   เป็นการนำพนักงานเข้า Queue
# D  ->  เป็นการนำพนักงานคนหน้าสุดออกจากแถว โดยจะแสดงผลเป็น id ของพนักงานคนนั้น ถ้าหากไม่มีพนักงานในแถวจะทำการแสดงผลเป็น Empty

# อธิบาย TestCase_1 :  จะมีพนักงาน 4 คน คือแผนก 1 id=101,102 และแผนก 2 id=201,202  ต่อมาจะแสดงผล Empty 
# เพราะยังไม่มีพนักงานในแถว  และนำพนักงาน id=101และ201 เข้าแถวตามลำดับ ต่อมาจะแสดงผลเป็น 101 
# เพราะพนักงาน 101 อยู่คนแรกและแสดงผล 201 เพราะอยู่คนแรก

# Enter Input : 1 101,1 102,2 201,2 202/D,E 101,E 201,D,D
# Empty
# 101
# 201


class Queue:
    def __init__(self):
        self.items = list()

    def enQueue(self, value):
        if self.is_Empty():
            self.items.append(value)
        else:
            self.addQueueByZone(value)

    def size(self):
        return len(self.items)

    def is_Empty(self):
        return self.size() <= 0

    def deQueue(self):
        s = ''
        if not self.is_Empty():
            s = self.items[0][2:]
            self.items.pop(0)
            return s
        else:
            s = 'Empty'
            return s
    
    def addQueueByZone(self,worker):
        index = -1
        if not self.is_Empty():   
            for i in range(len(self.items)):
                if int(self.items[i][0]) == int(worker[0]):
                    index = i
            if index != -1:
                self.items.insert(index+1,worker)
            else:
                self.items.append(worker)


    def __str__(self):
        s = ''
        if not self.is_Empty():
            return str(self.items)
        else:
            return ''


def findZone(value,wk):
    index = 0
    for i in range(len(wk)):
        if str(wk[i][2:]) == str(value[2:]):
            index = i
            break
    return index
            


if __name__ == '__main__':
    q = Queue()
    n = input('Enter Input : ').split('/')
    wk =  [x for x in n[0].split(',')]
    oper = [x for x in n[1].split(',')]
    for i in range(len(oper)):
        if oper[i][0] == 'E':
            q.enQueue(wk[findZone(oper[i],wk)])
        elif oper[i][0] == 'D':
            print(q.deQueue())