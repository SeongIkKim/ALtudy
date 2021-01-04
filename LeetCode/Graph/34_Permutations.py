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
'''


