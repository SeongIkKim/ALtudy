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
