# 배열의 K 번째 큰 요소
# 정렬되지 않은 배열에서 K번째 큰 요소를 추출하라.

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        heap = list()
        for n in nums:
            heapq.heappush(heap,-n)  # 음수로 저장한다 => 숫자가 클수록 작은 숫자가 되겠지!

        for _ in range(k-1):
            heapq.heappop(heap) 
        
        return -heapq.heappop(heap)


        def findKthLargest2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        return sorted(nums, reverse=True)[k-1]  # 역순으로 정렬해서 바로 접근!
