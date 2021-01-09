import collections

# 1st try

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True

        discovered = set()
        routes = collections.defaultdict(list)
        for pr in prerequisites:
            for i in range(len(pr) - 1):
                routes[pr[i]].append(pr[i + 1])

        def dfs(fr):
            print(discovered)
            if fr in discovered:
                return False
            discovered.add(fr)
            for destination in routes[fr]:
                result = dfs(destination)
                if result == False:
                    return False
            return True

        return dfs(prerequisites[0][0])

'''
코드가 자꾸 꼬인다. 티켓문제와 같은거같은데 뭐가 잘못된거지.
'''

# solution - dfs

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)

        for x, y in prerequisites:
            graph[x].append(y)

        # 순환구조 판별하기위해, 방문했던 노드를 traced에 저장한다.
        traced = set()

        def dfs(i):
            # 이미 방문한 노드이면 순환구조이므로 False 반환
            if i in traced:
                return False

            traced.add(i)
            # graph에 있는 각 경로에 대해서 계속 수행한다.
            # 하나라도 순환구조가 있어 False를 반환하면, 계속 False를 반환하여 빠져나오는 구조가 된다.
            for y in graph[i]:
                if not dfs(y):
                    return False
            # 탐색 종료 후 순환노드 삭제
            # 방문한 노드를 삭제하지 않고 그냥 둔다면 방문했던 노드들이 그대로 남게되어, 순환을 잘못 판단할 수 있다.
            # 대표적인 예 [[0,1],[0,2],[1,2]]
            # 0->1->2를 거치고 나면 traced에 {0,1,2}가 남는데, 이경우 1->2는 순환이 아님에도 불구하고 이미 방문했던 노드로 판단되어 순환판단을 내린다.
            # 따라서, dfs를 호출할 때마다(각 숫자를 건너갈 때마다) for 탐색을 수행하고 난 뒤, 자기 턴이 끝날 때 i를 삭제해주어야한다.
            traced.remove(i)

            return True

        # graph 내의 모든 key값에 대해 수행한다.
        # 이렇게 하지 않고 dfs를 한번만 호출하면, 연결고리가 없이 떨어진 graph들을 탐색하지 않는다.
        # defaultdict 클래스의 key를 호출하는 방법 : list(DICT)
        for x in list(graph):
            if not dfs(x):
                return False

        return True

'''
840ms(7.65%)
17.5MB(19.55%)
순환 노드를 remove할 생각을 못했다. 그냥 파라미터로 넘길 생각만 했지...
거의 가깝게 해결했는데 아쉽다.
'''

# solution - dfs 최적화(가지치기)

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)

        for x, y in prerequisites:
            graph[x].append(y)

        traced = set()
        # visit한 graph를 담아두어 다시 탐색하지 않도록(가지치기) 하기 위한 변수
        visited = set()

        def dfs(i):
            # 순환구조이면 False
            if i in traced:
                return False
            # 이미 방문한 그래프일경우 즉시 True를 리턴하여 넘긴다
            if i in visited:
                return True

            traced.add(i)
            for y in graph[i]:
                if not dfs(y):
                    return False

            # 탐색 종료 후 순환 노드 삭제
            traced.remove(i)
            # 탐색 종료 후 방문 노드 추가
            visited.add(i)

            return True

        # 순환 구조 판별
        for x in list(graph):
            if not dfs(x):
                return False

        return True

'''
124ms(27.81%)
17.9MB(9.58%)
visited를 이용하여 이미 탐색을 끝낸 graph를 다시 탐색하는 불필요함을 줄였다.
타임이 크게 줄었다.
'''
