import math
from typing import List

# 1st try

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        return [math.prod(nums[:i]+nums[i+1:]) for i in range(len(nums))]

'''
시간초과
for문 하나 + math.prod면 당연히 O(n^2)이긴 한데, 혹시 몰라서 넣어봤다.
'''

# solution

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []

        # 왼쪽에서부터 차례로 축적하는 곱셈
        p = 1
        for i in range(len(nums)):
            out.append(p)  # nums[i]를 넣는것이 아니라 지금까지 축적해온(즉, 왼쪽 곱인) p를 넣는다.
            p *= nums[i]

        # 왼쪽 곰셈 결과에 오른쪽 값을 차례대로 곱셈
        p = 1
        for i in range(len(nums) - 1, -1, -1):
            out[i] *= p  # 자기 기준으로 오른쪽의 곱을 기존의 out[i](즉, 왼쪽 곱)에 곱한다.
            p *= nums[i]

        return out

'''
236ms(46.05%)
21.1MB(39.17%)
기상천외한 방법을 사용한다..
하나의 포인터를 이용해 좌우로 훑으면서 왼쪽 곱과 오른쪽 곱을 더한다.
자기 차례에 왔을 때 자신이 아니라 이전까지의 곱을 곱하여 결과적으로는 한쪽 곱과 나머지 한쪽 곱을 곱하게 된다.
'''

'''
O(n)을 원하면, 좌우로 훑는것을 생각해보자.
for문을 반복하지 않아도, 자기자신을 기준으로 좌우가 갈려서 딱 2번 훑으면 되는게 아닌지 고민해보자.
'''
