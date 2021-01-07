from itertools import combinations
from typing import List

# 1st try

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        for i in range(len(nums)+1):
            subsets.extend(map(list,combinations(nums,i)))
        return subsets

'''
32ms(79.82%)
14.6MB(16.70%)
'''

# 2nd try

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []

        def dfs(path, index):
            if len(subsets) == 2 ** len(nums):
                return
            subsets.append(path)
            for i in range(index, len(nums)):
                dfs(path + [nums[i]], i + 1)

        dfs([], 0)
        return subsets

'''
36ms(52.01%)
14.4MB(42.56%)
'''

