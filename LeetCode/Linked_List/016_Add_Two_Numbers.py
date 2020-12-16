import functools


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

# 1st solution

from typing import List

class Solution:
    # 연결 리스트 뒤집기
    def reverseList(self, head: ListNode) -> ListNode:
        node, prev = head, None

        while node:
            next, node.next = node.next, prev
            prev, node = node, next

        return prev

    # 연결 리스트를 파이썬 리스트로 변환
    def toList(self, node: ListNode) -> List:
        list: List = []
        while node:
            list.append(node.val)
            node = node.next
        return list

    # 파이썬 리스트를 연결 리스트로 변환
    def toReversedLinkedList(self, result: str) -> ListNode:
        prev: ListNode = None
        for r in result:
            node = ListNode(r)
            node.next = prev
            prev = node

        return node

    # 두 연결 리스트의 덧셈
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a = self.toList(self.reverseList(l1))
        b = self.toList(self.reverseList(l2))

        # str 형변환후 join하고 int변환하거나, map함수를 사용할수도 있지만, reduce를 사용하는 편이 가장 우아하다.
        # reduce는 데이터를 누적하여 집계하기위해 사용되는 함수로, functools 패키지는 고계함수(함수를 다루는 함수)들을 모아놓은 패키지이다.
        resultStr = functools.reduce(lambda x, y: 10 * x + y, a, 0) + functools.reduce(lambda x, y: 10 * x + y, b, 0)

        # 최종 계산 결과 연결 리스트 변환
        return self.toReversedLinkedList(str(resultStr))


'''
80ms(11.54%)
14.3MB(12.00%)
연결리스트를 뒤집고 -> 리스트화하고 -> 숫자를 더하고 -> 다시 리스트화시킨다.
처음에 바로 생각나는 풀이지만 풀이가 더럽고, 우아하지 않음.
1. reduce함수를 사용하는 방법을 눈여겨보자.
'''

# 2nd solution

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = head = ListNode(0) # head와, 추후에 return할 root를 동시에 할당하기

        carry = 0
        while l1 or l2 or carry: # 지저분한 while문 이하를 세가지 조건으로 압축
            sum = 0
            # 두 입력값의 합 계산 - l1, l2를 한번씩 검사하므로 굳이 and, not으로 긴 조건을 붙여 분리할 필요가 없다.
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next

            # 몫(자리올림수)과 나머지(값) 계산 - 겹치던 부분을 마지막에 한번에 계산.
            carry, val = divmod(sum + carry, 10) # s // 10, s % 10을 한번에 처리해주는 divmod 함수.
            head.next = ListNode(val)
            head = head.next

        return root.next

'''
72ms(49.17%)
14.3MB(12.00%)
전가산기를 응용한 방식으로, 내 풀이와 비슷하다.
그러나 l1,l2에 대한 if문의 개별사용, divmod 함수 등으로 가독성이 훨씬 좋다.
'''


