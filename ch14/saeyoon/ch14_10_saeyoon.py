"""
## 14-10. 이진 탐색 트리를 더 큰 수 합계 트리로

BST의 각 노드를 현재값보다 더 큰 값을 가진 모든 노드의 합으로 만들어라.
"""
from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.val = 0

    def bstToGst(self, root: TreeNode) -> TreeNode:
        if root:
            self.bstToGst(root.right)
            self.val += root.val
            root.val = self.val
            self.bstToGst(root.left)

        return root


if __name__ == '__main__':
    root = TreeNode(4)
    root.left = TreeNode(1)
    root.right = TreeNode(6)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(7)
    root.left.right.right = TreeNode(3)
    root.right.right.right = TreeNode(8)

    sol = Solution()
    print(sol.bstToGst(root))