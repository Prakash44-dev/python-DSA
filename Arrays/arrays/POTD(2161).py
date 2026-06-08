nums = [9,12,5,10,14,3,10]
pivot = 10
lp =[]
gp= []
p=[]
for i in range(len(nums)):
    if nums[i]<pivot:
        lp.append(nums[i])
    elif nums[i]>pivot:
        gp.append(nums[i])
    else :
        p.append(nums[i])
res = lp+p+gp 
print(res)                