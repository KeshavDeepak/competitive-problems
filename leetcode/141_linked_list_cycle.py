# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast:
            fast = fast.next

            if fast:
                fast = fast.next
            else:
                return False
            
            slow = slow.next

            # check if fast and slow have met up
            if fast == slow: # cycle!
                return True
        
        return False
