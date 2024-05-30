# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow, fast = head, head
#slow and fast ptr will meet sometime if there is cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def hasCycle2(self, head: Optional[ListNode]) -> bool:
        ptrs={}
        curr=head

        while curr:
            if ptrs.get(curr.next):
                return True
            ptrs[curr.next]=curr.val
            curr=curr.next
        
        #print(ptrs)
        return False