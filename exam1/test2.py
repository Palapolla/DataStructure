# รับจำนวนเต็มบวก 1 จำนวนแล้วหาว่า มีจำนวนที่หารลงตัวกี่จำนวน โดยให้แสดงผลเหมือนตัวอย่าง

#  *** Divisible number ***
# Enter a positive number : 0
# 0 is OUT of range !!!

#  *** Divisible number ***
# Enter a positive number : 1
# Output ==> 1 
# Total ==> 1

#  *** Divisible number ***
# Enter a positive number : 24
# Output ==> 1 2 3 4 6 8 12 24 
# Total ==> 8

print(' *** Divisible number ***')
n = int(input('Enter a positive number : '))
ans = list()

if n == 0:
    print('0 is OUT of range !!!')
    quit()

for i in range(1,n+1):
    if n%i == 0:
        ans.append(i)

def printAns(ans):
    for i in ans:
        print(i,end=' ')

print('Output ==> ',end='')
print(' '.join(map(str,ans)))
print('Total ==> {}'.format(len(ans)))
