from collections import Counter
import heapq

class Solution:
  def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    count = Counter(nums)
    return heapq.nlargest(k, count.keys(), key=count.get)


# # orr
# class Solution:

#   def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#     count_dict = {}
#     for num in nums:
#       count_dict[num] = count_dict.get(num, 0) + 1

#     # Convert to list of tuples and sort by frequency descending
#     sorted_counts = sorted(count_dict.items(), key=lambda x: x[1], reverse=True)

#     # Extract the first k elements' keys
#     return [item[0] for item in sorted_counts[:k]]
