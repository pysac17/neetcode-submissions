from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count = Counter(s1)
        window_count = Counter()

        for i in range(len(s2)):
            window_count[s2[i]] += 1

            # Shrink the window if it's longer than s1
            if i >= len(s1):
                left_char = s2[i - len(s1)]
                window_count[left_char] -= 1
                if window_count[left_char] == 0:
                    del window_count[left_char]

            if window_count == s1_count:
                return True

        return False
