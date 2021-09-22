from typing import Optional
from typing import Tuple


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 1st try
class Solution:
    def swap_trees(
            self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> Tuple[Optional[TreeNode], Optional[TreeNode]]:
        return root2, root1

    def traverse(self, root: Optional[TreeNode]):
        # 어떻게 return하는지가 감이 안온다
        pass

    def merge_trees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # 1. 두 빈 트리를 받을 경우
        if not root1 and not root2:
            return TreeNode()

        # 2. 한 트리와 한 빈 트리를 받을 경우
        if not all([root1, root2]):
            # 빈 트리를 무조건 root2로 옮기기.
            if not root1:
                root1, root2 = self.swap_trees(root1, root2)
            return root1

        # 3. 두 비지 않은 트리를 받았을 경우
        merged_tree = ret = TreeNode(root1.val + root2.val)
        pass

        return ret

"""
오랜만에 잡은 알고리즘, 트리, 재귀구조가 잘 기억이 나지 않는다...
"""

# 1st solution
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 and root2:
            node = TreeNode(root1.val + root2.val)
            node.left = self.mergeTrees(root1.left, root2.left)
            node.right = self.mergeTrees(root1.right, root2.right)
            return node
        else:
            return root1 or root2

"""
88ms(62.23%)
15.5MB(26.33%)
재귀구조를 사용한 간단한 풀이
1. 이진트리에서 재귀구조는 오직 부모, 왼쪽 자식, 오른쪽 자식만 정의하면 된다.
2. 각 자식 노드에 대해서는 부모노드처럼 수행할 수 있게 재귀호출을 한다.
3. 끝쪽부터 어떻게 return할 지 고민하지 말자. 재귀를 사용했을때 최후에 최초의 노드, 즉 최초의 부모노드가 반환되도록 짜면 된다.
4. return a or b는 a와 b 중 none이 아니거나 더 큰값을 반환한다.
"""
