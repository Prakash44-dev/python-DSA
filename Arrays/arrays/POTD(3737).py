nums = [1,2,2,3]
target = 2
n = len(nums)
c= 0 

for i in range(n):
    temp =0
    for j in range(i,n):
        if nums[j]==target :
            temp+=1
        length = j-i+1
        if temp*2 > length:
            c+=1    
print(c)            