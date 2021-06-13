from typing import List

# 1st try

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        mid = root = len(nums) // 2
        print(mid, root)
        while mid == target:
            print(f"mid[{mid}] : {nums[mid]}")
            if nums[mid] == target:
                print('mid == target')
                return mid
            if mid != 0 and nums[mid] > target:
                print('mid > target')
                mid = mid // 2
            elif nums[mid] < target:
                print('mid < target')
                mid = (mid + len(nums)) // 2
            elif mid == root:
                if nums[mid] != target:
                    print('mid == 0')
                    root = (root + len(nums)) // 2
                    print("root update ", root)
                    mid = root
                else:
                    return 0

"""
O(log n)이니 당연히 binary search긴 할테지만...
"""

# Solution 1

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 예외처리
        if not nums:
            return -1

        low, high = 0, len(nums) - 1  # mid로 정하는게 아니라 log, high로 직접 탐색범위 지정

        while low <= high:
            mid = (low + high) >> 1  # bitshift로 1칸 밀어서 몫만 취하고 나머지는 버림(//2와 같음)

            # 정답을 찾았을 경우
            if target == nums[mid]:
                return mid

            # 이진 탐색
            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        # 못찾았을 경우 예외처리
        return -1

"""
40ms(75.06%)
14.8MB(20.45%)
그냥 일반적인 이진 탐색.
너무 쫄았나?
"""

