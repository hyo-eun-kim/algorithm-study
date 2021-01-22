class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """heap으로 안풀었다"""

        return sorted(nums)[::-1][k-1]
