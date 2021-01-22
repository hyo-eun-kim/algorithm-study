'''
54. 전위, 중위 순회 결과로 이진 트리 구축

트리의 전위, 중위 순회 결과를 입력값으로 받아 이진 트리를 구축하라.

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

결과:
    3
   / \
  9  20
    /  \
   15   7

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if inorder:
            index = inorder.index(preorder.pop(0))
            
            node = TreeNode(inorder[index])
            node.left = self.buildTree(preorder, inorder[0:index])
            node.right = self.buildTree(preorder, inorder[index+1:])
            
            return node
    # 132 ms