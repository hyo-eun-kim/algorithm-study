"""
## 14-11. 이진 탐색 트리 합의 범위

BST가 주어졌을 떄 L이상 R 잏의 값을 지닌 노드의 합을 구하라.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        # 220 ms
        def dfs(root):
            if not root:
                return 0

            if root.val < low:
                return dfs(root.right)
            if root.val > high:
                return dfs(root.left)
            return root.val + dfs(root.left) + dfs(root.right)

        return dfs(root)


if __name__ == '__main__':
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(7)
    root.right.left = TreeNode(None)
    root.right.right = TreeNode(18)

    sol = Solution()
    print(sol.rangeSumBST(root, 7, 15))