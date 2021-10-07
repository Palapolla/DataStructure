# รับข้อความ 2 ข้อความ

# ข้อความแรกให้หมุนขวาสองตำแหน่ง ข้อความที่สองให้หมุนซ้ายสามตำแหน่ง

# แสดงผลแต่ละครั้งของการหมุน

# หยุดเมื่อข้อความที่หมุน เหมือนข้อความที่รับเข้ามา

# โดยแสดงผล 5 บรรทัดแรก และบรรทัดสุดท้าย


# *** String Rotation ***
# Enter 2 strings : 1234567 abcabcabc
# 1 6712345 abcabcabc
# 2 4567123 abcabcabc
# 3 2345671 abcabcabc
# 4 7123456 abcabcabc
# 5 5671234 abcabcabc
#  . . . . . 
# 7 1234567 abcabcabc
# Total of  7 rounds.

from typing import Counter


print('*** String Rotation ***')
origi = input('Enter 2 strings : ').split(' ')
first = origi[0]
second = origi[1]
count = 1 

while True:
    temp1 = ''
    temp1 = first[len(first)-2:] + first[:len(first)-2]
    first = temp1

    temp2 = ''
    temp2 = second[3:] + second[:3]
    second = temp2

    if count <=5 :
        print(count, first, second)
    if first == origi[0] and second == origi[1] :
        if count > 5 :
            print(' . . . . . ')
            print(count, first, second)
        break
    count += 1

print('Total of  {} rounds.'.format(count))