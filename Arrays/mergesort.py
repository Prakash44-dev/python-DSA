def merge_sort(s):
    if len(s) > 1:
        mid = len(s)//2
        left = s[:mid]
        right = s[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                s[k] = left[i]
                i += 1
            else:
                s[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            s[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            s[k] = right[j]
            j += 1
            k += 1
s = [7, 9, 3, 4, 5, -2]
merge_sort(s)
print(s)
