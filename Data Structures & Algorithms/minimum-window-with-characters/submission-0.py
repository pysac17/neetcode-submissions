class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        
        left = 0
        ans = ""
        for i in range(len(s)):
            temp_t = t
            if s[i] in t:
                left = i
                temp_t = temp_t.replace(s[i], "", 1)
                right = i+1
                while right<=len(s)-1 and len(temp_t)!=0:
                    if s[right] in temp_t:
                        temp_t = temp_t.replace(s[right], "", 1)
                    right += 1
                if len(temp_t) == 0:
                    window = s[left:right]
                    if ans == "" or len(window) < len(ans):
                        ans = window
        return ans


                    
        