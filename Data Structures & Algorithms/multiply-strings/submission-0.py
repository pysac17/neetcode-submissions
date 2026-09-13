class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        m, n = len(num1), len(num2)
        res = [0] * (m+n)
        num1, num2 = num1[::-1], num2[::-1]

        for i1 in range(m):
            for i2 in range(n):
                mult = int(num1[i1]) * int(num2[i2])
                res[i1+i2] += mult
                res[i1+i2+1] += res[i1+i2] // 10   
                res[i1+i2] %= 10

        while len(res)>1 and res[-1] == 0:
            res.pop()

        return "".join(map(str, res[::-1]))