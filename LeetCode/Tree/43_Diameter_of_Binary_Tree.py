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



