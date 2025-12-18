nums = [0,1,0,3,12]
n= len(nums)
j=0
for i in range(1,n):
    if nums[i]!=0 :
        nums[i],nums[j]=nums[j],nums[i]
        j+=1
print(nums)