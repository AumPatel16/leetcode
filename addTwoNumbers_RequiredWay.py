# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class Solution:
    def addTwoNumbers(self, l1, l2):
        sentinel = curr = ListNode()
        carry = 0

        while l1 or l2:
            if not l1:   # l2 is longer than l1 and l1 is exhausted, swap references
                l1, l2 = l2, l1   # ensures that l1 always points to the longer list, so no checks required for l1
				
            curr_sum = carry + l1.val
            if l2:
                curr_sum += l2.val
				
            l1.val, carry = curr_sum % 10, curr_sum // 10
            curr.next = curr = l1   # first curr.next = l1 and then curr = l1
			
            l1 = l1.next 
            if l2:
                l2 = l2.next
        
        if carry:
            curr.next = ListNode(carry)
            
        return sentinel.next

lis1 = ListNode(2)
lis1.next = ListNode(4)
lis1.next.next = ListNode(3)

lis2 = ListNode(5)
lis2.next = ListNode(6)
lis2.next.next = ListNode(4)
a = Solution()

print(a.addTwoNumbers(lis1,lis2).next.next.val)
