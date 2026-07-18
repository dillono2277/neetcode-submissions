# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        first = head
        second = head
        count = 0

        while first and first.next:
            if count < n:
                first = first.next
                count += 1
            else:
                first = first.next
                second = second.next
        # second.next should be what needs to be removed
        if count < n:
            #remove head
            return head.next
        second.next = second.next.next
        return head





        