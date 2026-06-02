nums = [3, 5, 4, 1, 1]  

nums.sort()
result=[]
print(nums)
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i] == nums[j]:
            result.append(nums[i])
            print("Repeated number is:", nums[i])
            
for i in range(len(nums)-1):
    if (nums[i]+1) != nums[i+1]:
        result.append(nums[i]+1)
        print("Missing number is:", nums[i]+1)
        break
 
print(result)       
        



    
        

    

