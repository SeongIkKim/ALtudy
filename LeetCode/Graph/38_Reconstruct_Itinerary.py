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

# 1st solution - 재귀

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        t_map = collections.defaultdict(list)
        # reverse=True 옵션을 넣어줘야, 아래에서 pop(0)가 아닌 pop()으로 처리할 수 있다.
        for fr, to in sorted(tickets, reverse=True):
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

'''
88ms(38.96%)
14.8MB(35.70%)
...어렵게 생각하지 말것.
루트수가 티켓+1이라는 것 보다 그냥 티켓을 다 소모한다는 간단한 조건식이 더 낫다..
'''

# 2nd solution - 스택

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        t_map = collections.defaultdict(collections.deque)
        for fr, to in sorted(tickets):
            t_map[fr].append(to)

        # 경로가 끊어질 경우를 대비하여 itn, stack 두 변수를 만든다.
        itn, stack = [], ['JFK']

        while stack:
            # 반복으로 스택을 구성하되 막히는 부분에서 풀어내는 처리
            while t_map[stack[-1]]:
                # 한번 방문했던 곳을 다시 방문하지 않기 위해, pop으로 값을 아예 제거한다(티켓제거)
                stack.append(t_map[stack[-1]].popleft())
            # 막힐경우, stack의 값을 다시 pop하여 거꾸로 풀어내기
            itn.append(stack.pop())

        return itn[::-1]

'''
80ms(60.27%)
14.4MB(89.54%)
솔직히 이게 더 어려운것같다.
'''
