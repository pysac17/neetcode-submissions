class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        while n not in seen:
            seen.add(n)
            sum_squares = 0
            while n:
                digit = n%10
                square = digit ** 2
                sum_squares += square
                n //= 10
            n = sum_squares
            if n == 1:
                return True

        return False


        