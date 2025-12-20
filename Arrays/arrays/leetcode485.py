# nums = [1,1,0,1,1,1]
# n=len(nums)
# count0=0
# count1=0

# for i in range(n) :
    
    
#     if nums[i]==1:
#         count0=0
#         count1+=1
        
#     else:
#         count1=0
#         count0+=1
        
# print(max(count0,count1))
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        nums = [1,1,0,1,1,1]
        count = 0
        max1 = 0
        
        for x in nums:
            if x == 1:
                count += 1
                max1 = max(max1, count)
            else:
                count = 0
        
        return max1

