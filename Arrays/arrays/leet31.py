nums = [1,2,3]
n=len(nums)
nxtgt=[]
nxtgrt=0
for i in range(n-1,0,-1):
    if nums[i-1]<nums[i]:
        nxtgt=[] 
        for j in nums[i:]:
            if j>nums[i-1] :
                nxtgt.append(j)
               
        nxtgrt=min(nxtgt)
        idx=nums.index(nxtgrt,i)
        nums[i-1],nums[idx] = nums[idx],nums[i-1]
        
        nums[i:] = sorted(nums[i:])
    else:
        nums=nums.reverse()   
print(nums)
            



