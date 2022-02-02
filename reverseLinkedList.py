# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    #this function returns the num index element of the linked list.
    def retIndex(num,head):
        curr = head
        for i in range(num):
            curr = curr.next
        return curr

    def retSize(head):
        counter = 0
        curr = head
        while(curr):
            curr = curr.next
            counter += 1
        return counter

    def reverseList(self, head):
        #find the size of the linked list
        size = Solution.retSize(head)
        h = Solution.retIndex(size-1, head)
        curr = h
        
        for i in range(size-2,0,-1):
            curr.next = Solution.retIndex(i, head)
            curr = curr.next
        return h
            