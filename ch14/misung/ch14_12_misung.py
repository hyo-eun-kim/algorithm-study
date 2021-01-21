# 이진 탐색 트리 노드 간 최소 거리
# 두 노드 간 값의 차이가 가장 작은 노드의 값의 차이를 출력하라

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        prev = -float('inf')
        result = float('inf')
        node = root 

        stack = []

        while stack or node :
            while node :
                stack.append(node)
                node = node.left
            node = stack.pop()

            result = min(result, node.val -prev) # 현재 저장된 값과, 노드를 뺀 값을 비교
            prev = node.val

            node = node.right 
        return result