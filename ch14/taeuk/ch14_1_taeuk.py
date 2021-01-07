'''
42. 이진 트리의 최대 깊이
이진 트리의 최대 깊이를 구하라.

Input: root = [3,9,20,null,null,15,7]
Output: 3

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def maxDepth(self, root):
        q = collections.deque()
        if not root:
            return 0
        q.append(root)
        maxdepth = 0
        
        while q:
            maxdepth += 1
            for _ in range(len(q)):
                node = q.popleft()
                
                # TreeNode에서 q의 제일 왼쪽인 node를 떼어냈을 때 node.left가 어떻게 존재하는 것인가..?
                # TreeNode가 원래 그런가?
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return maxdepth

    # 44 ms

# 파이썬스러운 풀이
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return 1 + max(map(self.maxDepth, (root.left, root.right))) if root else 0
    
    # 72 ms
