#Definition for singly linked list
from typing import List


class ListNode:
    def __init__(self, val = None):
        self.val = val
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = ListNode()
    def append(self, value, next = None):
        newNode = ListNode(value)
        current = self.head
        while(current.next != None):
            current = current.next
        current.next = newNode
    def display(self):
        current = self.head
        print("[ ", end = "")
        while(current.next != None):
            current = current.next
            print(current.val, end = " ")
            
        print("]")

    def listLength(self):
        current = self.head
        count = 0
        while(current.next != None):
            current = current.next
            count+=1
        return count

class Solution:
    def addTwoNumbers(self, l1, l2):
        carry = 0
        lSum = 0
        maxLength = max(l1.listLength(),l2.listLength())
        sum = LinkedList()
        l1 = l1.head.next
        l2 = l2.head.next
        for i in range(maxLength):
            lSum = 0
            if(l1 != None):
                lSum += l1.val
                l1 = l1.next
            if(l2 != None):
                lSum += l2.val
                l2 = l2.next
            lSum += carry
            if(lSum > 9):
                carry = 1
                lSum %= 10
            else:
                carry = 0
            
    
            sum.append(lSum)
           
        if(carry != 0):
            sum.append(carry)
 
        return sum

a = LinkedList()

a.append(0)


b = LinkedList()

b.append(1)



a.display()
b.display()
ans = Solution()
(ans.addTwoNumbers(a,b)).display()