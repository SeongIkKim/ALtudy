import collections
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
