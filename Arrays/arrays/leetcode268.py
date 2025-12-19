nums=[9,7,8,6,5,4,2,1]
n = len(nums)
total = (n * (n + 1)) // 2
print(total - sum(nums))
