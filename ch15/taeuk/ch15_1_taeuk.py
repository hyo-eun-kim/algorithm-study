'''
55. 배열의 K번째 큰 요소

정렬되지 않은 배열에서 k번째 큰 요소를 추출하라.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5

Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4

'''

# 내 풀이
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        return nums[k-1]
    
    # 64 ms

# heapq 모듈 이용
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = list()
        for n in nums:
            heapq.heappush(heap, -n)
            
        for _ in range(k-1):
            heapq.heappop(heap)
            
        return -heapq.heappop(heap)
    # 68 ms