# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        """
        BST 특성 상 루트와 가장 차이가 작은 것은 왼쪽 자식 노드의 가장 오른쪽 말단 노드 혹은
        오른쪽 자식 노드의 가장 왼쪽 말단 노드가 될 것임.
        따라서 이를 탐색하는 방향으로 가면 된다.
        근데 다만 여기서 비교하는 건 루트라고 정해준 게 아니라 다 탐색을 해야 된다는 거고, 그럼         in-order 순회가 제일 나음.
        """
        prev = -float("Inf")
        res = float("Inf")

        stack, node = [], root

        while stack or node:
            while node: # 가장 왼쪽 말단 노드로 내려가기 위한 작업
                stack.append(node)
                node = node.left

            node = stack.pop() # 가장 먼저 팝되는 게 왼쪽 말단 노드임

            res = min(res, node.val - prev)
            prev = node.val
            # 실제로 전단계와 현재의 차이로 일관되게 코딩을 할 수 있어서 inorder가 제일 적합

            node = node.right

        return res
