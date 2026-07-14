from typing import List
from math import gcd

class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        m = max(nums)

        # dp[g1][g2] = number of ways
        # gcd of seq1 = g1, gcd of seq2 = g2
        dp = [[0] * (m + 1) for _ in range(m + 1)]
        dp[0][0] = 1

        for x in nums:
            new_dp = [row[:] for row in dp]

            for g1 in range(m + 1):
                for g2 in range(m + 1):
                    if dp[g1][g2] == 0:
                        continue

                    ways = dp[g1][g2]

                    # Put x in seq1
                    ng1 = gcd(g1, x)
                    new_dp[ng1][g2] = (
                        new_dp[ng1][g2] + ways
                    ) % MOD

                    # Put x in seq2
                    ng2 = gcd(g2, x)
                    new_dp[g1][ng2] = (
                        new_dp[g1][ng2] + ways
                    ) % MOD

            dp = new_dp

        return sum(dp[g][g] for g in range(1, m + 1)) % MOD