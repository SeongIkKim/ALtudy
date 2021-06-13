from typing import List

# 1st try
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        answer = []
        for a in range(len(nums)-3):
            for b in range(a+1,len(nums)-2):
                for c in range(b+1, len(nums)-1):
                    s = set(nums[c+1:len(nums)])
                    if target-(nums[a] + nums[b] + nums[c]) in s :
                        if [nums[a], nums[b], nums[c], target-(nums[a] + nums[b] + nums[c])] not in answer:
                            answer.append([nums[a], nums[b], nums[c], target-(nums[a] + nums[b] + nums[c])])
        return answer

"""
5880 ms(5.08%)
14.3MB(77.01%)
통과한게 엽기
"""

# Solution 1

class Solution:
    def threeSums(self, nums, target):
        nums.sort()
        result = []
        for i in range(len(nums) - 2):
            j, k = i + 1, len(nums) - 1
            t = target - nums[i]
            if i == 0 or nums[i] != nums[i - 1]:  # 중복되는 경우 제거
                while j < k:
                    s = nums[j] + nums[k]
                    if s < t:
                        j += 1
                    elif s > t:
                        k -= 1
                    else:
                        result.append([nums[i], nums[j], nums[k]])
                        while j < k and nums[j] == nums[j + 1]:
                            j += 1
                        while j < k and nums[k] == nums[k - 1]:
                            k -= 1
                        j += 1
                        k -= 1
        return result

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums) - 3):
            if i == 0 or nums[i] != nums[i - 1]:
                result.extend([[nums[i]] + l for l in self.threeSums(nums[i + 1:], target - nums[i])])

        return result

"""
724ms(63.10%)
14.4MB(53.31%)
1. 3sum 기밤으로 4sum 만들기
2. 투포인터가 사용되는 전형적인 예(투포인터는 O(n^2)을 O(n)으로 낮춰줄 수 있음)
"""
