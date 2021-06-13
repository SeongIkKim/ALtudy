class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Solution 1

class Solution:
    def removeNthFromEnd(self, head, n):
        def remove(head):
            # 1. 탈출조건: 끝에 도달하면 0과 None 반환
            if not head:
                return 0, head
            # 2. 재귀조건 : 한번 탈출조건에 도달하고 나면, 재귀조건을 따른다.
            # - i는 끝노드에서 몇번째인지, head.next는 현재 노드의 다음노드를 정한다
            i, head.next = remove(head.next)
            # - 현재 노드가 지워야하는 노드가 아니라면, 원래 그대로 반환한다.
            # - 현재 노드가 지워야하는 노드(i+1 == n)라면, head.next를 반환하여 현재 노드를 건너뛴다.
            return i+1, (head, head.next)[i+1 == n]
        return remove(head)[1] # [0]은 몇번째 노드인지, [1]은 다음노드를 의미하므로 head를 의미한다.

"""
32ms(77.98%)
14.2MB(48.06%)
재귀인건 감이 왔지만 솔직히 이해 안가는 코드다.
"""

# Solution 2

class Solution:
    def removeNthFromEnd(self, head, n):
        fast = slow = head
        for _ in range(n):
            fast = fast.next
        # 예외처리 - fast를 n번 옮겼는데 None이라는 것은 정확히 막다른 노드에 도달했다는 뜻.
        # 이는 곧 n이 Linked List size라는 것을 의미하므로, 뒤에서 size번째, 즉 첫번째 노드를 제외한 나머지 노드를 반환한다(head.next)
        if fast is None:
            return head.next
        # fast는 이미 n번을 갔으므로, slow보다 n개 먼저 도착한다.
        # 거꾸로 말하면, fast.next가 끝에 도달했을때 slow.next는 끝기준으로 n개 뒤쳐져있다는 뜻이다.
        # 따라서 slow.next는 마지막에서 n번째 노드가 된다.
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head

"""
36ms(51.96%)
14.3MB(48.06%)
일반적인 사람의 입장에서 훨씬 이해가 잘가는 코드.
1. Linked List의 size를 아는 우아한 방법(n번 옮겨서 fast가 막다른 노드라면 n=size)
2. 심지어 fast를 미리 n번 옮겨놔서, fast와 동일한 속도로 이동하는 slow를 만들어 간격만큼 뒤에서 거리를 남기는 테크닉
"""


if __name__ == '__main__':
    node = head = ListNode()
    for i in range(1,5):
        node.val = i
        node.next = ListNode()
        node = node.next
    node.val = 5
    S = Solution()
    print(S.removeNthFromEnd(head, 2))
