# 이진 트리의 최대 깊이
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def maxDepth1(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if node is None:
            return 0
        return max(self.maxDepth(node.left) + 1, self.maxDepth(node.right) + 1)

##########################################################################

    def maxDepth(self, root):
        if root is None : 
            return 0
        
        queue = collections.deque([root])
        depth =0

        while queue:
            depth +=1
            for _ in range(len(queue)):
                node = queue.popleft()

                # 자식노드 삽입
                if node.left:
                    queue.append(node.left)
                if node.right :
                    queue.append(node.right)


        return depth  # 반복 횟수는 깊이이다!
