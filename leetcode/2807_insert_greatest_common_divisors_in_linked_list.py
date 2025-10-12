# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def get_gcd(self, a, b):
        #* ensure a is the larger number
        if a < b: a, b = b, a
        
        while b != 0:
            a, b = b, a % b  
        
        return a
        
    def insertGreatestCommonDivisors(self, head: ListNode) -> ListNode:
        p1 = head
        
        while p1.next:
            p2 = p1.next
            
            #* get the gcd value
            gcd = self.get_gcd(p1.val, p2.val)
            
            #* insert this in between the nodes
            gcd_node = ListNode(gcd)
            
            p1.next = gcd_node
            gcd_node.next = p2
            
            #* move p1 forward
            p1 = p2
        
        return head
            
            

#* main code
solution = Solution()

#* test cases
print(solution.insertGreatestCommonDivisors(ListNode(18, ListNode(6, ListNode(10, ListNode(3))))))

print(solution.insertGreatestCommonDivisors(ListNode(5, ListNode(2, ListNode(10, ListNode(25))))))        