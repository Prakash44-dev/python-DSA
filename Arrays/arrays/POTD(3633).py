# landsttime = [2,8]
# landduration  = [4,1]
# watersttime = [6]
# waterduration = [3]   
# landmin = float('inf')
# watermin = float('inf')
# for i in range(len(landsttime)):
#     if landsttime[i] +landduration[i]<landmin:
#         landmin = landsttime[i] +landduration[i]
#         print(landmin)
# for i in range(len(watersttime)):
#     if watersttime[i] +waterduration[i]<watermin:
#         watermin = watersttime[i] +waterduration[i]
#         print(watermin)
# res = max(landmin, watermin)
# print(res)        
from typing import List

class Solution:
    def earliestFinishTime(
        self,
        landStartTime: List[int],
        landDuration: List[int],
        waterStartTime: List[int],
        waterDuration: List[int]
    ) -> int:

        def solve(start1, dur1, start2, dur2):
            min_end = float('inf')

            for i in range(len(start1)):
                min_end = min(min_end, start1[i] + dur1[i])

            ans = float('inf')

            for i in range(len(start2)):
                ans = min(ans, max(start2[i], min_end) + dur2[i])

            return ans

        return min(
            solve(landStartTime, landDuration, waterStartTime, waterDuration),
            solve(waterStartTime, waterDuration, landStartTime, landDuration)
        )
    


class Solution:
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        def solve(ls, ld, ws, wd):
            finish = float('inf')

            for i in range(len(ls)):
                finish = min(finish, ls[i] + ld[i])

            ans = float('inf')

            for i in range(len(ws)):
                ans = min(ans, max(finish, ws[i]) + wd[i])

            return ans

        return min(
            solve(landStartTime, landDuration, waterStartTime, waterDuration),
            solve(waterStartTime, waterDuration, landStartTime, landDuration)
        )
    