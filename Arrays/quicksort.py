def quick_sort(s):
    if len(s) <= 1:
        return s
    pivot = s[len(s)//2]
    left = [x for x in s if x < pivot]
    middle = [x for x in s if x == pivot]
    right = [x for x in s if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

s = [7, 9, 3, 4, 5, -2]
print(quick_sort(s))
