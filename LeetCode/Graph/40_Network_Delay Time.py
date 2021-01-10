import collections
import heapq
from typing import List

# 1st try

class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:

        visited = set()

        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        ts = []

        def bfs(source, t):
            visited.add(source)
            if not graph[source]:
                ts.append(t)

            q = collections.deque()

            for v, w in graph[source]:
                q.append((v, w))

            while q:
                target, weight = q.popleft()
                bfs(target, t + weight)

        bfs(K, 0)

        if len(visited) != N:
            return -1

        return max(ts)

'''
Memory Limit Exceeded
[[1,2,1],[2,1,3]]
2
2
'''

# 2nd try

class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:

        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        ts = []

        def bfs(source, t, visited=[]):
            if source in visited:
                return
            visited.add(source)
            if not graph[source] and len(visited) == N:
                ts.append(t)

            q = collections.deque()

            for v, w in graph[source]:
                q.append((v, w))

            while q:
                target, weight = q.popleft()
                bfs(target, t + weight, visited)
                visited.remove(target)

        bfs(K, 0, set())

        return min(ts) if min(ts) > 0 and ts != [] else -1

'''
[[2,1,1],[2,3,1],[3,4,1]]
4
2

output = 1 , expected = 2
'''

# solution

class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = collections.defaultdict(list)
        # 그래프 인접 리스트 구성
        for u,v,w in times:
            graph[u].append((v,w))

        # 큐 변수 : [(소요 시간, 정점)]
        Q = [(0,K)]
        dist = collections.defaultdict(int) # 각 노드 도달 최단거리

        # 우선순위 큐 최솟값 기준으로 정점까지 최단 경로 삽입
        while Q:
            time, node = heapq.heappop(Q)
            # 최단경로가 아직 나오지 않은 node에 대해서
            if node not in dist:
                dist[node] = time
                for v, w in graph[node]:
                    # 시간(alt)는 현재 시간 + 다음 노드까지 도달하는 시간
                    alt = time + w
                    heapq.heappush(Q, (alt, v))

        # 모든 노드의 최단 경로 존재 여부 판별
        # 즉, times가 끊어져있어 모든 노드를 도달하지 못하는 것이 아닌지 판별
        if len(dist) == N:
            return max(dist.values())
        return -1

'''
492ms(44.36%)
16.4MB(15.01%)
1. 최단경로 알고리즘은 다익스트라 알고리즘을 사용한다(edge에 음수가 존재하지 않는다면)
2. 다익스트라 알고리즘은 우선순위큐를 사용한다(python에서는 heapq사용)
3. 최단시간은 각 노드에 도달했을때마다 딕셔너리에 기록한다
'''

