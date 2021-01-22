# BST가 주어졌을 때 low 이상 high 이하의 값을 지닌 노드의 합을 구하여라!

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# my solution
# runtime : 268ms (faster than 28%) <- 모든 경우를 탐색해서 느리다 (pruning 아이디어 꼭 기억!)
# memory: 22.3MB (less than 19.48%)
class Solution:
    def __init__(self):
        self.cum_sum = 0
        
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if root is None:
            return
        if low <= root.val and root.val<=high:
            self.cum_sum += root.val
        self.rangeSumBST(root.left, low, high)
        self.rangeSumBST(root.right, low, high)
        return self.cum_sum

# solution1 (비추!)
# runtime: 280ms (faster than 17%)
# memory: 22.2MB (less than 63%)
class BookSolution1:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if not root:
            return 0

        return (root.val if low <= root.val <= high else 0) + \
                self.rangeSumBST(root.left, low, high) + \
                self.rangeSumBST(root.right, low, high)

# solution2 (추천!!!!) with pruning
# runtime: 192ms (faster than 97%)
# memory: 22.3MB (less than 63%)
class BookSolution2:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        def dfs(node: TreeNode):
            if not node:
                return 0
            if node.val < low:
                # 현재 노드의 value가 low보다 작다면
                # left subtree에 존재하는 모든 node의 value는 low보다 작기 떄문에
                # right subtree만 탐색
                return dfs(node.right)
            elif node.val > high:
                # 현재 노드의 value가 high보다 크다면
                # right subtree에 존재하는 모든 node의 value는 high보다 크기 떄문에
                # left subtree만 탐색
                return dfs(node.left)
            else:
                return node.val+dfs(node.left)+dfs(node.right)
        return dfs(root)


# DFS
# runtime: 192ms (faster than 97%)
# memory: 22.3MB (less than 63%)
class BookSolution3:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        stack = [root]
        _sum = 0
        while stack:
            node = stack.pop()
            if node:
                if node.val > low:
                    # 즉 node.val <= low라면 lef node를 append X
                    stack.append(node.left)
                if node.val < high:
                    # 즉, node.val >= high라면 right node를 append X
                    stack.append(node.right)
                if low <= node.val <= high:
                    _sum += node.val
        return _sum


# BFS
# runtime: 208ms (faster than 70.22%)
# memory: 22.5MB (less than 7%)
class BookSolution4:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        stack = [root]
        _sum = 0
        while stack:
            node = stack.pop(0) # queue처럼 이용하는 것
            if node:
                if node.val > low:
                    stack.append(node.left)
                if node.val < high:
                    stack.append(node.right)
                if low <= node.val <= high:
                    _sum += node.val
        return _sum
