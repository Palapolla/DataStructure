
# ****** ห้ามใช้ For , While  ( ให้ฝึกเอาไว้ เนื่องจากถ้าเจอตอนสอบจะได้ 0 )

# เขียน Recursive เพื่อหาว่า String ที่รับเข้ามาเป็น Palindrome หรือไม่

def palindrome_check(s,start,end):
    if end - start == 1 or start == end:
        print("'{}' is palindrome".format(s))
    else:
        
        if s[start] == s[end]:
            palindrome_check(s,start+1,end-1)
        else:
            print("'{}' is not palindrome".format(s))

s = input("Enter Input : ")
palindrome_check(s,0,len(s)-1)
    
