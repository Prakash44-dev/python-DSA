# nums = [1,2,3,-3,1,1,1,4,2,-3]
# k = 3
# n = len(nums)
# count=0
# for i in range(0,n):
#     if nums[i]==k:
#         count+=1
#     sum= nums[i]
    
#     for j in range(i+1,n):

#         if sum+nums[j]==k:
#             count+=1
#         sum = sum+nums[j]
# print(count)        
nums = [1,2,3]
k = 3

count = 0
prefix = 0
freq = {0:1}

for num in nums:

    prefix += num

    if prefix - k in freq:
        count += freq[prefix-k]

    freq[prefix] = freq.get(prefix,0) + 1

print(count)