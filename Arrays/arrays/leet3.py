s = "abcabcbb"
a=[]
count=0
le=0
for i in s :
    if i in a :
        a=a[a.index(i)+1:]
        
    a.append(i)    
     


    

print(len(a))