# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        tempStack = []
        count = 0

        current1 = l1
        current2 = l2

        num1 = 0
        num2 = 0

        while current1:
            tempStack.append(current1.val)
            current1 = current1.next
            count += 1

        temp = 0
        while tempStack:
            temp = tempStack.pop()
            for i in range(1, count):
                temp = temp * 10
            num1 = num1 + temp
            count -= 1
        
        count = 0
        while current2:
            tempStack.append(current2.val)
            current2 = current2.next
            count += 1

        temp = 0
        while tempStack:
            temp = tempStack.pop()
            for i in range(1, count):
                temp = temp * 10
            num2 = num2 + temp
            count -= 1
        
        totalNum = num1 + num2
        totalStr = str(totalNum)
        totalStrReversed = totalStr[::-1]

        resultDummy = ListNode()
        resultCurrent = resultDummy


        for char in totalStrReversed:
            resultCurrent.next = ListNode(int(char))
            resultCurrent = resultCurrent.next
        return resultDummy.next



                


        
        