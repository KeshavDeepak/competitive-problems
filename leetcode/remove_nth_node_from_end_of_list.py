class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head, n):
        diff_btwn_ptrs = n - 1
        
        ptr_1 = head
        before_ptr_1 = None
        
        # initialize ptr_2 at an offset of diff_btwn_ptrs away from ptr_1
        ptr_2 = head
        for i in range(diff_btwn_ptrs):
            ptr_2 = ptr_2.next
            
        
        # start moving both the pointers until the end of the list has been reached for ptr_2
        while ptr_2.next is not None:
            before_ptr_1 = ptr_1
            ptr_1 = ptr_1.next
            ptr_2 = ptr_2.next
        
        # remove ptr_1 from the list
        if before_ptr_1 is None: # this means that the head node itself has to be removed
            head = ptr_1.next
        else: # ptr_1 is not the head node
            before_ptr_1.next = ptr_1.next
            
        return head

answer = removeNthFromEnd(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2)

print("----------------")
# print out answer
while answer is not None:
    print(answer.val)
    answer = answer.next
            
        