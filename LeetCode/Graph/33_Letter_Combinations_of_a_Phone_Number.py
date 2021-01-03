from typing import List

# 1st try

class Solution:
    numbers = {2: ['a', 'b', 'c'], 3: ['d', 'e', 'f'], 4: ['g', 'h', 'i'], 5: ['j', 'k', 'l'], 6: ['m', 'n', 'o'],
               7: ['p', 'q', 'r', 's'], 8: ['t', 'u', 'v'], 9: ['w', 'x', 'y', 'z']}

    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return

        def recursive_dfs(s, p, digits, combi):
            if len(s) == len(digits):
                return combi.append(s)
            for letter in self.numbers[int(digits[p])]:
                recursive_dfs(''.join([s, letter]), p + 1, digits, combi)

        combi = []
        recursive_dfs('', 0, digits, combi)

        return combi

'''
32ms(56.17%)
14.3MB(50.90%)
클래스 변를 손코딩해서 이렇게 해도 되나 싶지만..
'''

# Solution

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        def dfs(index, path):
            # 끝까지 탐색하여 백트래킹
            if len(path) == len(digits):
                result.append(path)  # 어차피 중첩함수이므로 result를 넘겨줄 필요가 없다
                return

            # 입력값 자릿수 단위 반복
            for i in range(index, len(digits)):
                # 숫자에 해당하는 모든 문자열 반복
                for j in dic[digits[i]]:
                    dfs(i + 1, path + j)

        # 예외처리
        if not digits:
            return []

        dic = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'],
               '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
        result = []
        dfs(0, "")

        return result

'''
32ms(56.17%)수
14.1MB(75.40%)

중첩함수라 result(combi), digits를 넘겨주지 않았음.
이외에는 거의 동일
'''
