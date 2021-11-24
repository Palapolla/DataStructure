# รับจำนวนเต็มมา 1 จำนวนแล้วให้แสดงผลดังนี้

# - หาก input ที่รับมานั้นมีการเรียงลำดับจากน้อยไปมาก และไม่มีตัวซ้ำเลยให้แสดงผลว่า "Metadrome"

# - หาก input ที่รับมานั้นมีการเรียงลำดับจากน้อยไปมาก และมีตัวซ้ำให้แสดงผลว่า "Plaindrome"

# - หาก input ที่รับมานั้นมีการเรียงลำดับจากมากไปน้อย และไม่มีตัวซ้ำเลยให้แสดงผลว่า "Katadrome"

# - หาก input ที่รับมานั้นมีการเรียงลำดับจากมากไปน้อย และมีตัวซ้ำให้แสดงผลว่า "Nialpdrome"

# - หาก input ที่รับมานั้นทุกหลักเป็นเลขเดียวกันหมด ให้แสดงผลว่า "Repdrome"

# - หากไม่อยู่ในเงื่อนไขด้านบนเลย ให้แสดงผลว่า "Nondrome"

# ****** ห้ามใช้ Built-in Function ที่เกี่ยวกับ Sort ให้น้องเขียนฟังก์ชัน Sort เอง

def bubble_sort_acend(ls):
    for i in range(len(ls)):
        for j in range(len(ls) - 1):
            if ls[j] > ls[j+1]:
                # Swap
                ls[j], ls[j+1] = ls[j+1], ls[j]
    return ls

def bubble_sort_decend(ls):
    for i in range(len(ls)):
        for j in range(len(ls) - 1):
            if ls[j] < ls[j+1]:
                # Swap
                ls[j], ls[j+1] = ls[j+1], ls[j]
    return ls
    
def ascending_order(ls):
    copy = ls[::]
    copy = bubble_sort_acend(copy)
    return ls == copy

def decending_order(ls):
    copy = ls[::]
    copy = bubble_sort_decend(copy)
    return ls == copy

def doub_check(ls):
    for i in range(len(ls)):
        for j in range(i+1,len(ls)):
            if ls[i] == ls[j]:
                return True
    return False

def same_check(ls):
    for i in range(len(ls)):
        if ls[0] != ls[i]:
            return False
    return True



inp = [int(x) for x in input('Enter Input : ')]
decending_order(inp)
# Metadrome
if ascending_order(inp) and not doub_check(inp) and not same_check(inp):
    print('Metadrome')

# Plaindrome
elif ascending_order(inp) and doub_check(inp) and not same_check(inp):
    print('Plaindrome')

# Katadrome
elif decending_order(inp) and not doub_check(inp) and not same_check(inp):
    print('Katadrome')

# Nialpdrome
elif decending_order(inp) and doub_check(inp) and not same_check(inp):
    print('Nialpdrome')

# Repdrome
elif same_check(inp):
    print('Repdrome')

# Nondrome
else:
    print('Nondrome')


