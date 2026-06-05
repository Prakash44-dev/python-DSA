from functools import cache

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:

        def solve(n):
            s = str(n)

            @cache
            def dp(pos, tight, started, prev1, prev2):
                if pos == len(s):
                    return (1, 0)

                limit = int(s[pos]) if tight else 9

                total_cnt = 0
                total_wavy = 0

                for d in range(limit + 1):
                    ntight = tight and d == limit

                    if not started and d == 0:
                        cnt, wav = dp(pos + 1, ntight, False, 10, 10)
                        total_cnt += cnt
                        total_wavy += wav
                    else:
                        add = 0

                        if started and prev2 != 10:
                            if (prev1 > prev2 and prev1 > d) or (
                                prev1 < prev2 and prev1 < d
                            ):
                                add = 1

                        cnt, wav = dp(
                            pos + 1,
                            ntight,
                            True,
                            d,
                            prev1 if started else 10,
                        )

                        total_cnt += cnt
                        total_wavy += wav + add * cnt

                return total_cnt, total_wavy

            return dp(0, True, False, 10, 10)[1]

        return solve(num2) - solve(num1 - 1)