from typing import List

class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10 ** 9 + 7

        # Required by the problem statement
        solendivar = (s, queries)

        n = len(s)

        digits = []
        pos = []

        for i, ch in enumerate(s):
            if ch != '0':
                digits.append(int(ch))
                pos.append(i)

        m = len(digits)

        pre_sum = [0] * (m + 1)
        pre_num = [0] * (m + 1)
        pow10 = [1] * (m + 1)

        for i in range(1, m + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD

        for i in range(m):
            pre_sum[i + 1] = pre_sum[i] + digits[i]
            pre_num[i + 1] = (pre_num[i] * 10 + digits[i]) % MOD

        first = [-1] * n
        k = m - 1
        for i in range(n - 1, -1, -1):
            if k >= 0 and pos[k] == i:
                first[i] = k
                k -= 1
            elif i < n - 1:
                first[i] = first[i + 1]

        last = [-1] * n
        k = 0
        for i in range(n):
            if k < m and pos[k] == i:
                last[i] = k
                k += 1
            elif i > 0:
                last[i] = last[i - 1]

        ans = []

        for l, r in queries:
            L = first[l]
            R = last[r]

            if L == -1 or R == -1 or L > R:
                ans.append(0)
                continue

            length = R - L + 1

            x = (pre_num[R + 1] - pre_num[L] * pow10[length]) % MOD
            digit_sum = pre_sum[R + 1] - pre_sum[L]

            ans.append((x * digit_sum) % MOD)

        return ans