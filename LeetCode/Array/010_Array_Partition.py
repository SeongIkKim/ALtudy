from typing import List

# 1st try
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum([v for i,v in enumerate(sorted(nums)) if i%2==0])

'''
264ms(46.61%)
16.9MB(6.37%)
코드 골프이긴 하나 속도가 느림
'''

# 2st try
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        s = 0
        for _ in range(len(nums) // 2):
            nums.pop()
            s += nums.pop()

        return s

'''
264ms(46.61%)
16.2MB(99%)
접근 방식이 같아 속도는 똑같지만, enumerate를 쓰지 않고 nums에서 pop처리해 사용공간이 적음
'''

# Solution
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])

'''
244ms(96.85%)
16.9MB(35.56%)
한 배열내에서 step을 뽑아낸다면, if문처리가 아니라 slicing이 가장 pythonic하고 빠르다.
slice -> pythonic(+ faster)
'''
