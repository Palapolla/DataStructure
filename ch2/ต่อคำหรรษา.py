# ให้นักศึกษาเขียนโปรแกรมภาษา Python ในการใช้ Class สำหรับ “เกมต่อคำ” โดยจะมีกติกาดังต่อไปนี้

 
# 1. คำล่าสุดจะต้องไม่ซ้ำกับคำที่เคยพูดไปแล้ว เช่นถ้าหากมีคนพูดว่า “Apple” ไปก่อนหน้านั้นแล้ว
# จะไม่สามารถพูดว่า “Apple” ได้อีก


# 2. โดยการดูว่า 2 คำนั้นจะ Match กันหรือไม่ ให้ดู 2 ตัวอักษรสุดท้ายของข้อความสุดท้ายใน List กับ 2
# ตัวอักษรแรก ของคำล่าสุด เช่น [“Apple”, “lemon”] ถ้าหากคำที่จะเข้ามาเป็น “Onion” จะถือว่า Match
# แต่ถ้าหากคำที่เข้ามาเป็น “nectarine” จะถือว่าไม่ Match และเกมจะจบลงทันที


# 3. Ignore Case Sensitive


# โดยจะมีรูปแบบคำสั่งดังต่อไปนี้
# - P < word > จะเป็นการต่อคำ
# - R จะเป็นการเริ่มคำใหม่ทั้งหมด
# - X เป็นการระบุว่าจบการทำงาน


# โดยจะรับประกันว่า word ที่รับมา จะมีความยาวอย่างน้อยที่สุดคือ



class TorKham:
    def __init__(self):
        self.words = []
    
    def restart(self):
        self.words.clear()
        return "game restarted"

    def play(self,word):
        if word[0] == "P" :
            if len(self.words)>1 and self.words[len(self.words)-2][len(self.words[len(self.words)-2])-2:len(self.words[len(self.words)-2])].lower() != self.words[len(self.words)-1][len(self.words[len(self.words)-1])-2:len(self.words[len(self.words)-1])].lower() :
                return "game over"
            else:
                self.words.append(word[1])
                return self.words   
                
    def peek(self):
        return self.words[-1]
    

torkham = TorKham()

print("*** TorKham HanSaa ***")

oldW = '0'

S = input("Enter Input : ").split(',')
for i in range(len(S)):
    S[i]=S[i].split(" ")
for j in range(len(S)):
    
    if S[j][0] == "R":
        oldW = 0
        print(torkham.restart())
    elif S[j][0] == "P":
        print('\'{}\''.format(S[j][1]),end=" -> ")
        print(str(torkham.play(S[j])))
    elif S[j][0] == "X":
        break
    else:
        print("\'{}\'".format(" ".join(S[j]))+" is Invalid Input !!!")
        break
