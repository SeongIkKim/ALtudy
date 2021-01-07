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



