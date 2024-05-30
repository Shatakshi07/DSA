# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3=ListNode(0)

        curr1=l1
        curr2=l2
        
        curr3=l3
        c=0

        while curr1 or curr2:
            val1 = curr1.val if curr1 is not None else 0
            val2 = curr2.val if curr2 is not None else 0

            n=val1 + val2 + c
            c=n//10

            curr3.next=ListNode(n%10)
            curr3=curr3.next

            if curr1 is not None:
                curr1 = curr1.next
            if curr2 is not None:
                curr2 = curr2.next

        if c==1:
            curr3.next=ListNode(c)

        return l3.next

        

        
            