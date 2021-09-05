
# เขียนภาษา Python เพื่อวาดรูปหัวใจ ซึ่งจะรับ input เป็นขนาดของรูปหัวใจ โดย input จะมีค่าตั้งแต่ 2 ขึ้นไป


print("*** Fun with Drawing ***")
a = int(input("Enter input : "))
for y in range(a):
    for x in range(1,4*a-2,1):
        if(x == (a)-y or x == (a)+y or x == (3*a-2)-y or x == (3*a-2)+y):
            print("*", end="")
        elif(x >= (a)-y and x <= (a)+y):
            print("+", end="")
        elif(x >= (3*a-2)-y and x <= (3*a-2)+y):
            print("+", end="")
        else:
            print(".", end="")
    print()

for m in range(1,2*a-1,1):
    for n in range(1,4*a-2,1):
        if(n == m+1 or n == 4*a-3-m):
            print("*", end="")
        elif(n > m+1 and n < 4*a-3-m):
            print("+", end="")
        else:
            print(".", end="")
    print()
