nums = [3, 4, 5, 1, 2]
n = len(nums)

br = -1

# Step 1: find the break point
for i in range(1, n):
    if nums[i] < nums[i - 1]:
        br = i
        break

# Step 2: if no break, already sorted
if br== -1:
    print(True)
else:
    # Step 3: check remaining part is sorted
    is_sorted = True
    for i in range(br + 1, n):
        if nums[i] < nums[i - 1]:
            is_sorted = False
            break

    # Step 4: check last <= first
    if not is_sorted or nums[-1] > nums[0]:
        print(False)
    else:
        print(True)
