
# Chapter : 15 - item : 2 - Exam_3_2_2a
#  ส่งมาแล้ว 0 ครั้ง
# จงเขียนโปรแกรมแบบ Recursive เพื่อหาค่า Min ของ Input ที่ป้อนมา แล้วแสดงผลดังตัวอย่าง


def find_min(n):
    if len(n) == 0:
       pass
    elif len(n) == 1:
       return n[0]
    else:
       new_min = find_min(n[1:])
       min = n[0]
       if new_min < min:
            min = new_min
       return min
inp = [int(x) for x in input('Enter Input : ').split(' ')]
print('Min :',find_min(inp))
