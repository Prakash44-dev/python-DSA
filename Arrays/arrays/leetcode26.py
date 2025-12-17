nums = [0,0,1,1,1,2,2,3,3,4]
n= len(nums)
j=0
for i in range(1,n):
    if nums[i]!=nums[j]:
        j+=1
        nums[j]=nums[i]
print(j+1)
print(nums[:j+1])        