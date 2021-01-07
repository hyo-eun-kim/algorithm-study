'''
45. 이진 트리 반전

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9

Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        q = collections.deque([root])
        
        while q:
            node = q.popleft()
            
            if node:
                node.left, node.right = node.right, node.left
                
                q.append(node.left)
                q.append(node.right)
                
        return root
    # 36 ms
