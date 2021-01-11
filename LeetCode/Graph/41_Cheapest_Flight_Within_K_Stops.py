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
        print(graph)

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
        print(graph)

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
