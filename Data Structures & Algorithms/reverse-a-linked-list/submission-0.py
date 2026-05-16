# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        array = []
        current = head

        while current:
            array.append(current.val)
            current = current.next
        
        array.reverse()

        newHead = ListNode(array[0])
        newCurrent = newHead

        for i in range(1, len(array)):
            newNode = ListNode(array[i])
            newCurrent.next = newNode
            newCurrent = newNode
        return newHead
            
        
        


        
        