"""
## 14-2. 이진 트리의 직경

이진 트리에서 두 노드 간 가장 긴 경로의 길이를 출력하라.
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
        self.diameter = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        # 48ms
        def dfs(node):
            if node is None:
                return 0
            left = dfs(node.left) # 왼쪽 서브 트리 탐색
            right = dfs(node.right) # 오른쪽 서브 트리 탐색
            self.diameter = max(self.diameter, left + right)
            return max(left, right) + 1

        dfs(root)
        return self.diameter


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    sol = Solution()
    print(sol.diameterOfBinaryTree(root))