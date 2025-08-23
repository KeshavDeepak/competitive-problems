# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def swapPairs(self, head):
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        while head and head.next:
            first = head
            second = head.next
            
            # swap
            prev.next = second
            first.next = second.next
            second.next = first
            
            # move pointers forward
            prev = head
            head = head.next
        
        return dummy.next


# helper functions
def convertListToLinked(li):
    if not li:
        return None
    
    dummy = ListNode(0)
    curr = dummy
    
    for val in li:
        curr.next = ListNode(val)
        curr = curr.next
        
    return dummy.next

def printLinkedList(head):
    li = [head.val]
    curr = head.next
    
    while curr:
        li.append(curr.val)
        
        curr = curr.next
    
    print(li)

# main code
solution = Solution()

# test cases
printLinkedList(solution.swapPairs(convertListToLinked([1, 2, 3, 4])))

