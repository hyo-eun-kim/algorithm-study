"""
## 14-3. 가장 긴 동일 값의 경로

동일한 값을 지닌 가장 긴 경로를 찾아라.
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
        self.answer = 0

    def longestUnivaluePath(self, root: TreeNode) -> int:
        # 380ms
        def dfs(node):
            if node is None:
                return 0
            left = dfs(node.left) # 왼쪽 서브 트리 탐색
            right = dfs(node.right) # 오른쪽 서브 트리 탐색

            left = left + 1 if node.left and node.val == node.left.val else 0
            right = right + 1 if node.right and node.val == node.right.val else 0

            self.answer = max(self.answer, left + right)
            print(node.val, left, right)
            return max(left, right)

        dfs(root)
        return self.answer


if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(1)
    root.right.left = TreeNode(5)

    sol = Solution()
    print(sol.longestUnivaluePath(root))