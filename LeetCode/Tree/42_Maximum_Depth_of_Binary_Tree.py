import collections


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

# 2nd try (bfs)

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0

        Q = collections.deque([root])

        depth = 0
        while Q:
            depth += 1
            for _ in range(len(Q)):
                node = Q.popleft()
                if node.left is not None:
                    Q.append(node.left)
                if node.right is not None:
                    Q.append(node.right)

        return depth

'''
40ms(73.34%)
15.4MB(91.39%)
solution(bfs)과 완전히 똑같음.
'''
