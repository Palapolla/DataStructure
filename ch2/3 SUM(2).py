def match(x):
    x.sort()
    ans = []
    n = []
    if len(x)<3:
        return "Array Input Length Must More Than 2"
    else:
        for i in range(len(x)):
            for j in range(i+1, len(x)):
                for k in range(j+1, len(x)):
                    if x[i] + x[j] + x[k] == 5:
                        n.append(x[i])
                        n.append(x[j])
                        n.append(x[k])
                    if len(n)==3:
                        a = n[:]
                        ans.append(a)
                        if len(ans)>1:
                            for m in range(len(ans)):
                                for q in range(m+1,len(ans)):
                                    if ans[m] == ans[q]:
                                        del ans[q]
                        n.clear()       
        return ans


n = [int(x) for x in input("Enter Your List : ").split()]
print(match(n))
