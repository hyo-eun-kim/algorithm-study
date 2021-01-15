'''
48. 균형 이진 트리

이진 트리가 높이 균형인지 판단하라.

높이균형: 모든 노드의 서브 트리 간의 높이 차이가 1 이하인 것

Example 1:
      3
     / \
    9  20
       / \
      15  7

Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2:
          1
         / \
        2   2
       / \
      3   3
     / \
    4   4

Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def check(root):
            if not root:
                return 0
            
            left = check(root.left)
            right = check(root.right)
            
            if left == -1 or right == -1 or abs(left-right) > 1:
                return -1
            
            return max(left, right) + 1
        return check(root) != -1
    
    # 48 ms
