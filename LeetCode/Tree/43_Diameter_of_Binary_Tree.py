# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 1st try
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root or (not root.left and not root.right):
            return 0

        D = dict()
        dep = set()

        def dfs(node, depth):
            if node.left and node.right:
                left_depth = dfs(node.left, depth + 1)
                right_depth = dfs(node.right, depth + 1)
                D[node.val] = [left_depth - depth, right_depth - depth]
                return max(left_depth, right_depth)
            elif node.left:
                return dfs(node.left, depth + 1)
            elif node.right:
                return dfs(node.right, depth + 1)
            else:
                dep.add(depth)
                return depth

        dfs(root, 0)
        if D:
            max_length = max([sum(i) for i in D.values()])
        else:
            return max(dep)

'''
테스트 케이스를 하나씩 해결하며 누더기처럼 기워붙였는데
결국 해결이 안되었다.
105/106개를 해결했다.(까비)
'''

# solution - dfs

class Solution:
    longest = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                # 기본적으로 좌, 우가 있다는 가정하에 2를 더하는데, 한 노드가 없으면 2 중 1이 사라져야하므로 -1을 리턴해준다
                return -1
            # 왼쪽, 오른쪽의 각 리프노드까지 탐색
            left = dfs(node.left)
            right = dfs(node.right)

            # 가장 긴 경로
            # nested 함수에서 클래스변수를 사용하지 않고 그냥 부모 함수의 변수를 갱신하면, 로컬변수로 변경되어버린다
            self.longest = max(self.longest, left + right + 2)
            # 상태 값
            # 윗 노드로 올려보낼때 또 하나의 edge를 거치므로, +1
            return max(left, right) + 1

        dfs(root)
        return self.longest

'''
기본적인 구상은 크게 다르지 않은데, 코드에 많은 차이가 있다.
1. 중첩 함수에서 부모 함수의 변수에 append, add 등이 아닌 갱신을 할 경우, local variable이 되어버린다. 따라서 클래스변수를 사용할것.
2. 가장 아래까지 내려갔다가 백트래킹으로 하나씩 업데이트하는 방식
'''

