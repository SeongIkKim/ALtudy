class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 1st try

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        stack = [head]
        node = head
        while node.next != None:
            stack.append(node.next)
            node = node.next

        head = stack[-1]
        while len(stack) > 1:
            node = stack.pop()
            node.next = stack[-1]

        stack.pop().next = None

        return head

'''
40ms(25.65%)
15.7MB(34.01%)
stack 이용한 iterative.
'''

