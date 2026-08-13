class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        # Step 1: Count required characters
        target = {}
        for char in t:
            target[char] = target.get(char, 0) + 1

        window = {}
        have, need = 0, len(target)
        res, resLen = [-1, -1], float("inf")
        left = 0

        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1

            if char in target and window[char] == target[char]:
                have += 1

            while have == need:
                # Update result
                if (right - left + 1) < resLen:
                    res = [left, right]
                    resLen = right - left + 1

                # Shrink from left
                window[s[left]] -= 1
                if s[left] in target and window[s[left]] < target[s[left]]:
                    have -= 1
                left += 1

        l, r = res
        return s[l:r+1] if resLen != float("inf") else ""
