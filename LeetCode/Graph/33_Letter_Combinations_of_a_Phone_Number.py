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
클래스 변수를 손코딩해서 이렇게 해도 되나 싶지만..
'''
