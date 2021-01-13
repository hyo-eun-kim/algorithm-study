"""
## 14-7. 균형 이진 트리

이진 트리가 높이 균형인지 판단하라.
- 높이 균형은 모든 노드의 서브 트리 간의 높이 차이가 1 이하인 것을 말한다.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 48ms
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


    def isBalanced(self, root: TreeNode) -> bool:
        if root is None:
            return True

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return abs(left - right) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.left.left = TreeNode(None)
    root.left.right = TreeNode(None)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    sol = Solution()
    print(sol.isBalanced(root))