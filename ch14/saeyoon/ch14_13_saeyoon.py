"""
## 14-13. 전위, 중위 순회 결과로 이진 트리 구축

트리의 전위, 중위 순회 결과를 입력값으로 받아 이진 트리를 구축하라.
"""
from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # 132ms
        if not inorder:
            return None

        # preorder의 첫 값은 루트 노드의 값
        index = inorder.index(preorder.pop(0))

        root = TreeNode(inorder[index])
        root.left = self.buildTree(preorder, inorder[0:index])
        root.right = self.buildTree(preorder, inorder[index+1:])

        return root

