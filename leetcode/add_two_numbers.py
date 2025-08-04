class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
        answer = ListNode()
        current_node = answer
        carry = 0

        while True:
            # get the current digits -- if one list has been exhausted, replace the digit with 0
            value_1 = l1.val if l1 is not None else 0
            value_2 = l2.val if l2 is not None else 0

            # add the digits up
            current_sum = value_1 + value_2 + carry
            
            # reset carry
            carry = 0

            # account for carry digit if it exists
            if len(str(current_sum)) > 1: # carry digit exists
                carry = current_sum // 10
                current_sum = current_sum % 10
            
            # add the sum to the answer
            current_node.val = current_sum
            
            # move to next node -- if one list has been exhausted, do not move any further
            if l1 is not None: l1 = l1.next
            if l2 is not None: l2 = l2.next
            
            # if both lists have reached None, break
            if l1 is None and l2 is None:
                break
            
            # create a new node for the next digit of the answer
            current_node.next = ListNode()
            current_node = current_node.next
        
        # if carry digit exists, add it to the answer
        if carry > 0:
            current_node.next = ListNode()
            current_node = current_node.next
            current_node.val = carry
        
        return answer
            
            
answer = addTwoNumbers(ListNode(2, ListNode(4, ListNode(3))), ListNode(5, ListNode(6, ListNode(4))))
# answer = addTwoNumbers(ListNode(0), ListNode(0))
# [[9,9,9,9,9,9,9], [9,9,9,9]]
# answer = addTwoNumbers(ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9))))))), ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))

# print out the answer
while answer is not None:
    print(answer.val)
    answer = answer.next