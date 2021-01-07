"""
## 14-4. 이진 트리 반전

이진 트리를 좌우 반전 시켜라.
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
    def invertTree(self, root: TreeNode) -> TreeNode:
        # 56ms
        if root is None:
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
        """
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            return root
        """

    ## BFS
    def invertTree2(self, root: TreeNode) -> TreeNode:
        # 28ms
        queue = collections.deque([root])

        while queue:
            node = queue.popleft()
            if node:
                node.left, node.right = node.right, node.left

                queue.append(node.left)
                queue.append(node.right)

        return root

    ## DFS
    def invertTree3(self, root: TreeNode) -> TreeNode:
        # 28ms
        stack = collections.deque([root])

        while stack:
            node = stack.pop()
            if node:
                stack.append(node.left)
                stack.append(node.right)
                node.left, node.right = node.right, node.left

        return root


if __name__ == '__main__':
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)

    sol = Solution()
    print(sol.invertTree(root))