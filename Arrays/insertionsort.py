s = [7, 9, 3, 4, 5, -2]
n = len(s)
for i in range(1, n):
    key = s[i]
    j = i - 1
    while j >= 0 and s[j] > key:
        s[j+1] = s[j]
        j -= 1
    s[j+1] = key
print(s)
