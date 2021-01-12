# Definition for singly-linked list.
import collections


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

# Graph

'''
discovered를 만들지 않고도 가지치기를 할수 있다면(예를 들어 해당 원소 '#'으로 표시)
만들지 말자. 공간복잡도 O(n)이다.
'''

## DFS

### 재귀구조
def recursive_dfs(v, discovered=[]):
    discovered.append(v)
    for w in graph[v]:
        if w not in discovered:
            discovered = recursive_dfs(w, discovered)
    return discovered

# -> dfs를 이용한 combinations 코드 예시 (LeetCode Graph - 35 참조)

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        S = []
        # 중첩구조 선언
        def dfs(comb, next_i):
            # 탈출 조건 명시
            if len(comb) == k:
                S.append(comb)
                return
            # index를 넘겨 다음 index에 대해서만 재귀호출
            for i in range(next_i, n + 1):
                # 인자로 넘길때 path에 i를 넣어서 전달하기
                dfs(comb+[i], i + 1)
        dfs([], 1)
        return S

### 반복구조(스택) - 재귀와 달리 역순으로 DFS를 수행한다.
def iterative_dfs(start_v):
    discovered=[]
    stack = [start_v]
    while stack:
        v = stack.pop()
        if v not in discovered:
            discovered.append(v)
            for w in graph[v]:
                stack.append(w)
    return discovered

'''
dfs는 백트래킹의 골격이 되는 알고리즘이다.
'''

## BFS

### 반복구조(큐)
def iterative_bfs(start_v):
    discovered = []
    queue = [start_v]
    while queue:
        v = queue.pop(0)
        for w in graph[v]:
            if w not in discovered:
                discovered.append(w)
                queue.append(w)
    return discovered

'''
dfs(반복)은 stack에서 빼낸 v를 검사하지만,
bfs(반복)은 queue에서 빼낸 v의 다음 w들을 검사한다.
'''

# 트리
'''
트리와 그래프의 차이점
그래프 : 순환이 존재
트리 : 순환이 존재하지 않음

n진트리는 child의 갯수가 최대 n개.

정이진트리 Full binary Tree
- child 갯수가 0개 또는 2개 (즉, 노드기준으로 생각)
완전이진트리 Complete binary Tree
- 마지막 레벨을 제외하고는 빈 공간이 없음.  
- 마지막 레벨은 모두 왼쪽부터 차례로 노드가 들어가 있어야함
포화이진트리 Perfect binary Tree
- 마지막 레벨까지 트리의 전체에 빈 공간이 없어야 함
'''
