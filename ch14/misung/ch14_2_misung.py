# 이진 트리의 직경
# 이진 트리에서ㅕ 두 노드 간 가장 긴 경로의 길이를 출력하라.

# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    diameter = 0
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def dfs(node):
            if not node:
                return 0   # 존재하지 않는 노드 
            
            left = dfs(node.left)  # 왼쪽, 오른쪽 leaf 노드 까지 탐색
            right = dfs(node.right)

            self.diameter = max(self.diameter, left + right)  #가장 긴 경로

            return max(left, right) + 1  # left sub tree의 depth, right sub tree의 depth
        
        dfs(root)
        return self.diameter