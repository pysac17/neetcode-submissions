class Solution:
    def reverse(self, x: int) -> int:
        MAX_INT, MIN_INT = 2**31 - 1, -2**31
        sign = -1 if x<0 else 1
        x_rev = 0
        x = abs(x)
        while x:
            digit = x%10
            x_rev = x_rev*10 + digit
            x //= 10
        x_rev = sign*x_rev
        if x_rev>MAX_INT or x_rev<MIN_INT:
            return 0
        return x_rev
        