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

# 2nd try

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        if head.next:
            node= self.reverseList(head.next)
            node.next = head
            head.next = None
        return head

'''
# head.next = None
Error - Found cycle in the ListNode
마지막에 빠져나오면서 1->2, 2->1을 만들어 무한순환을 만들어 실패.
# head.next = None을 넣지 않으면
최후에 return하는 head가 tail node라서 불가.
'''

# 1st Solution(재귀)

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def reverse(node: ListNode, prev: ListNode = None):  # prev : 이전노드 기억
            # empty list 예외처리
            if not node:
                return prev
            # 현재노드 node를 기준으로 다음과 같이 할당한다.
            # next : 기존의 다음 노드
            # node.next : 기억해둔 이전 노드(prev)
            # 따라서 재귀 호출은 기존의 순서(1-2-3-4-5)를 따라가되, next의 연결은 역(prev)으로 진행
            next, node.next = node.next, prev
            return reverse(next, node)  # 기존의 다음순서 재귀호출, 그리고 현재 노드를 prev로 지정

        # 가장 깊숙한 노드(5)로 들어가서 해당 노드만을 계속 반환하므로, 마지막의 return값도 기존의 tail node(5)가 된다.
        return reverse(head)

'''
32ms(85.28%)
20.5MB
문제가 쉬워서 코드는 직관적이지만..
가장 깊은 깊이로 들어가서 tail을 그대로 끄집어내기 위해 return문에 재귀호출을 한다.
next, node.next, prev 스왑을 유심히 볼 것.
'''


# 2nd Solution(반복)

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        node, prev = head, None

        while node:  # node가 tail node라면 next = None, 이후에 node = None이되므로 while문을 탈출한다.
            next, node.next = node.next, prev  # 기존의 방향을 temp에 저장해두는것과 같다.
            prev, node = node, next

        return prev  # while문을 탈출할 때 node는 None이므로, 이전의 노드 prev가 tail node.

'''
32ms(85.28%)
15.5MB(41.98%)
prev, node, next를 이용하여 순서를 바꾸는 방식은 같지만, 여러 변수를 전달하기 위해 새 함수를 만들 필요가 없다.
또한, 일반적으로 속도와 사용메모리가 더 빠르다.
'''
