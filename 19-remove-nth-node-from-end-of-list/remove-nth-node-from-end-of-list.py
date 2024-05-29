# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow=head
        start=head
        if head.next:
            fast=head.next
        else:
            return None
        
        c=2
        
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if fast!=None:
                c+=2
            else:
                c+=1

        #print(c)
        #print(n)
        n=c-n+1

        #print(n)
        if n==1:
            return head.next
        temp=head
        h=n//2
        if n%2==0:
            h-=1
            finish=head.next
        else:
            finish=head
        
        
        while h>0:
            start=start.next
            temp=finish.next
            finish=finish.next.next
            h-=1
        
        temp.next=finish.next

        return head

        
