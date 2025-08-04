# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def mergeTwoLists(list1, list2):
        # base case
        if list1 == None or list2 == None:
            if list1:
                return list1
            
            if list2:
                return list2
            
            return None 
        
        # recursive case
        if list1.val <= list2.val:
            list3 = list2.next
            list2.next = list1.next
            list1.next = list2
            
            head = list1
            
            list1 = list2.next
            list2 = list3
            
            mergeTwoLists(list1, list2)
            
        else:
            list3 = list1.next
            list1.next = list2.next
            list2.next = list1
            
            head = list2
            
            list2 = list1.next
            list1 = list3
            
            mergeTwoLists(list1, list2)
        
        return head
        
        
list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))

list1 = ListNode(2)
list2 = ListNode(1)

list1 = ListNode(5)
list2 = ListNode(1, ListNode(2, ListNode(4)))

answer = mergeTwoLists(list1, list2)

# Function to print the linked list
def printLinkedList(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Print the merged linked list
printLinkedList(answer)


#!! does not work for the latest input