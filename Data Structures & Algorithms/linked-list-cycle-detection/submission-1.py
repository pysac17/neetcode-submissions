# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        jump = head
        double_jump = head

        while double_jump and double_jump.next:
            jump = jump.next
            double_jump = double_jump.next.next
            if jump == double_jump:
                return True
            
        return False
        