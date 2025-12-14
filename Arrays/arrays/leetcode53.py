nums = [-2,1,-3,4,-1,2,1,-5,4]

subarrays=[]
subarrayssums=[]
n=len(nums)
for i in range(n):
    for j in range(i,n):
        subarrays.append(nums[i:j+1])
print(subarrays)
for k in subarrays:
    subarrayssums.append(sum(k))
print(max(subarrayssums))    
