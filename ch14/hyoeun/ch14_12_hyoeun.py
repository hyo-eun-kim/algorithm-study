# 두 노드간 값의 차이가 가장 작은 노드의 값의 차이를 출력하라 .
# https://leetcode.com/problems/minimum-distance-between-bst-nodes/

import sys

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.prev = -sys.maxsize
        self.result = sys.maxsize
        
    def minDiffInBST(self, root: TreeNode) -> int:
        print(root.val)
        if root.left:
            self.minDiffInBST(root.left)
        
        self.result = min(self.result, root.val-self.prev)
        self.prev = root.val
        
        if root.right:
            self.minDiffInBST(root.right)
        return self.result