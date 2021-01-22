# 트리의 preorder, inorder traversal를 받아 binary tree를 만들어라!
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 재귀 코드 너무 어렵다 :(
# 보면 알겠는데, 작성하기가 어렵다는 것은 아직 모른다는 거겠지 ..
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if inorder:
            value = preorder.pop(0)
            index = inorder.index(value)
            
            node = TreeNode(value)
            node.left = self.buildTree(preorder, inorder[:index])
            node.right = self.buildTree(preorder, inorder[index+1:])
            return node