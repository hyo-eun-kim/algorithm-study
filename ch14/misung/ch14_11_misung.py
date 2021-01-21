# 이진 탐색 트리 합의 범위
# 이진 탐색 트리가 주어졌을때, L 이상 R 이하의 값을 지닌 노드의 합을 구하라.
# 이진탐색 트리 : 왼쪽이 항상 작고, 오른쪽이 항상 크다. 

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        def dfs(node):
            if not node:
                return 0

            if node.val<low :  # 노드의 값이  L보다 작으면 left는 볼필요 없다!
                return dfs(node.right)
            elif node.val>high : # 노드의 값이 R보다 크면 right 는 볼필요 없다!
                return dfs(node.left)

            return node.val + dfs(node.left) +dfs(node.right)

        return dfs(root)