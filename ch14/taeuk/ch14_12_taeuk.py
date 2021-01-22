'''
53. 이진 탐색 트리(BST) 노드 간 최소 거리

두 노드 간 값의 차이가 가장 작은 노드의 값의 차이를 출력하라.

Input: root = [4,2,6,1,3,null,null]
Output: 1

diagram:

          4
        /   \
      2      6
     / \    
    1   3  

노드 3과 노드 4의 값의 차이는 1이다.

'''

# 반복 구조

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        prev = -sys.maxsize
        result = sys.maxsize
        
        stack = []
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()

            result = min(result, node.val - prev)
            
            prev = node.val
            node = node.right
            
        return result
    # 32 ms
    
# 재귀 구조
class Solution:
    prev = -sys.maxsize
    result = sys.maxsize
    
    def minDiffInBST(self, root: TreeNode) -> int:
        if root.left:
            self.minDiffInBST(root.left)
            
        self.result = min(self.result, root.val - self.prev)
        self.prev = root.val
        
        if root.right:
            self.minDiffInBST(root.right)
            
        return self.result
    # 24 ms