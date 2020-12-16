# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode, prev: ListNode, l: int) -> tuple:
        # print(locals())
        if l <= 0:
            if head:
                next, head.next = head.next, prev
                return (head, next)
            else:
                return (prev, None)
        next, head.next = head.next, prev

        return self.reverseList(next, head, l - 1)

    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        root = head
        for _ in range(m - 2):
            head = head.next
        prev = head
        left_chain, head = head, head.next
        print(left_chain, head)

        left_chain.next, next = self.reverseList(head, None, n - m)
        # print('####')
        # print( left_chain)
        # print(left_chain.next)
        # print(next)
        while head.next:
            head = head.next
        head.next = next

        return root






