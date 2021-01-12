class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 1st Try

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        m = set()

        def down(node, depth):
            if node.left is None and node.right is None:
                m.add(depth)
                return
            if node.left:
                down(node.left, depth + 1)
            if node.right:
                down(node.right, depth + 1)

        down(root, 1)

        return max(m)

'''
44ms(43.17%)
16.3MB(18.38%)
m에 결국 depth의 뭉터기가 들어가므로 그닥 효율적이지 않다.
원래는 max함수로 외부의 변수를 바꿔치기 하려고 했는데, nested임에도 선언이 안되었다고 나온다..
'''
