# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        """
        leetcode 52
        범위에 맞는 것들만 더해주자
        """
        # 스택 dfs
        stack, res = [root], 0
        while stack:
            node = stack.pop()
            if node:
                if node.val > low: # low와 high 사이에 있으면 두 가지 모두가 스택에 푸시
                    stack.append(node.left)
                if node.val < high:
                    stack.append(node.right)
                if low <= node.val <= high:
                    res += node.val

        return res
