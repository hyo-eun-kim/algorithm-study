'''
43. 이진 트리의 직경

이진 트리에서 두 노드 간 가장 긴 경로의 길이를 출력하라.

이진 트리가 주어졌을 때 ，
      1
     / \
    2   3
   / \
  4   5
가장 긴 경로는 4->2->1->3 또는 5 ->2->1->3으로 3 이다.

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 이해가 잘 되지 않는 문제
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 0
        def depth(node):
            if not node: 
                return -1
            L = depth(node.left)
            R = depth(node.right)
            
            self.ans = max(self.ans, L+R+2)
            
            return max(L, R) + 1

        depth(root)
        return self.ans
    # 56 ms
    