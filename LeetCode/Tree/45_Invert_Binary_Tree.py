# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 1st try

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:

        def dfs(node):
            if not node:
                return None
            if node.left is None and node.right is None:
                return None
            if (node.left and node.right is None) or (node.left is None and node.right):
                node.left, node.right = node.right, node.left
                return None

            left = dfs(node.left)
            right = dfs(node.right)

            if left is None and right is None:
                node.left, node.right = node.right, node.left

        dfs(root)

        return root

'''
TestCase
Input : [2,3,null,1]
Output : [2,null,3,1]
Expected : [2,null,3,null,1]
원래 null이 없던 곳에서 null이 생겨야 한다는 사실을 간과했다.
'''
