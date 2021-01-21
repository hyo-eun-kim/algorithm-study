# 두 이진트리를 병합하라.
# 중복되는 노드는 값을 합산한다.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        result_node = TreeNode()
        if not t1: 
            return t2
        if not t2: 
            return t1

        result_node.data = t1.data + t2.data

        result_node.left = self.mergeTrees(t1.left, t2.left)
        result_node.right = self.mergeTrees(t1.right, t2.right)
        return result_node