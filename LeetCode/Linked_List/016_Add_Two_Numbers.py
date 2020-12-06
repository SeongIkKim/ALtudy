class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 1st try

def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    result, prev = ListNode(), ListNode()
    head = result
    carry = 0
    while l1 or l2:
        if l1 and l2:
            s = l1.val + l2.val + carry
            carry, s = s // 10, s % 10
            result.val = s
            result.next, l1, l2 = ListNode(), l1.next, l2.next
            result, prev = result.next, result
        elif l1 and not l2:
            s = l1.val + carry
            carry, s = s // 10, s % 10
            result.val = s
            result.next, l1 = ListNode(), l1.next
            result, prev = result.next, result
        elif not l1 and l2:
            s = l2.val + carry
            carry, s = s // 10, s % 10
            result.val = s
            result.next, l2 = ListNode(), l2.next
            result, prev = result.next, result

    if carry:
        result.val = carry
    else:
        prev.next = None

    return head

'''
68ms(73.27%)
14.3MB(26.27%)
여차저차 직관적으로 풀었지만, 풀이에 중복이 많고 불필요한 변수가 많다.
'''
