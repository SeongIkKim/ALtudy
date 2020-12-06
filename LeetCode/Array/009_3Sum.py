from itertools import combinations
from typing import List

# 1st try

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = [tuple(sorted(list(triplet))) for triplet in list(combinations(nums, 3)) if sum(triplet) == 0]

        return list(set(triplets))

'''
시간초과
코드 골프 느낌으로 해봤는데 아무래도 combinations는 시간복잡도가 너무 큰것같다.
브루트 포스라서 시간복잡도가 O(n^3)
'''

# solution(improved)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = set()

        nums.sort()
        print(nums)
        l = len(nums)
        if l < 2:
            return triplets

        for i in range(l - 2):
            # 축(nums[i])이 중복인 경우 건너뛰기(이전의 연산과 차이가 없음)
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, l - 1
            while left < right:
                # print(nums[i], nums[left], nums[right])
                s = nums[i] + nums[left] + nums[right]
                if s > 0:
                    right -= 1
                elif s < 0:
                    left += 1
                else:
                    # print("append", nums[i],nums[left],nums[right])
                    triplets.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1

        return triplets

'''
872ms(57.22MB)
16.9MB(91.98%)
1. 세 개의 합이지만, 축 하나를 잡고 투포인터로 O(n^2)까지 끌어내릴수 있다.
2. 일반적으로 투포인터를 사용할때는 전체 배열을 sort하고 시작하는것이 좋다.(python sort의 시간복잡도는 O(nlogn)으로 대단히 빠르다)
3. 책에서는 while문을 한개 더 넣어 triplet 중복을 제거했지만, 나는 return 값이 정해져있지 않으므로 set을 사용. 이 방식이 조금 더 가독성이 좋고 시간이 미세하게 빠르다.
'''
