# จงเขียนโปรแกรมแบบ Recursive เพื่อรับค่าจำนวนเทอม ของ Harmonic แล้วหาค่าผลรวม 

# โดยในโปรแกรมห้ามใช้คำสั่งการวนซ้ำ(while, for) และให้แสดงผลดังตัวอย่าง



# Harmonic sum = 1 + 1/2 + 1/3 + 1/4 + ... 

# สามารถพิมพ์เลขทศนิยมตามจำนวนจุดทศนิยมที่ต้องการได้จากคำสั่ง

# print("%.5f" %(3.1428571428))





def harmonic_sum(n):
    global express
    global result

    if n == 1:
        result = (1/n) + result
        express = '1' + express
        print(express,'= ',end='')
        return result
    express = ' + 1/{}'.format(n) + express
    result = (1/n) + result
    harmonic_sum(n-1)


express = ''
result = 0.0
print(' *** Harmonic sum ***')
num = int(input("Enter number of terms : ")) 
harmonic_sum(num)
print("%.8f" %(result))