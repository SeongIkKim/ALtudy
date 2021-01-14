class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 1st try

class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        if not root:
            return 0

        lengths = [1]

        def dfs(node):
            if node is None:
                return False
            count = 0
            left = right = False
            if node.left and node.left.val == node.val:
                count += 1
                left = dfs(node.left)
            if node.right and node.right.val == node.val:
                count += 1
                right = dfs(node.right)
            if (left, right) == (False, False):
                lengths[-1] += count
                lengths.append(1)

        dfs(root)

        print(lengths)

        return max(lengths)

'''
너무 간단하게 생각했나?
'''

# solution

class Solution:
    result = 0

    def longestUnivaluePath(self, root: TreeNode) -> int:

        def dfs(node):
            if node is None:
                return 0

            # 존재하지 않는 노드까지 DFS 재귀 탐색
            # 즉, 일단 리프노드까지 내려간 뒤 백트래킹으로 올라오기
            left = dfs(node.left)
            right = dfs(node.right)

            # 현재 노드가 자식 노드와 동일한 경우 거리 1 증가
            if node.left and node.left.val == node.val:
                left += 1
            else:
                left = 0
            if node.right and node.right.val == node.val:
                right += 1
            else:
                right = 0

            # result는 현재까지 가장 긴 "노드의 중복경로길이"를 담아두는 변수
            self.result = max(self.result, left + right)

            # 서로 다른 두 노드간의 경로이므로, left와 right 둘 중 하나의 경로를 택해야한다.
            # 현재 노드가 left와 right가 갈리면, 그 아래의 경로가 나뉘었을 경우 한방향밖에 택할 수 없기 때문.
            # 둘 중 더 길이가 긴 경로쪽을 택해야한다
            return max(left, right)

        dfs(root)
        return self.result

'''
396ms(58.48%)
18.2MB(24.87%)
어렵다. 재귀도 어려운데 백트래킹을 중첩하는 구조는 더욱 어렵다. 마지막 파트는 이해가 안된다.
1. 백트래킹을 위해서, 일단 dfs로 리프노드까지 내려가야한다.
2. 내려가는 방향은 두가지, left와 right. 백트래킹에서 차례대로 값을 쌓아올려 리턴해줘야한다.
3. 현재 노드 기준으로 이전보다 더 긴 중복길이인지를 판단하고, 갱신해줘야한다. 이 때 변수는 클래스변수여야 로컬변수로 갱신되지 않는다.
4. 결국 현재 노드가 두 노드 사이의 경로 노드 중 하나라면, 좌 우 방향을 모두 선택할 수 없다. 더 큰쪽을 선택해야 한다. 이게 제일 어렵다.
'''
