"""
## 14-1. 이진 트리의 최대 깊이

이진 트리의 최대 깊이를 구하라.
"""
from typing import *
import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # 44ms
        if root is None:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def maxDepth2(self, root: TreeNode) -> int:
        # 36ms
        if root is None:
            return 0

        queue, depth = collections.deque(), 0
        if root:
            queue.append(root)

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth += 1
        return depth


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.left.left = TreeNode(None)
    root.left.right = TreeNode(None)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    sol = Solution()
    print(sol.maxDepth(root))
    print(sol.maxDepth2(root))