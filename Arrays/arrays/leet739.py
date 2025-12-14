s=[73,74,75,71,69,72,76,73]

res=[]
for i in range (len(s)):
    temp=False
    for j in range(i+1,len(s)):
        if(s[j]>s[i]) :
            res.append(j-i)
            temp=True
            break
        
    
    if not temp:
      res.append(0)            
# res.append(0)   
# [1, 1, 4, 2, 1, 1, 0,0]   
        
            
          
    
    


        
        
            
            
print(res)        

