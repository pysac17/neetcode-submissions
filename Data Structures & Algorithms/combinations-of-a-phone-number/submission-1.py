class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res= []
        digittochar = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz",
        }

        def bt(i, curr):
            if len(curr) == len(digits):
                res.append(curr)
                return

            for c in digittochar[digits[i]]:
                bt(i+1, curr+c)

        if digits:
            bt(0, "")

        return res

        