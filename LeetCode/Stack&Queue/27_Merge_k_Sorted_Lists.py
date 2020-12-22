import heapq
from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        root = result = ListNode(None)
        heap = []

        # 각 연결 리스트의 루트를 힙에 저장
        for i in range(len(lists)):
            if lists[i]:
                # 이때, lists[i].val이 중복되면 구분자가 없어져 에러가 나므로, i도 넣어준다.
                # lists.val은 크기 비교를 위해, i는 에러 방지를 위해, lists[i]는 노드 할당을 위해 넣는다.
                heapq.heappush(heap, (lists[i].val, i, lists[i]))

        # 힙 추출 이후 다음 노드는 다시 힙에 저장
        while heap:
            # 최소 힙이므로 node는 최소값 노드
            node = heapq.heappop(heap)
            idx = node[1]  # 최소값 노드
            result.next = node[2]  # 최소값 노드가 있는 리스트의 다음 부분

            result = result.next
            # 뒤에 남은 부분이 있으면 heap에 다시 넣어 다음 비교를 준비한다
            if result.next:
                heapq.heappush(heap, (result.next.val, idx, result.next))

        return root.next

'''
리스트 내에서 최소 값을 찾아 반환하는, 우선순위 큐 문제.
python에서는 우선순위 큐를 주로 heapq로 구현한다.
명시적인 우선순위 큐인 PriorityQueue와 heapq의 차이점은 스레드 세이프 지원여부 뿐이며, PriorityQueue도 내부적으로 heapq를 사용한다.
파이썬의 GIL이라는 특성 상 멀티 스레딩은 의미가 없고 대부분 멀티 프로세싱을 이용한다.
이러한 점에서 PriorityQueue의 스레드 세이프 기능은 사실상 오버헤드만 늘리는 셈이다.
따라서 대부분의 실무에서도 heapq만 사용하며, 모든 우선순위 큐 문제를 heapq로 구현할 것이다.
'''
