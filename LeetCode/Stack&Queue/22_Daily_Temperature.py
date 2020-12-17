from typing import List

# 1st try

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        ans = [0] * len(T)

        stack = []
        for i, tmp in enumerate(T[:-1]):
            stack.append((i, tmp))
            while stack and stack[-1][1] < T[i + 1]:
                date = stack.pop()[0]
                ans[date] = (i + 1) - date

        return ans

'''
512ms(52.23%)
19.7MB(9.11%)
'''
