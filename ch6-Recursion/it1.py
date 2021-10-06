# จงเขียนฟังก์ชั่นที่แสดงผลเลข 1 จนถึง n

# และฟังก์ชั่นที่แสดงผลเลขตั้งแต่ n จนถึง 1

# โดยแสดงผลตามตัวอย่าง

# ****ห้ามใช้คำสั่ง len, for, while, do while, split*****

# หมายเหตุ ฟังก์ชันต้องมี parameter แค่เพียง 1 ตัว
def printFromList(l,i):
    if i == n:
        return 0
    else:
        print(l[i],end=(' '))
        i = i+1
        printFromList(l,i)

def print1ToN(n):
    if n == 0:
        printFromList(ans1,0)
    else :
        ans1.insert(0,n)
        n = n-1
        print1ToN(n)

def printNto1(n):
    if n == 0:
        printFromList(ans2,0)
    else :
        ans2.append(n)
        n = n-1
        printNto1(n)

n = abs(int(input("Enter Input : ")))
ans1 = []
ans2 = []

print1ToN(n)
printNto1(n)