# 전위 중위 순회 결과로 이진 트리 구축
# 트리의 전위, 중위 순회 결과를 입력값으로 받아 이진 트리를 구축하라.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):  # 전위, 중위
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if inorder :
            root_val = preorder.pop(0) 
            root =  TreeNode(root_val) 
            index= inorder.index(root_val)  # 중위순회에서 루트값의 인덱스 구하기

            root.left = self.buildTree(preorder, inorder[0:index])
            root.right = self.buildTree(preorder, inorder[index+1:])

            return root