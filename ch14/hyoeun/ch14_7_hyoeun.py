'''
48. 균형 이진 트리
이진트리가 높이 균형(height-balanced)인지 판단하라.
높이 균형은 모든 노드의 서브트리 간의 높이 차이가 1이하인 것을 말한다.
https://leetcode.com/problems/balanced-binary-tree/
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def recursive(node):
            if node is None:
                return -1
            left = 1 + recursive(node.left)
            right = 1 + recursive(node.right)

            if abs(left - right) > 1:
                nonlocal ret
                ret = False
            return max(left, right)  # <- 중요!

        ret = True
        recursive(root)
        return ret
