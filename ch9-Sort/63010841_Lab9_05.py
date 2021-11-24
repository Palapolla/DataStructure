inp = input('Enter Input : ').split('/')
inp = [x.split(',') for x in inp]
ans = []
for ele in range(len(inp)):
    result = []
    result.append(inp[ele][0])
    wins = inp[ele][1]
    loss = inp[ele][2]
    draws = inp[ele][3]
    Total_Points = 3 * int(wins) + 0 * int(loss) + 1 * int(draws)
    tp = {}
    tp['points'] = Total_Points
    scored = inp[ele][4]
    conceded = inp[ele][5]
    Goal_Difference = int(scored) - int(conceded)
    cc = {}
    cc['gd'] = Goal_Difference
    result.append(tp)
    result.append(cc)
    ans.append(result)

def bubblesort(list):
   for ele in range(len(list)-1,0,-1):
      for idx in range(ele):
        if list[idx][1]['points']<list[idx+1][1]['points']:
            temp = list[idx]
            list[idx] = list[idx+1]
            list[idx+1] = temp
        elif list[idx][1]['points']==list[idx+1][1]['points']:
            if list[idx][2]['gd']<list[idx+1][2]['gd']:
                temp = list[idx]
                list[idx] = list[idx+1]
                list[idx+1] = temp
bubblesort(ans)
print('== results ==')
for ele in ans:
    print(ele)