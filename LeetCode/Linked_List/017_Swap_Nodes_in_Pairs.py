class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 1st try

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


# Solution 1(Not recommended)
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        cur = head

        while cur and cur.next:
            cur.val, cur.next.val = cur.next.val, cur.val
            cur = cur.next.next

        return head

'''
노드에 속한 정보가 값 하나밖에 없으므로
간단히 노드의 값을 바꾸는 형태.
그러나 노드 값이 여러개이면 오버헤드가 커지고, 문제에서도 언급하듯 이 방식은 원하는 풀이방식이 아님.
노드의 위치를 직접 교환해야한다.
'''

# Solution 2
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        root = prev = ListNode(None)
        prev.next = head

        # head는 홀수번째 노드
        while head and head.next:
            # even이 a를 가리키도록 할당
            even = head.next
            head.next = even.next
            even.next = head

            # prev가 even을 가리키도록 할당
            prev.next = even

            # 다음 비교로 건너뛰기
            prev = head
            head = head.next

        return root.next

'''
내가 푼 방식과 동일한 방식. 그러나..
1. header 대신 root라는 변수면을 사용하여 가독성을 높임
2. odd, next라는 새로운 변수 할당을 하지 않고 그냥 처리
3. 한줄에 여러 할당을 사용하지 않고, 차례대로 swap하여 코드가 짧고 가독성이 높음
'''

# Solution 3
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head and head.next:
            p = head.next
            head.next = self.swapPairs(p.next) # 다음 블록의 swap을 호출한다.
            p.next = head
            return p # 해당 블록의 swap에서 돌려주는 값은, 블록의 첫번째 값(즉, 리스트 전체의 head노드)
        return head

'''
재귀 백트래킹으로 풀이한, 가장 우아한 풀이.
1. 변수 할당이 극단적으로 줄어든다(p밖에 할당하지 않음) -> 공간복잡도가 가장 난다
2. swap부분은 p=head.next /// p.next = head 두 부분밖에 없고, head.next는 다음 블록을 백트래킹 호출하는 부분으로, 가독성이 높다
근데 내가 짜기는 왜이리 힘든 것일까?
'''
