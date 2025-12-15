# s=[7,9,3,4,5,-2]
# n=len(s)
# j=0
# for i in range(j,n-1):
#     a=min(s[j:])
#     b=s.index(a)
#     s[i],s[b]=s[b],s[i]
#     j+=1
s = [7, 9, 3, 4, 5, -2]
n = len(s)

for i in range(n - 1):
    min_index = i
    for j in range(i + 1, n):
        if s[j] < s[min_index]:
            min_index = j
    s[i], s[min_index] = s[min_index], s[i]

print(s)



