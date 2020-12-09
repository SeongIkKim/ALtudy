class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return None
        if not head.next:
            return head

        header = ListNode()
        header.next = head
        prev, odd, even = header, header.next, header.next.next
        next, even.next = even.next, odd
        odd.next, prev.next = next, even

        while odd.next and odd.next.next:
            prev, odd, even = odd, odd.next, odd.next.next
            next, even.next = even.next, odd
            odd.next, prev.next = next, even

        return header.next

'''
24ms(94.64%)
14.4MB(18.25%)
조금 변수 할당이 복잡해도 정석대로 푼듯?
'''


