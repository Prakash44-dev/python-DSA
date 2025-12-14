s=[7,1,5,3,6,4]
buy=0
sell=0
pro=0
profit=0

for i in range(0,len(s)):
    for j in range(i+1,len(s)):
        if s[i] < s[j]:
            sell = s[j]
            buy = s[i]
            pro = sell - buy     
        if pro > profit:
            profit = pro

print(profit)
