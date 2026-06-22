text = "loonbalxballpoon"
dic = {'b':0,'a':0,'l':0,'o':0,'n':0}
for i in text:
    if i in dic :
        dic[i]+=1
mn = min(dic['b'],dic['a'],dic['l']//2,dic['o']//2,dic['n'])
print(mn)        
 
