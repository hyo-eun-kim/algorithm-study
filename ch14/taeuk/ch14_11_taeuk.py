'''
52. 이진 탐색 트리(BST) 합의 범위

이진 탐색 트리(BST)가 주어졌을 때 L 이상 R 이하의 값을 지닌 노드의 합을 구하라.

Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32

'''

# 내 풀이

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if root == None: 
            return 0
        if root.val > high: 
            return self.rangeSumBST(root.left,low,high)
        if root.val < low: 
            return self.rangeSumBST(root.right,low,high)
        
        return root.val + self.rangeSumBST(root.left,low,high) + self.rangeSumBST(root.right,low,high)  
    # 212 ms
    

# DFS 가지치기로 필요한 노드 탐색
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        def dfs(node: TreeNode):
            if not node:
                return 0

            if node.val < low:
                return dfs(node.right)
            elif node.val > high:
                return dfs(node.left)

            return node.val + dfs(node.left) + dfs(node.right)
        
        return dfs(root)
    # 184 ms
    
# 반복 구조 DFS로 필요한 노드 탐색
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        stack, sum = [root], 0
        # 스택 이용 필요한 노드 DFS 반복
        while stack:
            node = stack.pop()
            if node:
                if node.val > low:
                    stack.append(node.left)
                if node.val < high:
                    stack.append(node.right)
                if low <= node.val <= high:
                    sum += node.val
        return sum
    # 192 ms
    
# 반복 구조 BFS로 필요한 노드 탐색
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        stack, sum = [root], 0
        while stack:
            node = stack.pop(0)
            if node:
                if node.val > low:
                    stack.append(node.left)
                if node.val < high:
                    stack.append(node.right)
                if low <= node.val <= high:
                    sum += node.val
        return sum
    # 212 ms