# ให้เรียงลำดับ input จากน้อยไปมากของจำนวนเต็มบวกและศูนย์ โดยถ้าหากเป็นจำนวนเต็มลบไม่ต้องยุ่งกับมัน

# ****** ห้ามใช้ Built-in Function ที่เกี่ยวกับ Sort ให้น้องเขียนฟังก์ชัน Sort เอง
def im_Sort_ButNotThat_Sort(in_list):
    negative = []
    copy = in_list[::]

    i = 0
    while True:
        if i == len(copy):
            break
        if copy[i] < 0:
            copy.pop(i)
            i = 0
        else:
            i += 1

    for i in range(len(in_list)):
        if in_list[i] < 0:
            negative.append([i,in_list[i]])

    for i in range(len(copy)):
        for j in range(len(copy) - 1):
            if copy[j] > copy[j+1]:
                # Swap
                temp = copy[j]
                copy[j] = copy[j+1]
                copy[j+1] = temp
                # in_list[j], in_list[j+1] = in_list[j+1], in_list[j]

    for i in range(len(negative)):
        copy.insert(negative[0][0],negative[0][1])
        negative.pop(0)

    return copy

inp = [int(x) for x in input('Enter Input : ').split()]
print(*im_Sort_ButNotThat_Sort(inp),sep=' ')