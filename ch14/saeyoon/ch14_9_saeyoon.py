"""
## 14-9. 정렬된 배열의 이진 탐색 트리 변환

오름차순으로 정렬된 배열을 높이 균형 이진 탐색 트리로 변환하라.
"""
from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        # 72ms
        if not nums:
            return None

        mid = len(nums) // 2

        node = TreeNode(nums[mid])
        node.left = self.sortedArrayToBST(nums[:mid])
        node.right = self.sortedArrayToBST(nums[mid + 1:])

        return node


if __name__ == '__main__':
    sol = Solution()
    print(sol.sortedArrayToBST([-10, -3, 0, 5, 9]))