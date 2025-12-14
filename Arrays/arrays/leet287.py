nums = [1,3,4,2,2]
n= len(nums)
m=0
# for i in range(n):
#     for j in range(i+1,n):

#         if nums[j]==nums[i]:
#             print(nums[i])
nums1=set(nums)
nsum=sum(nums)
n1sum=sum(nums1)
print(nsum-n1sum)

    

    
