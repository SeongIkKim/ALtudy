class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 1st try

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        root = prev = ListNode(None)
        even_root = even = ListNode(None)
        root.next = odd = head

        while odd and odd.next:
            # 이전의 짝수노드와 다음 짝수노드 잇기
            even.next = odd.next
            # 짝수노드 갱신
            even = odd.next
            # 이전의 홀수노드와 다음 홀수노드 잇기
            odd.next = odd.next.next
            # 이전 홀수노드 기억 및 홀수노드 갱신
            prev, odd = odd, odd.next

        # tail None으로 연결 (List Cycle 방지)
        even.next = None

        if odd and not odd.next:
            odd.next = even_root.next
        else:
            prev.next = even_root.next

        return root.next

'''
36ms(93.17%)
16.4MB(20.95%)
생각은 바로 났는데 even.next = None으로 리스트 사이클을 벗어나기까지가 조금 걸렸다.
'''

# Solution

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None:
            return None

        odd = head
        even_head = even = head.next

        # even이 뒤쪽에 오므로 even 기준으로 while문을 돌리는 듯 하다
        while even and even.next:
            # 훨씬 직관적인 풀이
            odd.next, even.next = odd.next.next, even.next.next
            odd, even = odd.next, even.next

        # 홀수 끝을 짝수 처음과 이어주기
        odd.next = even_head
        return head

'''
36ms(93.17%)
16.4MB(20.95%)
시간복잡도 공간복잡도 동일하지만, 더 직관적인 풀이
1. root=ListNode(None)같은 쓸데없는 헤더를 만들지 않음
2. while문 이하의 내용이 훨씬 직관적임
3. while문의 조건을 odd가 아닌 even기준으로 잡았기 때문에 odd 끝부분과 even_head를 이어주는 과정이 간단
'''
