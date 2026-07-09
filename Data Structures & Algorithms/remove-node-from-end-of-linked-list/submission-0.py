# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        counter = 0
        cur = head
        prev = None

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        rev = prev
        prev = None

        while rev:
            counter += 1
            if counter == n:
                # print(rev.val)
                rev = rev.next
                continue
            temp = rev.next
            rev.next = prev
            prev = rev
            rev = temp

        return prev

        # while cur:
        #     temp = cur.next
        #     cur.next = prev
        #     prev = cur
        #     cur = temp

        # return prev