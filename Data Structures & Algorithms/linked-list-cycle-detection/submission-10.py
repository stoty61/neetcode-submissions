# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s = set()
        slow = head
        fast = head

        while slow and fast:
            slow = slow.next 
            fast = fast.next
            if fast and fast.next:
                fast = fast.next
            else:
                return False


            if slow == fast:
                return True

            
            

        return False
        