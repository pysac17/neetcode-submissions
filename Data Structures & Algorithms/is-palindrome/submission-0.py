class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        if len(s)%2 == 0 :
            print(s)
            lower = len(s)//2-1
            upper = len(s)//2
            while lower >= 0 and upper < len(s):
                if s[lower] != s[upper]:
                    return False
                lower -= 1
                upper += 1
        else:
            lower = len(s)//2
            upper = len(s)//2
            while lower >= 0 and upper < len(s):
                if s[lower] != s[upper]:
                    return False
                lower -= 1
                upper += 1
        return True
            