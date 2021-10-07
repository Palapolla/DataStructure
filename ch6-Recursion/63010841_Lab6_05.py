
# นักศึกษาจะได้รับ Input เป็น list<int> ของดาวเคราะห์น้อย
# สำหรับดาวเคราะห์น้อยแต่ละดวงนั้น ค่าสัมบูรณ์ จะแสดงขนาดของมัน และเครื่องหมายแสดงถึงทิศทางของมัน (ถ้าเลขเป็นบวกแสดงว่าวิ่งไปทางขวา ,ลบทางซ้าย) โดยที่ดาวเคราะห์น้อยแต่ละดวงเคลื่อนที่ด้วยความเร็วเท่ากัน

# ค้นหาสถานะของดาวเคราะห์น้อยหลังจากการชนกันทั้งหมด

# 1.หากดาวเคราะห์น้อยสองดวงมาพบกันดวงที่เล็กกว่าจะระเบิด

# 2.ถ้าทั้งสองมีขนาดเท่ากันทั้งคู่จะระเบิด

# 3.ดาวเคราะห์น้อยสองดวงที่เคลื่อนที่ไปในทิศทางเดียวกันจะไม่มีวันพบกัน

# ****ห้ามใช้คำสั่ง for, while, do while*****

# หมายเหตุ ฟังก์ชันมี parameter ได้ไม่เกิน 2 ตัว

# def asteroid_collision(asts):
#     #Code Here

# x = input("Enter Input : ").split(",")
# x = list(map(int,x))
# print(asteroid_collision(x))


def asteroid_collision(asts):
    if len(asts) == 1:
        return asts

    results = asteroid_collision(asts[1:])

    if len(results) > 0 and asts[0] > 0 and results[0] < 0:
    

        if asts[0] == abs(results[0]):
            if len(results) > 1:
                return results[1:] 
            elif len(results) == 1:
                return []

        elif asts[0] > abs(results[0]):
            return asteroid_collision([asts[0]] + results[1:])

        elif asts[0] < abs(results[0]):
            return results

    else:
        return [asts[0]] + results


x = input("Enter Input : ").split(",")
x = list(map(int, x))
print(asteroid_collision(x))