landslide =[2,8]
landduration = [4,1]
watersttime = [6]
waterduration = [3]
ans =0

def solve (ls,ld, ws, wd):
    lf = float('inf')
    wf = float('inf')
    for i in range (len(ls)):
        lf = min(lf, ls[i]+ld[i])

    for i in range (len(ws)):
        wf = min(wf, max(lf, ws[i])+wd[i]) 
        return wf
    
    res = min(solve(landslide, landduration, watersttime, waterduration), solve(watersttime, waterduration, landslide, landduration))
    ans = res
    return res
