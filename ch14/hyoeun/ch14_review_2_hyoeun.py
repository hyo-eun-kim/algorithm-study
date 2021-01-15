'''
Leetcode 103. Binary Tree Zigzag level order traversal
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
'''

import collections
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# faster than 89% (28ms)
# less than 69% (14.5MB)
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        deq = collections.deque([root])
        result = [[root.val]]
        level = 0
        while deq:
            new_deq = []
            while deq:
                node = deq.pop()
                if node:
                    if level % 2:
                        new_deq.extend([node.left, node.right])
                    else:
                        new_deq.extend([node.right, node.left])

            level += 1
            deq = collections.deque(new_deq)
            new_result = [node.val for node in new_deq if node]
            if new_result: result.append(new_result)
        return result
