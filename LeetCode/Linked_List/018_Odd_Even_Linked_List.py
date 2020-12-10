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

