def lis_greedy_per_start(nums):
    best = 0
    for i in range(len(nums)):
        seq = [nums[i]]                # start a new subsequence for this i
        for j in range(i+1, len(nums)):
            if nums[j] > seq[-1]:      # compare with last picked element
                seq.append(nums[j])
        best = max(best, len(seq))
    return best

nums = [10,9,2,5,3,7,101,18]
print(lis_greedy_per_start(nums))  # prints 4 for this example
