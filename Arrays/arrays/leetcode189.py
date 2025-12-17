nums = [1,2,3,4,5,6,7]
k = 3
n=len(nums)

def reverse(Start,end):
    while Start<end:
        nums[Start],nums[end]=nums[end],nums[Start]
        Start+=1
        end-=1

k=k%n
reverse(0,n-1)
reverse(0,k-1)
reverse(k,n-1)
print(nums)

