import collections
from typing import List

# 1st try

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        t_map = collections.defaultdict(collections.deque)
        for fr, to in sorted(tickets, reverse=True):
            t_map[fr].append(to)

        itn = []

        def dfs(fr, C):
            if len(itn) == len(tickets) + 1:
                return
            itn.append(fr)
            candidates = t_map[fr]
            if len(itn) < len(tickets) + 1 and not candidates:
                itn.pop()
                C.appendleft(fr)
                return
            for i in range(len(candidates)):
                nxt = candidates.pop()
                dfs(nxt, candidates)

        dfs('JFK', t_map['JFK'])

        return itn

'''
이전에 풀어봤던 문제인데, 백트래킹이 좀 빡세다.
lexical order로 정렬하는건 sort로 쉽게 되는데, 막다른 티켓일경우 다시 되돌아가는 recursive가 어렵다.
30분동안 못풀어서 실패.
'''

# solution

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        t_map = collections.defaultdict(list)
        for fr, to in sorted(tickets):
            t_map[fr].append(to)

        itn = []

        def dfs(a):
            # 그냥 모든 티켓을 다 소모할때까지 dfs를 돌리기만 해도 된다...
            while t_map[a]:
                dfs(t_map[a].pop())
            # dfs 가장 깊숙한곳에서부터 append하므로, 루트 방향은 역순이 된다.
            itn.append(a)

        dfs('JFK')

        # 루트 방향을 뒤집어 정상적인 방향으로 반환한다.
        return itn[::-1]
