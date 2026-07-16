from math import gcd
from typing import List

class Solution:
    def gcdSum(self, nums: List[int]) -> int:
        pre = []
        mx = 0

        for x in nums:
            mx = max(mx, x)
            pre.append(gcd(x, mx))

        pre.sort()

        ans = 0
        n = len(pre)
        for i in range(n // 2):
            ans += gcd(pre[i], pre[n - 1 - i])

        return ans
    