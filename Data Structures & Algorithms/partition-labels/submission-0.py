class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count = Counter(s)
        res = []
        temp = set()

        i=0
        j=0

        while j<len(s):
            count[s[j]] -= 1
            temp.add(s[j])

            if count[s[j]] == 0:
                temp.remove(s[j])
            
            if not temp:
                res.append(j-i+1)
                i = j+1
            j+=1
        return res
        