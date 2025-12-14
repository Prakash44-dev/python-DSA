s = [-2,1,-3,4,-1,2,1,-5,4]
n = len(s)
p = s[4]   # max sum so far (at least one element must exist)
tot = 0 
for i in range(n):          # starting index
                    # reset sum for each new start
    for j in range(i, n):   # ending index
        tot += s[j]         # add current element
        if tot > p:
            p = tot

print(p)   # ✅ 6
