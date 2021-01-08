'''
https://leetcode.com/problems/maximum-depth-of-binary-tree/
Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# run time 40ms (faster than 72%)
# memory usage 16.3MB (less than 14%)
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def dfs(depth, node):
            nonlocal max_depth
            if max_depth < depth:
                max_depth = depth
            if node.left:
                dfs(depth+1, node.left)
            if node.right:
                dfs(depth+1, node.right)

        if not root:
            return 0
        max_depth = 0
        dfs(1, root)
        return max_depth


# 참고한 풀이
class Solution2:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        else:
            l_depth = self.maxDepth(root.left)
            r_depth = self.maxDepth(root.right)
            return max(l_depth, r_depth)+1


if __name__ == "__main__":
    solution = Solution2()

    node = TreeNode(3)
    node.left = TreeNode(9)
    node.right = TreeNode(20)
    node.right.left = TreeNode(15)
    node.right.right = TreeNode(7)
    print(solution.maxDepth(node))




