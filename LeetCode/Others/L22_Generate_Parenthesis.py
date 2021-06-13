from typing import List

# Solution 1

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # left와 right는 남은(추가할 수 있는) 왼쪽괄호/오른쪽괄호의 수.
        # https://docs.python-guide.org/writing/gotchas/#mutable-default-arguments
        # default arguments는 함수 define 타임에 단 한번 설정되고, 덕분에 recursive 함수라도 매번 재할당할 필요없이 같은 parens에 add up 된다.
        def generate(p, left, right, parens=[]):
            # left부터 쓰기 시작(재귀)
            if left:
                generate(p + '(', left - 1, right)
                # left를 썼다면 right를 써서 짝맞추기(재귀)
            if right > left:
                generate(p + ')', left, right - 1)
            # 단순히 오른쪽 괄호가 없는것이 아니라, left와 right를 모두 썼음을 의미
            # 즉, 6개를 다 쓰면 parens에 괄호쌍 추가
            if not right:
                parens.append(p)
            return parens
        return generate('', n, n)


"""
28ms(95.55%)
14.3MB(99.50%)
어나더레벨 파이썬..
1. 백트래킹 알고리즘
2. default argument의 신박한 사용. 저걸 사용하면 recursive에서도 계속 동일한 리스트를 사용할 수 있겠구나.
"""


# Solution 2

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if not n:
            return []
        left, right, ans = n, n, []
        self.dfs(left, right, ans, "")
        return ans

    def dfs(self, left, right, ans, string):
        # 왼쪽보다 오른쪽을 먼저 쓴 경우는 return(제거)
        # 모든 짝이 맞는 괄호쌍은, 왼쪽 괄호가 먼저 나와야하기 때문에 right가 left보다 작을수가 없다(left가 무조건 더 작다)
        if right < left:
            return
        # 탈출조건 : answer 찍기
        if not left and not right:
            ans.append(string)
            return
        # 왼쪽 괄호가 남아있으면 계속 사용(dfs)
        if left:
            self.dfs(left - 1, right, ans, string + "(")
        # 오른쪽 괄호가 남아있으면 계속 사용(dfs)
        if right:
            self.dfs(left, right - 1, ans, string + ")")

"""
32ms(84.98%)
14.3MB(96.05%)
좀 더 이해하기 쉬운 DFS 방식.
1. recursive간에 짝이 맞는 괄호집합을 담아둘 ans는 최초에 함수로 전달하여 append함으로써 call by objective-reference
2. 모든 올바른 괄호쌍에서, 오른쪽 괄호는 왼쪽괄호보다 먼저 사용될 수 없다.
3. 괄호의 개수나 종류를 숫자로 치환하는 습관을 들이자.
"""


if __name__=='__main__':
    S = Solution()
    print(S.generateParenthesis(3))
