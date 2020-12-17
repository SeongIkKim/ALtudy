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
이전에 프로그래머스에서 풀어봤던 문제라서 쉽게 풀 수 있었다.
그땐 2시간 걸렸는데..
'''

# 1st solution - 스택

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        answer = [0] * len(T)
        stack = []
        for i, cur in enumerate(T):
            while stack and cur > T[stack[-1]]:
                last = stack.pop()
                answer[last] = i - last
            stack.append(i)  # stack에는 인덱스만 담는다

        return answer

'''
504ms(65.00%)
18.9MB(25.05%)
내 풀이와 방식은 같지만, stack에 enumerate를 담는 대신 인덱스만 담았다.
덕분에 메모리를 줄일 수 있었다. 런타임도 조금 줄어들었다.
'''


