# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge(self, left, right):
        answer = ListNode(-1)
        curr = answer

        while left and right:
            if left.val <= right.val: # left is smaller (or equal)
                curr.next = left
                curr = curr.next
                left = left.next
            else: # right is smaller
                curr.next = right
                curr = curr.next
                right = right.next

        while left:
            curr.next = left
            curr = curr.next
            left = left.next
        
        while right:
            curr.next = right
            curr = curr.next
            right = right.next
        
        return answer.next
                
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # base case
        if not head or not head.next:
            return head

        # main case
        slow = head
        fast = head
        prev = slow

        while fast:
            fast = fast.next

            if fast:
                fast = fast.next
            else:
                break

            prev = slow
            slow = slow.next 

        # break left half 
        prev.next = None
        
        # sort the two halves
        left = self.sortList(head)
        right = self.sortList(slow)

        # merge the sorted halves
        return self.merge(left, right)
