# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        front = head
        behind = head
        new_head = ListNode(-1, head)
        prev = new_head

        for _ in range(n):
            front = front.next
        
        while front:
            front = front.next
            prev = behind
            behind = behind.next

        prev.next = behind.next

        return new_head.next
