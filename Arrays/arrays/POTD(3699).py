class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7

        m = r - l + 1

        if n == 1:
            return m

        dp_inc = [0] * m
        dp_dec = [0] * m

        # Length = 2
        for i in range(m):
            dp_inc[i] = i          # values smaller than i
            dp_dec[i] = m - 1 - i  # values greater than i

        for _ in range(3, n + 1):

            pref_dec = [0] * (m + 1)
            pref_inc = [0] * (m + 1)

            for i in range(m):
                pref_dec[i + 1] = (pref_dec[i] + dp_dec[i]) % MOD
                pref_inc[i + 1] = (pref_inc[i] + dp_inc[i]) % MOD

            new_inc = [0] * m
            new_dec = [0] * m

            for i in range(m):
                # previous value < current value
                new_inc[i] = pref_dec[i]

                # previous value > current value
                new_dec[i] = (
                    pref_inc[m] - pref_inc[i + 1]
                ) % MOD

            dp_inc, dp_dec = new_inc, new_dec

        return (sum(dp_inc) + sum(dp_dec)) % MOD