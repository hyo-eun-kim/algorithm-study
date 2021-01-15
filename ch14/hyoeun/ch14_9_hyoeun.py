'''
50. 정렬된 배열의 이진 탐색 트리 변환
오름차순으로 정렬된 배열을 높이 균형 이진 탐색 트리로 변환하라.
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
'''
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 재귀코드 계속 읽기!
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return  # 종료조건
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])
        return root
