from itertools import combinations, permutations
from typing import List

# 1st try

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        S = []

        def dfs(rest, comb):
            if rest == 0:
                for i in permutations(comb):
                    if i in S:
                        return
                S.append(tuple(comb))
                return

            for key in candidates:
                if key <= rest:
                    dfs(rest - key, comb + [key])

        dfs(target, [])

        return S

'''
안될줄은 알았지만..
permutations과 combinations 남용으로 timeexceed.
'''

# solution - dfs

from itertools import combinations, permutations


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        result = []

        def dfs(csum, index, path):
            # 종료 조건
            if csum < 0:
                return
            if csum == 0:
                result.append(path)
                return

            # 자신부터 하위 원소까지의 나열 재귀 호출
            # 왜 하위원소로 갈 때 자신을 제외하냐면, 중복'조합'이기 때문.
            # [2]+[3]으로 시작하든 [3]+[2]로 시작하든 차이가 없다.
            # 즉, 조합만 따지려면 이전까지 계산했던 부분을 가지치기 하고 그 다음부터 계산해야한다.
            for i in range(index, len(candidates)):
                # 조합이 아닌 순열을 묻는 문제라면 파라미터로 i 대신 0을 넘김(그럼 항상 최초부터 탐색)
                dfs(csum - candidates[i], i, path + [candidates[i]])

        dfs(target, 0, [])

        return result


'''
80ms(63.00%)
14.2MB(65.18%)
1. 백트래킹과 dfs 사용 가능
2. 가지치기를 하기 위해 인덱스 i를 넘겨 다음 부분부터 찾도록 하는 기법.
중복 순열과 중복 조합은 조금 더 까다로움.
중복순열의 경우 itertools의 product(이터러블, repeat(=길이))로도 풀 수 있음.
중복 조합의 경우 길이가 정해져 있으면 itertools의 combinations_with_replacement(이터러블, repeat(=길이))로도 풀 수 있음.
'''
