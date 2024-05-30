# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        ptrs={}
        curr=head

        while curr:
            if ptrs.get(curr.next):
                return True
            ptrs[curr.next]=curr.val
            curr=curr.next
        
        #print(ptrs)
        return False