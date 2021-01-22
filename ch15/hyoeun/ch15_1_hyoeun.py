# https://leetcode.com/problems/kth-largest-element-in-an-array/
# 정렬되지 않은 배열에서 k번째로 큰 요소를 찾아라.
# [3, 2, 1, 5, 6, 4], k=2 -> 5

# runtime: 64ms (faster than 72.39%)
# memory: 15MB (less than 77%)
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # python은 min heap으로 반전해서 넣어주기
        nums = list(map(lambda x:-x, nums))
        # heapify
        heapq.heapify(nums)
        # k-1번 pop
        for _ in range(k-1):
            heapq.heappop(nums)
        # return
        return -heapq.heappop(nums)

# 내장함수 이용
class Solution2:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums, reverse=True)[k-1]