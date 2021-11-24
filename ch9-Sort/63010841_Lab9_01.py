# รับ input เป็น list แล้วแสดงขั้นตอนของ bubble sort ตามตัวอย่าง

# ***ห้ามใช้ Built-in Function ที่เกี่ยวกับ Sort เช่น .sort ให้น้องเขียนฟังก์ชัน Sort เอง และห้าม Import***

def Im_bubble_sort_not_that_sort(in_list):
    global move
    for i in range(len(in_list)):

        if i != 0 and move != None and i != len(in_list)-1:
            print(i,'step',end=' : ')
            print(in_list,end='')
            print(' move[{}]'.format(move))
        if i == len(in_list)-1 or move == None:
            print('last step',end=' : ')
            print(in_list,end='')
            print(' move[{}]'.format(move))
            break

        move = None
        for j in range(len(in_list) - 1):
            if in_list[j] > in_list[j+1]:
                # Swap
                temp = in_list[j]
                in_list[j] = in_list[j+1]
                in_list[j+1] = temp
                move = in_list[j+1]
                # in_list[j], in_list[j+1] = in_list[j+1], in_list[j]

move = int
inp = [int(x) for x in input('Enter Input : ').split()]
Im_bubble_sort_not_that_sort(inp)