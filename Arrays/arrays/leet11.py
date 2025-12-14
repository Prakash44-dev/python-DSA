height = [1,8,6,2,5,4,8,3,7]
n=len(height)
area=0
a=0
i=0
j=n-1
while(i<j):
    a=min(height[i],height[j])*(j-i)
    if a>=area:
        area=a
    if height[i]>height[j]:
        j-=1
    else :
        i+=1
print(area)