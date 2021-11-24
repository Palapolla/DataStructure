
# จงเขียนโปรแกรมแบบ Recursive เพื่อหาว่า String ที่รับเข้ามาเป็น Palindrome หรือไม่ แล้วให้แสดงผลดังตัวอย่าง

def palindrome_checker(s,start,end):
    global inp
    if end - start == 1 or start == end:
        print("'{}' is palindrome".format(inp))
    else:
        # print('yes')
        # print(s[start],s[end])
        # print(start,end)
        if s[start] == s[end]:
            palindrome_checker(s,start+1,end-1)
        else:
            print("'{}' is not palindrome".format(inp))

inp = input("Enter Input : ")
s = inp.lower()
filter = " ().,?!@#$\"“”’\'%^><&;:"
for char in filter:
    s = s.replace(char, "")
# print(s)
# print(len(s))
palindrome_checker(s,0,len(s)-1)
    