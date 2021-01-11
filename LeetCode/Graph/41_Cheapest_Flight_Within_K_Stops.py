import collections
import heapq
import sys

# 1st try
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))

        D = collections.defaultdict(lambda: sys.maxsize)

        # 정점, 가격
        Q = [(src, 0)]

        stop = 0
        while Q and stop <= K:
            fr, price = heapq.heappop(Q)
            for v, w in graph[fr]:
                D[v] = min(D[v], price + w)
                heapq.heappush(Q, (v, D[v]))

            stop += 1

        return D[dst] if D[dst] != sys.maxsize else -1

'''
[테스트 케이스 실패]
10
[[3,4,4],[2,5,6],[4,7,10],[9,6,5],[7,4,4],[6,2,10],[6,8,6],[7,9,4],[1,5,4],[1,0,4],[9,7,3],[7,0,5],[6,5,8],[1,7,6],[4,0,9],[5,9,1],[8,7,3],[1,2,6],[4,1,5],[5,2,4],[1,9,1],[7,8,10],[0,4,2],[7,2,8]]
6
0
7
'''

# 2nd try

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))

        D = collections.defaultdict(lambda: sys.maxsize)

        # 정점, 가격
        Q = collections.deque([(src, 0)])

        stop = 0
        while stop <= K:
            for _ in range(len(Q)):
                fr, price = Q.popleft()
                for v, w in graph[fr]:
                    D[v] = min(D[v], price + w)
                    Q.append((v, D[v]))
            stop += 1

        return D[dst] if D[dst] != sys.maxsize else -1

'''
Memory Limit Exceeded
후.. 화난다.
'''


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))

        D = collections.defaultdict(lambda: sys.maxsize)

        # 정점, 가격
        Q = collections.deque([(src, 0)])

        stop = 0
        while stop <= K:
            for _ in range(len(Q)):
                fr, price = Q.popleft()
                for v, w in graph[fr]:
                    # 핵심은 가지치기. if문을 넣지 않으면 계산했던 D[v]의 다음 노드를 다시 큐에 넣어버린다..
                    if min(D[v], price + w) == price + w:
                        D[v] = min(D[v], price + w)
                        Q.append((v, D[v]))
            stop += 1

        return D[dst] if D[dst] != sys.maxsize else -1

'''
84ms(83.48%)
15.3MB(67.49%)
팁 : sys.maxsize
BFS
1. 그래프 생성
2. 큐 생성(첫 원소를 넣어둠)
3. 전 단계에서 쌓아둔 큐 내역(for _ in range(len(Q))을 뽑으면서 다음 큐 내역을 뒤쪽에 쌓음.
4. 이 때, 이미 찾은 원소를 가지치기 하지 않으면 메모리/시간 초과.
'''

# solution

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))

        # 전체 거리를 보관할 필요가 없기에 D 딕셔너리를 삭제
        # 도착점까지 최단 경로만 계산하면 됨

        # 큐 변수 : [(가격, 정점, 남은 가능 경유지 수)]
        Q = [(0, src, K)]

        while Q:
            price, node, k = heapq.heappop(Q)
            if node == dst:
                return price
            if k >= 0:
                for v, w in graph[node]:
                    alt = price + w
                    heapq.heappush(Q, (alt, v, k - 1))
        return -1

'''
84ms(83.48%)
19.8MB(27.37%)
D를 두지 않고서도 dst까지의 최단경로만 구하면 된다.
다만, 직관성을 위해 가지치기를 하지 않아서 공간복잡도가 커졌다.
dst를 찾자마자 바로 price를 반환할수 있는것은 왜인지 잘 모르겠다...
K 이내의 더 많은 횟수 & 더 낮은 price로 dst에 도착할 수 있는것은 아닌지..
'''
