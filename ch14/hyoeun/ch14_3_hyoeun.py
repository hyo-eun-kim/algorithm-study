'''
https://leetcode.com/problems/longest-univalue-path/

longest univalue path
    5
   / \
  4   5
 / \   \
4   4   5
         \
         5

답은 4
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, index=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.index = index

# 어디가 틀렸는지 모르겠다 ....
# -> else: left = 0 과 else: right = 0 추가해주니 해결되었다!
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        def dfs(node: TreeNode):
            if not node: return 0

            nonlocal longest_path
            left = dfs(node.left)
            right = dfs(node.right)

            if node.left and node.val == node.left.val:
                left += 1
            # else:
            #     left = 0
            if node.right and node.val == node.right.val:
                right += 1
            # else:
            #     right = 0

            longest_path = max(longest_path, left+right)
            return max(left, right)

        longest_path = 0
        dfs(root)
        return longest_path


# 다른 풀이
# 여기서 변수 2개를 둔 이유를 모르겠다!
class Solution2:
    def longestUnivaluePath(self, root):
        def dfs(root):
            """Return longest overall and longest ending at root."""
            if not root:
                return 0, 0
            l1, l2 = dfs(root.left)
            r1, r2 = dfs(root.right)        
            l2 = 1 + l2 if root.left and root.left.val == root.val else 0
            r2 = 1 + r2 if root.right and root.right.val == root.val else 0
            return max(l1, r1, l2 + r2), max(l2, r2)
        return dfs(root)[0]


if __name__ == "__main__":
    solution = Solution()

    # root = TreeNode(5)
    # root.left = TreeNode(4)
    # root.right = TreeNode(5)
    # root.left.left = TreeNode(1)
    # root.left.right = TreeNode(1)
    # root.right.right = TreeNode(5)

    # root = TreeNode(1)
    # root.left = TreeNode(4)
    # root.right = TreeNode(5)
    # root.left.left = TreeNode(4)
    # root.left.right = TreeNode(4)
    # root.right.right = TreeNode(5)

    # root = TreeNode(1)
    # root.right = TreeNode(1)
    # root.right.right = TreeNode(1)
    # root.right.right.right = TreeNode(1)

    root = None

    print(solution.longestUnivaluePath(root))

