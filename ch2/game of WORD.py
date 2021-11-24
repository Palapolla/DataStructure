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
        # if j%2 == 0:
        #     oldW = torkham.peek()
        # print(oldW)
        # if S[j][1][len(S[j][1])-2:len(S[j][1])].lower() == :
        #     break
    elif S[j][0] == "X":
        break
    else:
        print("\'{}\'".format(" ".join(S[j]))+" is Invalid Input !!!")
        break

# a = ['asdfer','asdf']
# print(a[0][len(a[0])-2:len(a[0])])
# and  self.words[len(self.words)-1][len[self.words[len(self.words)-1]]-2:len(self.words)] != word[0][len(word)-2:len(word)]

number = int(input("Input = "))
stars = 1
spaces = 2 * number - 2
for _ in range(number):  # top half
    for _ in range(stars):
        print('*', end="")
    for _ in range(spaces):
        print(' ', end="")
    for _ in range(stars):
        print('*', end="")
    stars += 1
    spaces -= 2
    print()

stars -= 1
spaces += 2
for _ in range(number-1):  # bottom half
    stars -= 1
    spaces += 2
    for _ in range(stars):
        print('*', end="")
    for _ in range(spaces):
        print(' ', end="")
    for _ in range(stars):
        print('*', end="")

    print()