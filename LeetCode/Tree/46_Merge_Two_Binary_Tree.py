from typing import Optional
from typing import Tuple


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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
