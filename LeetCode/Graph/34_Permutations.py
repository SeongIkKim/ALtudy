from itertools import permutations
from typing import List

# 1st try

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return permutations(nums)

'''
36ms(87.70%)
14.2MB(80.61%)
역시.. 파이썬은 내장함수지.
단, 이방식은 list내의 path가 튜플로 반환된다(permutation은 튜플들의 리스트를 내놓는다)
따라서, 리스트 내의 리스트로 반환하고 싶다면 다음과 같이 map함수를 이용한다.
*map 함수 : 원소들에 대하여 각각 factory 함수를 실행한 결과를 모아 map객체에 담아서 반환한다.

return list(map(list, permutations(nums)))

'''

# 2nd try

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        P = []

        def dfs(nums, path):
            if len(path) == len(nums):
                P.append(path)
                return
            for n in nums:
                if n not in path:
                    dfs(nums, path + [n])

        dfs(nums, [])
        return P

'''
36ms(87.70%)
14.5MB(11.93%)
DFS로 풀어봤다.
중첩함수이므로 dfs의 파라미터에 nums를 빼도 작동한다.
'''

# 1st Solution - dfs

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        prev_elements = []

        def dfs(elements):
            # 리프 노드일 때 결과 추가
            if len(elements) == 0:
                # prev.elements 대신 prev.elements[:]를 사용하여 복사 값을 넘겨준다.
                # 그냥 prev.elements를 추가하면 노드에 대한 참조값을 추가하는 형태가 된다.
                # 간편한 복사 테크닉 --> list[:]
                results.append(prev_elements[:])

            # 순열 생성 재귀 호출
            for e in elements:
                # 남은 elements 중에...
                next_elements = elements[:]
                # 다음에 순서로 넣을 e를 제외하고 나머지를 다음 선택지로 남겨둔다.
                next_elements.remove(e)

                # prev_elements는 path와 같다.
                prev_elements.append(e)
                # 다음 선택지들에 대해 다시 dfs 수행. 여기서 재귀적으로 호출될것이다.
                dfs(next_elements)
                # dfs에 도달해 results를 찍고 나오면, 이제 prev_elements는 다음 e를 위해 재활용해야한다.
                # 따라서 이번에 담아둔 e를 제거하여 다시 기존의 상태로 백트래킹한다.
                prev_elements.pop()

        dfs(nums)
        return results

'''
40ms(66.38%)
14.4MB(33.21%)
백트래킹 과정이 코드로 고스란히 남겨져있다.
처음 봤을땐 이해하기 힘들었는데, 정말 '방식 그대로 옮긴' 코드같다.
'''



