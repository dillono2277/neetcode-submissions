# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None
        
        prev = None
        current = second
        while current:
            nextNode = current.next
            current.next = prev
            prev = current
            current = nextNode
        
        first = head
        second = prev

        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1


            first = temp1
            second = temp2


        # rightStack = []
        # newHead = head
        # returnThing = newHead


        # current = head
        # n = 0
        # while current is not None:
        #     rightStack.append(current)
        #     current = current.next
        #     n += 1
        # leftCount = math.ceil(n/2)
        
        # current = head
        # while leftCount >= 0 and current is not None:
        #     newHead.next = rightStack.pop()
        #     newHead.next.next = current.next
        #     newHead = newHead.next.next
        #     current = current.next
        #     leftCount -= 1
        # return returnThing



        