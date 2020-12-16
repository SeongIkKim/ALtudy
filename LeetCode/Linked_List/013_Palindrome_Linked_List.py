import collections


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head == None or head.next == None:
            return True

        result = []
        node = head
        result.append(node.val)
        while node.next:
            node = node.next
            result.append(node.val)
        if result == result[::-1]:
            return True
        return False

'''
64ms(89.30%)
24.5MB(15.25%)
O(n)이긴 한거같은데 공간복잡도가 O(1)은 아닌듯 하다.
'''

# Solution

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head == None or head.next == None:
            return True

        result = collections.deque()
        node = head

        while node is not None:
            result.append(node.val)
            node = node.next

        while len(result) > 1:
            if result.popleft() != result.pop():
                return False

        return True

'''
68ms(74.38%)
24.2MB(30.90%)
deque를 사용하였고, result의 공간을 0으로 만들었다.
그러나 별 차이가 없어보이긴 한다...
'''
