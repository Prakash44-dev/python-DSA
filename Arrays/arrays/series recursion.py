s=[]
def series(n):
    
    if n == 0:
        return 0
    s.append(n)
    series(n-1)
series(5)
print(s)    
