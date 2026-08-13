class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        sorted_keys = sorted(hashmap, key=lambda x: hashmap[x], reverse=True)
        return sorted_keys[:k]

        