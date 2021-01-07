'''
44. 가장 긴 동일 값의 경로

동일한 값을 지닌 가장 긴 경로를 찾아라.

Input: root = [5,4,5,1,1,5]
Output: 2

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.result = 0
        def dfs(node: TreeNode):
            if node is None:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            if node.left and node.left.val == node.val:
                left += 1
            else:
                left = 0
            
            if node.right and node.right.val == node.val:
                right += 1
            else:
                right = 0
                
            self.result = max(self.result, left + right)
            return max(left, right)
        
        dfs(root)
        return self.result
    # 재귀가 너무 헷갈린다.
    
    # 396 ms
