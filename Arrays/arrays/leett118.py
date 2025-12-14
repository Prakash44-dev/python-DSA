n=5
pas=[]
prev=[1]


pas.append(prev)
for i in range(n-1):
    prevlen=len(prev)
    pres=[0]*(prevlen+1)
    pres[0],pres[prevlen]=1,1
    for j in range(1,prevlen):
        pres[j]=prev[j]+prev[j-1]
    pas.append(pres)
    prev=pres
print(pas)        

