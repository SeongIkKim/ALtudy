from collections import deque

# 1st try

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        candidates = deque()
        for i, num in enumerate(nums):
            if i < 3:
                candidates.append(num)
                continue
            if sum(candidates) < target:
                candidates.popleft()
                candidates.append(num)
        distance = abs(target - sum(candidates))  # +/- 바뀌는 지점 기준으로 잡은 최초 후보
        print(candidates)
        for left in range(i - 2, -1, -1):
            candidates[0] = nums[left]
            print(f"candidates : {candidates}")
            leftshift_distance = abs(target - sum(candidates))
            if leftshift_distance <= distance:
                print(f"distance {distance} | leftshift {leftshift_distance}")
                distance = leftshift_distance
            else:
                candidates[0] = nums[left+1]
                break
        for right in range(i + 2, len(nums)):
            candidates[-1] = nums[right]
            print(f"candidates : {candidates}")
            rightshift_distance = abs(target - sum(candidates))
            if rightshift_distance <= distance:
                print(f"distance {distance} | rightshift {rightshift_distance}")
                distance = rightshift_distance
            else:
                candidates[-1] = nums[right-1]
                break
        return sum(candidates)


"""
반례
nums : [1,1,-1,-1,3]
target : -1
"""

# Solution 1

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = sum(nums[:2])  # 최초 3개로 초기화
        # i, j, k : left, mid, right
        for i in range(len(nums) - 2):
            j, k = i + 1, len(nums) - 1  # right는 end부터 왼쪽으로
            while j < k:  # mid와 right 탐색
                sum = nums[i] + nums[j] + nums[k]  # 탐색 중의 new sum(result 후보)
                # 1. target과 일치하면 더 낮게 나올수가 없으므로 그냥 반환
                if sum == target:
                    return sum
                # 2. 기존의 result보다 더 낮은 sum이 나오면 갱신
                if abs(sum - target) < abs(result - target):
                    result = sum
                # 방향성 설정
                # 1. target보다 작을경우 mid를 rightshift
                if sum < target:
                    j += 1
                # 2. target보다 클경우 right를 leftshift
                elif sum > target:
                    k -= 1

        return result

"""
136ms(53.38%)
14.3MB(40.90%)
1. mid부터 정해놓는게 아니라, O(n^2)임을 명확히 파악하고 left 내부에서 right와 mid를 투포인터 사용
2. 포인터 방향성 설정과 갱신과정 분리
"""
