# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 1st try

class Solution:
    def reverseList(self, head: ListNode, l: int) -> ListNode:
        node, prev = head, None

        while l >= 0:
            next, node.next = node.next, prev
            prev, node = node, next
            l -= 1

        return (prev, next)

    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        root = prev = ListNode(None)
        root.next = head
        for _ in range(m - 1):
            prev = head
            head = head.next

        prev.next, next = self.reverseList(head, n - m)
        head = prev
        while head.next:
            head = head.next
        head.next = next

        return root.next

'''
32ms(56.90%)
14.3MB(59.47MB)
reverseList는 템플릿을 활용했다.
'''

# solution

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        root = start = ListNode(None)
        root.next = head

        # start, end 변수 init
        for _ in range(m-1):
            start = start.next
        end = start.next
        # 이시점에서 start는 대상범위 직전노드, end는 대상범위 첫번째 노드

        # end 뒤의 노드를 하나씩 start 앞으로 끌어당겨오기 --> 뒤집기
        for _ in range(n-m): # 길이만큼
            # tmp는 현재까지 뒤집은 연결 리스트의 첫 노드
            tmp, start.next, end.next = start.next, end.next, end.next,next
            start.next.next = tmp
            # start.next는 끌어당겨온 노드
            # 끌어당겨온 노드의 다음은 이전까지 뒤집어놓은 리스트의 첫 노드
            # 따라서, 뒤집어진 연결 리스트의 앞부분이 하나 추가된 것.
            # 마지막에, end.next.next는 뒤집어진 연결 리스트의 끝부분과 남은 연결리스트의 첫 부분을 연결한다.
        return root.next

'''
28ms(82.35%)
14.3MB(33.40%)다
1. 두 지점을 잡고 끝부분을 당겨와서 앞부분을 갱신하는 개념
2. end는 리스트가 밀려나면서 자동적으로 tail 노드가 된다는 것
이해하면 간단한데 떠올리기가 쉽지 않다
'''
