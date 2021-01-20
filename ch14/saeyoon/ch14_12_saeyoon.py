"""
## 14-12. 이진 탐색 트리 노드 간 최소 거리

두 노드 간 값의 차이가 가장 노드의 값의 차이를 출력하라.
"""
import sys

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.pre = -sys.maxsize
        self.result = sys.maxsize

    def minDiffInBST(self, root: TreeNode) -> int:
        # 32ms
        if root is None:
            return

        # 중위 순회를 하며 차이가 가장 작은 것을 업데이트 해가는 식으로 진행
        self.minDiffInBST(root.left)
        self.result = min(self.result, root.val - self.pre)
        self.pre = root.val
        self.minDiffInBST(root.right)

        return self.result
