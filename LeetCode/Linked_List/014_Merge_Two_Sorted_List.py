class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return None
        elif l1 and not l2:
            return l1
        elif not l1 and l2:
            return l2

        temp = ListNode()
        (current, other) = (l1, l2) if l1.val <= l2.val else (l2, l1)

        while current.next:
            if current.next.val <= other.val:
                current = current.next
            else:
                temp = current.next
                current.next = other
                current = current.next
                other = temp

        if other:
            current.next = other

        return l1 if l1.val <= l2.val else l2

'''
36ms(71.62%)
14.3MB(6.29%)
'''

# Solution
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # l1과 l2중 더 작은 값을 찾아 l1의 자리에 오도록 만든다.
        if (not l1) or (l2 and l1.val > l2.val):
            l1,l2 = l2,l1 #  pythonic한 swap
        if l1:
            l1.next = self.mergeTwoLists(l1.next,l2) # l1.next와 l2를 비교하여 더 작은값을 l1.next에 오도록 재귀호출
        return l1 # l1(더 작은값) 반환

'''
36ms(71.62%)
14.2MB(46.11%)
1. 재귀함수 사용 - 리스트를 마치 노드처럼 사용할것(l1, l2의 크기비교로 노드 스왑)
2. 노드 swap하여 작은 쪽을 l1으로 고정
'''

