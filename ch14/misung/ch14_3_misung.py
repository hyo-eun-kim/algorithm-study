# 가장 긴 동일 값의 경로 

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    longest_path =0
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node):
            if not node: 
                return 0
            print('node',node)
            left = dfs(node.left)
            right = dfs(node.right)

            if node.left and node.val == node.left.val:
                left += 1
            else:
                left = 0
            if node.right and node.val == node.right.val:
                right += 1
            else:
                right = 0
            
            print(left,right,self.longest_path)
             
            #왼쪽, 오른쪽 자식노드 간 거리의 합이 최댓값인거 저장
            self.longest_path = max(self.longest_path, left+right)

            # 자식 노드 상태값중 큰 값 리턴 
            return max(left, right)

        dfs(root)
        return self.longest_path