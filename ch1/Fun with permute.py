"""
เขียนโปรแกรม Python เพื่อสร้างวิธีเรียงสับเปลี่ยนที่เป็นไปได้ทั้งหมดจากชุดตัวเลขที่กำหนด

"""
print("*** Fun with permute ***")
n = list(map(int, input("input : ").split(",")))
print("Original Cofllection: ", n)
n = n[::-1] 
print("Collection of distinct numbers:")
print(" ", end="")

def addPermute(pos, m) :
    return [m[0:i] + [n[pos]] + m[i:] for i in range(len(m)+1)]
def permute(m) :
    if len(m) == 0 :
        return [[]]
    return [x for y in permute(m[1:])  for x in addPermute(m[0], y)]
print(permute([i for i in range(len(n))]))
