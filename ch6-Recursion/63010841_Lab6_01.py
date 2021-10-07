# จงเขียนฟังก์ชั่นที่แสดงผลเลข 1 จนถึง n

# และฟังก์ชั่นที่แสดงผลเลขตั้งแต่ n จนถึง 1

# โดยแสดงผลตามตัวอย่าง

# ****ห้ามใช้คำสั่ง len, for, while, do while, split*****

# หมายเหตุ ฟังก์ชันต้องมี parameter แค่เพียง 1 ตัว
def print1ToN(n):
    if n <= 1:
        print("1 ", end="")
        return
    print1ToN(n-1)
    print(str(n), end=" ")

def printNto1(n):
    n = 1 if n < 1 else n
    print(str(n), end=" ")
    if n <= 1:
        return
    else:
        printNto1(n-1)

n = int(input("Enter Input : "))
print1ToN(n)
printNto1(n)