s = [7, 9, 3, 4, 5, -2]
n = len(s)
for i in range(n-1):
    for j in range(n-1-i):
        if s[j] > s[j+1]:
            s[j], s[j+1] = s[j+1], s[j]
print(s)
