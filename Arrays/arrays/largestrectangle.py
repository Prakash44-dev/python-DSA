l=[2,1,5,6,2,3]
n=len(l)-1
max=0
a=0
area=0

for i in range (n):
    j=i+1
    a =l[i]+l[j]
    if a>max:
        max=a
        if l[i]>l[j]:
            area = l[j]*2
        if l[j]>l[i]:
            area = l[i]*2    
print(area)        
