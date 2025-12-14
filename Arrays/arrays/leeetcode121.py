import math
prices = [7,1,5,3,6,4]
n=len(prices)
buy=math.inf
sell=0
for i in range(n):
    if prices[i]<buy:
        buy=prices[i]
        
for j in range((prices.index(buy)+1),n):
    if prices[j]>sell:
        sell=prices[j]
       
print(sell-buy)        

