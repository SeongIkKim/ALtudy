from typing import List

# 1st try

class Solution:

    def trap(self, height: List[int]) -> int:

        elevation_map = {0: 0}

        top = 0
        # s = []
        box = 0

        for i, level in enumerate(height):
            # level이 top보다 높음 : 가장 높은 level
            if level > top:
                print('커짐')
                for new_level in range(1, level):
                    elevation_map[new_level] = i
                top = level
            # level이 top과 같음
            elif level == top:
                print('같음')
                box += level * (i - (elevation_map[level] + 1))
            # level이 top보다 낮음 : 내려가있는 중
            else:
                print('작아짐')
                if elevation_map[level]:
                    box += level * (i - (elevation_map[level] + 1))

                elevation_map[level] = i

        return box

'''
2시간, 실패
1. 풀이 방법은 여러가지가 생각나는데 이걸 코드로 못옮기겠음
'''


# 1st solution

class Solution:
    def trap(self, height: List[int]) -> int:

        if not height:
            return 0

        volume = 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]

        while left < right:
            # max함수로 간편하게 크기 비교
            left_max, right_max = max(left_max, height[left]), max(right_max, height[right])

            # 더 높은쪽을 향해 포인터 이동
            # 단순히 한칸씩 옮기는게 아니라, 현 상황에서 어느쪽이 더 높은지 보고 그에 맞추어 이동한다.
            if left_max <= right_max:
                volume += left_max - height[left]
                left += 1
            else:
                volume += right_max - height[right]
                right -= 1

        return volume

'''
52ms(66.77%)
14.7MB(64.36%)
1. 투포인터 방식으로 O(n)
2. 웅덩이의 volume은 각 이동마다 세로길이 측정(정적분처럼)
'''

# 2nd solution

class Solution:
    def trap(self, height: List[int]) -> int:

        stack = []
        volume = 0

        for i in range(len(height)):
            # 현재 높이가 이전보다 높은 변곡점
            # 1. stack이 있고(즉, 첫칸이 아니고)
            # 2. 직전높이보다 높은지 검사한다
            while stack and height[i] > height[stack[-1]]:
                # 바로 전 칸의 높이값(top)을 꺼낸다
                top = stack.pop()

                # top을 한개 뽑으니 stack이 없다
                # == 이전 칸이 없다
                # == 웅덩이를 완성할 왼쭉 기둥이 없다
                if not len(stack):
                    break

                # 이전과의 차이만큼 물높이 처리
                # 가로가 길다란 직사각형 단위로 구한다

                distance = i - stack[-1] - 1  # 가로길이

                # 왼쪽 오른쪽 기둥중 낮은 기둥에 맞추어서
                # 전칸의 높이값(height[top]) 부터 쌓인 가장 위쪽 물 블록의 높이를 구한다
                water_height = min(height[i], height[stack[-1]]) - height[top]  # 세로길이

                volume += distance * water_height

            # 각 height마다 stack에 들어간다
            stack.append(i)

        return volume

'''
52ms(66.77%)
14.7MB(64.36%)
1. stack 방식으로 O(n)
2. 직관적이지는 않은 풀이
3. 투포인터와 반대로 가로로 나눈 길이를 구한다
'''

