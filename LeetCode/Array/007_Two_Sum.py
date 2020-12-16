from typing import List

# 1st try

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted(nums)

        left = 0
        right = len(nums) - 1
        done = False

        while not done and left < right:
            sum = sorted_nums[left] + sorted_nums[right]
            if sum > target:
                right -= 1
            elif sum < target:
                left += 1
                right = len(nums) - 1
            else:  # sum == target
                done = True

        first_num_index = nums.index(sorted_nums[left])
        nums[first_num_index] = None # index가 흐트러지지 않게 하려고
        second_num_index = nums.index(sorted_nums[right])

        return [first_num_index, second_num_index]

'''
1108ms(23.24%)
27.6MB(13.32%)
투 포인터 방식으로, 이 경우 아래의 solution보다 가독성이 더 좋지만, sorted 때문에 속도도 느리고 공간복잡도도 높다.
index를 찾아내는 방식에서는 sort를 할 시 index가 파괴되므로 사용을 지양한다.
'''

# 1st solution

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        nums_map = dict()

        # 키 값을 바꿔서 딕셔너리 저장(num으로 index 조회하기 위하여)
        for i, num in enumerate(nums):
            if target - num in nums_map:
                return [i, nums_map[target - num]]
            nums_map[num] = i


'''
440ms(41.54%)
28MB(10.55%)
1. 키값쌍을 바꾼 딕셔너리로 인덱스 조회
'''
