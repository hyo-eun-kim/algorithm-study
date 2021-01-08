# 이진 트리 반전

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return
            
        root.left, root.right = self.invertTree(root.left), self.invertTree(root.right)

        return root