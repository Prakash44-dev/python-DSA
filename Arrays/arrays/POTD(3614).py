class Solution:
    def processStr(self, s: str, k: int) -> str:
        length = 0

        # Forward pass: compute final length
        for ch in s:
            if ch == '*':
                length = max(0, length - 1)
            elif ch == '#':
                length *= 2
            elif ch == '%':
                pass
            else:
                length += 1

        if k >= length:
            return '.'

        # Backward pass: trace k back
        for i in range(len(s) - 1, -1, -1):
            ch = s[i]

            if ch == '*':
                length += 1

            elif ch == '#':
                length //= 2
                if k >= length:
                    k -= length

            elif ch == '%':
                k = length - 1 - k

            else:  # letter
                length -= 1
                if k == length:
                    return ch

        return '.'