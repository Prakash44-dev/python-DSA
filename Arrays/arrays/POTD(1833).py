costs =[7,3,3,6,6,6,10,5,9,2]
coins = 56
n= len(costs)
count = 0
sm =0
for i in range(n):
    if costs[i]<coins and sm<coins:
        sm = sm+costs[i]
        if sm<coins:
            count+=1
    
print(count)        

        

