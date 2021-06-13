from typing import List

# Two Pointer

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        max_area = 0
        while left < right:
            max_area = max(max_area, (right-left) * min(height[left], height[right]))
            # 가로 길이를 좁히면서 넓이를 늘리기 위해서는 세로 길이가 길어져야한다.
            # 왼쪽/오른쪽 높이 중 낮은 쪽을 기준으로 max_area가 정해지므로, 낮은 쪽을 올리는 방향으로 이동한다.
            if height[left] < height[right]:
                left +=1
            else:
                right -= 1
        return max_area

if __name__ == '__main__':
    S = Solution()
    S.maxArea([1,8,6,2,5,4,8,3,7])
