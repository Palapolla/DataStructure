# ****** ห้ามใช้ For , While  ( ให้ฝึกเอาไว้ เนื่องจากถ้าเจอตอนสอบจะได้ 0 )

# เขียน Recursive รับค่า a,b โดยที่ a,b เป็นจำนวนเต็มบวกหรือศูนย์ และค่าหา ab  

def powarrrrrrrrrr(a,b):
    if b == 1:
        print(a)
    elif b == 0:
        print(1)
    else:
        a = a*c
        b = b-1
        powarrrrrrrrrr(a,b)

a,b = [int(x) for x in input("Enter Input a b : ").split(" ")]
c = a
powarrrrrrrrrr(a,b)