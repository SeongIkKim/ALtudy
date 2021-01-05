from itertools import combinations
from typing import List

# 1st try

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return list(map(list,combinations(range(1,n+1),k)))


'''
76ms(96.68%)
15.7MB(65.72%)
역시... 파이썬은 내장함수다222
추천 솔루션도 이와 같다.
'''

# 2nd try

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n == 1:
            return [[1]]

        S = []

        def dfs(comb):
            if len(comb) == k and comb not in S:
                S.append(comb)
                return
            for i in range(1, n + 1):
                if i not in comb:
                    dfs(comb.union({i}))

        dfs(set())

        return S

'''
테스트케이스 다 통과는 하는데,
막상 제출하면 time exceed가 뜬다.
not in이 너무 많은가..
'''

# 3rd try

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n == 1:
            return [[1]]

        S = []

        def dfs(comb, next_i):
            if len(comb) == k and comb not in S:
                S.append(comb)
                return
            for i in range(next_i, n + 1):
                dfs(comb.union({i}), i + 1)

        dfs(set(), 1)

        return S

'''
968ms(5.09%)
18.8MB(5.14%)
이전에 돌렸던 i에 대해서는 제끼고 수행하도록 해서 통과는 했는데, 많이 느리다. 
'''

# Solution - dfs

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        results = []

        def dfs(elements, start: int, k: int):
            if k == 0:
                results.append(elements[:])
                return

            # 자신 이전의 모든 값을 고정하여 재귀 호출
            for i in range(start, n + 1):
                elements.append(i)
                dfs(elements, i + 1, k - 1)
                elements.pop()

        dfs([], 1, k)
        return results

'''
452ms(71.19%)
15.9MB(21.47%)
1. k==0일때, 즉 길이를 맞추었을 때 not in 검사 하지않음. 그렇게 하지 않아도 다음 i에 관해 수행함.
2. 리스트 병합은, 역시 append와 pop보다 느리다.
'''

# 내 코드 개선판

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        S = []
        def dfs(comb, next_i):
            if len(comb) == k:
                S.append(comb)
                return
            for i in range(next_i, n + 1):
                dfs(comb+[i], i + 1)
        dfs([], 1)
        return S
