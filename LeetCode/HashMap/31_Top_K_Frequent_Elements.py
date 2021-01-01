import collections
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        C = collections.Counter(nums)
        L = [(v,k) for k,v in C.items()]
        L.sort(reverse=True)
        L = [k for v,k in L[:k]]
        return L

'''
104ms(43.51%)
19MB(12.21%)
카운터, 튜플리스트화, 정렬을 모두 써서 느린거같긴한데 일단은 통과.
'''
