from typing import List

# 1st try

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(i, j, discovered):
            stack = [(i, j)]
            while stack:
                i, j = stack.pop()
                if grid[i][j] not in discovered and grid[i][j] == 1:
                    discovered.append((i, j))
                    for ii in range(i - 1, i + 2):
                        for jj in range(j - 1, j + 2):
                            try:
                                if (ii, jj) not in discovered:
                                    stack.append((ii, jj))
                            except:
                                continue
            return discovered

        discovered = []
        count = 0
        while len(discovered) < len(grid) * len(grid[0]):
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 1 and grid[i][j] not in discovered:
                        discovered = dfs(i, j, discovered)
                        count += 1

        return count

# 2nd try

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(i, j, discovered):
            stack = [(i, j)]
            while stack:
                i, j = stack.pop()
                if grid[i][j] not in discovered and grid[i][j] == '1':
                    discovered.append((i, j))
                    for ii, jj in [(i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1)]:
                        try:
                            if grid[ii][jj] is not None and (ii, jj) not in discovered:
                                stack.append((ii, jj))
                        except:
                            continue
            return discovered

        discovered = []
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and (i, j) not in discovered:
                    discovered = dfs(i, j, discovered)
                    count += 1

        return count

'''
43/46
테스트케이스 중 3개를 통과 못했다.
얼기설기 엮은 코드긴 한데 어디가 문제인지 잘 모르겠다.
'''

# 3rd try

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(i, j):
            stack = [(i, j)]
            while stack:
                i, j = stack.pop()
                if grid[i][j] == '1':
                    grid[i][j] = 0
                    for a, b in [(ii, jj) for ii, jj in [(i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1)] if
                                 0 <= ii < len(grid) and 0 <= jj < len(grid[0])]:
                        try:
                            if grid[a][b] is '1':
                                stack.append((a, b))
                        except:
                            continue

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i, j)
                    count += 1

        return count

'''
152ms(33.55%)
15.3MB(58.50%)
discovered를 만들 필요 없이 그냥 0으로 만들면 된다(조언을 보고 멍해졌다)
리스트컴프리헨션문이 아주 괴랄한데, 갓python님의 -1,-2 등 음수 인덱스 지원때문이다(...)
세상에, try except걸어놓은 ii, jj가 (0,-1)이 될 지는 몰랐다. 
'''

# solution

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            # 더 이상 grid 영역이 아니거나, 땅('1')이 아닌 경우 종료
            if not (0 <= i < len(grid)) or not (0 <= j < len(grid[0])) or grid[i][j] != '1':
                return

            grid[i][j] = 0

            # 동서남북 탐색
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i, j)
                    # 하나의 섬 탐색이 끝났음
                    count += 1
        return count

'''
136ms(76.62%)
15.6MB(32.10%)
초반 예외처리가 깔끔하여 이후 코드가 모두 우아해진다.
재귀함수를 사용할 때 예외처리는 함수 머릿부분에 두려고 의식적으로 노력해보자.
'''
