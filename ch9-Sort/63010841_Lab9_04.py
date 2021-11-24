# เขียนโปรแกรมที่ทำการรับข้อมูลเป็น list เพื่อหาค่ามัธยฐานของข้อมูลใน list โดยจะเริ่มต้นจากข้อมูลใน list เพียง 1 
# ตัวจากนั้นค่อยๆเพิ่มไปเรื่อยๆจนครบ 
# โดยในการหาค่ามัธยฐานเราต้องจัดเรียงข้อมูลตามลำดับจากน้อยไปหามากเสียก่อน 
# จากนั้นแสดงผลตามตัวอย่าง

# ***ห้ามใช้ Built-in Function ที่เกี่ยวกับ Sort เช่น sort, min, max,ฯลฯ***

# l = [e for e in input("Enter Input : ").split()]
# if l[0] == 'EX':
#     Ans = "xxx"
#     print("Extra Question : What is a suitable sort algorithm?")
#     print("   Your Answer : "+Ans)
# else:
#     l=list(map(int, l))
#     #code here


# ***test case พิเศษเพิ่มเติม ไม่คิดคะแนน และไม่มีผลต่อการผ่านโจทย์ข้อนี้หรือไม่***

# พี่มีคำถามมาถามน้องๆว่าในกรณีโจทย์แบบนี้ ถ้าหากจำนวน  input มีจำนวนมากกว่าหมื่นตัวขึ้นไป เราสามารถ sort algorithm แบบใดมาประยุกต์ใช้จึงจะเหมาะสม และ ทำเวลาได้ดี

# - bubble sort

# - straight selection sort

# - insertion sort

# - shell sort

# - merge sort

# - quick sort

# - minHeap and maxHeap

# พิมพ์คำตอบลงในช่อง Ans = "xxx"

# ***ยกมือถามได้นะถ้าสงสัยว่าทำไมเป็นอันนี้***

def insertion_sort(inp_list):
    # We start from 1 since the first element is trivially sorted
    for index in range(1, len(inp_list)):
        curr_val = inp_list[index]
        curr_pos = index

        # As long as we haven't reached the beginning and there is an element
        # in our sorted inp_list larger than the one we're trying to insert - move
        # that element to the right
        while curr_pos > 0 and inp_list[curr_pos - 1] > curr_val:
            inp_list[curr_pos] = inp_list[curr_pos -1]
            curr_pos = curr_pos - 1


        # We have either reached the beginning of the inp_list or we have found
        # an element of the sorted inp_list that is smaller than the element
        # we're trying to insert at index curr_pos - 1.
        # Either way - we insert the element at curr_pos
        inp_list[curr_pos] = curr_val
    return inp_list
        
def findMed(ls):
    n = len(ls)
    medPos = n/2
    if n%2 == 0:
        print('median = %.1f' %((ls[int(medPos)]+ls[int(medPos)-1])/2))
    else:
        print('median = %.1f' %(ls[int(medPos)]))

l = [e for e in input("Enter Input : ").split()]
if l[0] == 'EX':
    Ans = "minHeap and maxHeap"
    print("Extra Question : What is a suitable sort algorithm?")
    print("   Your Answer : "+Ans)
else:
    l=list(map(int, l))
    printLs = []
    res = []
    for i in l:
        printLs.append(i)
        res.append(i)
        res = insertion_sort(res)
        print('list =',printLs,end=' : ')
        findMed(res)

    