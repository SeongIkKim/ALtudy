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
