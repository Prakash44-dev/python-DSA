gain = [-5,1,5,0,-7]
n= len(gain)
sm = 0
mx = 0
for i in range(n):
    sm = sm+gain[i]
    if sm>mx :
        mx = sm
print(mx)        
