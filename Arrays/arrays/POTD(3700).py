class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1
        sz = 2 * m

        M = [[0] * sz for _ in range(sz)]

        # up transitions
        for i in range(m):
            for j in range(i):
                M[i][m + j] = 1

        # down transitions
        for i in range(m):
            for j in range(i + 1, m):
                M[m + i][j] = 1

        def mat_mul(A, B):
            n1 = len(A)
            n2 = len(B[0])
            k = len(B)

            C = [[0] * n2 for _ in range(n1)]

            for i in range(n1):
                for t in range(k):
                    if A[i][t]:
                        for j in range(n2):
                            C[i][j] = (C[i][j] +
                                       A[i][t] * B[t][j]) % MOD
            return C

        def mat_pow(M, p):
            sz = len(M)
            R = [[1 if i == j else 0 for j in range(sz)]
                 for i in range(sz)]

            while p:
                if p & 1:
                    R = mat_mul(R, M)
                M = mat_mul(M, M)
                p >>= 1

            return R

        vec = [[1] for _ in range(sz)]

        P = mat_pow(M, n - 1)
        res = mat_mul(P, vec)

        return sum(x[0] for x in res) % MOD