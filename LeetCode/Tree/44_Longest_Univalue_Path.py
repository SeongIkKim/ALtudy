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
