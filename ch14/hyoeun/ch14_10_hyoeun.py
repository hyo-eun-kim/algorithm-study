'''
51. 이진 탐색 트리(BST)를 더 큰 수 합계 트리로
BST의 각 노드를 현재값보다 더 큰 값을 가진 노드의 합으로 만들어라.
https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    cum_sum = 0
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if root:
            # in-order traversal
            self.bstToGst(root.right)
            self.cum_sum += root.val
            # print(root.val, ":", self.cum_sum)
            root.val = self.cum_sum
            self.bstToGst(root.left)
        return root