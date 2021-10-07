# จงเขียนโปรแกรมเพื่อรับข้อความ แล้วให้แสดงผล จำนวนตัวอักษรพิมพ์ใหญ่ และ พิมพ์เล็ก 
# และแสดงตัวอักษรที่พบ เรียงตามลำดับตัวอักษร โดยไม่แสดงตัวอักษรซ้ำ และให้แสดงผลตามตัวอย่าง



# หมายเหตุ ให้ระวังตัวอักษรตัวใหญ่ตัวเล็ก ให้ดี

#  *** String count ***
# Enter message : I Love KMITL.
# No. of Upper case characters : 7
# Unique Upper case characters : I  K  L  M  T  
# No. of Lower case Characters : 3
# Unique Lower case characters : e  o  v  

print(' *** String count ***')
n = input('Enter message : ')

countUp = 0
countLow = 0
upAns = list()
lowAns = list()
for i in range(len(n)):
    # check upper case
    if n[i].isupper():
        if len(upAns) == 0:
            upAns.append(n[i])
            countUp += 1
        elif len(upAns) != 0 and n[i] in upAns:
            countUp += 1
        else: 
            upAns.append(n[i])
            countUp += 1
        
    #check lower case
    if n[i].islower():
        if len(lowAns) == 0:
            lowAns.append(n[i])
            countLow += 1
        elif len(lowAns) != 0 and n[i] in lowAns:
            countLow += 1
        else:
            lowAns.append(n[i])
            countLow += 1
lowAns.sort()
upAns.sort()
print('No. of Upper case characters : {}'.format(countUp))
print('Unique Upper case characters : ',end='')
print('  '.join(upAns))
print('No. of Lower case Characters : {}'.format(countLow))
print('Unique Lower case characters : ',end='')
print('  '.join(lowAns))


