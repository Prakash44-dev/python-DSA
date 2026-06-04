# x = 2.00000, n = 10
# res = 1
# for i in range(n):
#     res = res*x

# print(res)
class Solution:
    def myPow(self, x, n):
        if n < 0:
            x = 1/x
            n = -n

        res = 1
        while n:
            if n & 1:
                res *= x
            x *= x
            n >>= 1
        return res
