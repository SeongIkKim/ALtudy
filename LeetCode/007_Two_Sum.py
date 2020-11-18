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
'''
