'''
https://leetcode.com/problems/diameter-of-binary-tree/
이진트리에서 두 노드간 가장 긴 경로의 길이를 출력하라.
          1
         / \
        2   3
       / \
      4   5
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 참고한 코드
# https://leetcode.com/problems/diameter-of-binary-tree/discuss/480877/543.-Diameter-of-Binary-Tree-and-124.-Binary-Tree-Maximum-Path-Sum
# 44ms (faster than 69%)
# 16.2MB (less than 73%)
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def height(root):
            nonlocal diameter
            if not root:
                return 0
            left = height(root.left)
            right = height(root.right)

            #     1
            #       2
            #     3   4
            #    5      6
            diameter = max(diameter, left+right)

            # max(left sub tree의 depth, right sub tree의 depth) + 1 (자식과 부모의 거리)
            return max(left, right)+1

        diameter = 0
        height(root)
        return diameter

if __name__ == "__main__":
