# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast != None:
            fast = fast.next
            if fast:
                fast = fast.next
            else:
                return slow

            slow = slow.next
        
        return slow
