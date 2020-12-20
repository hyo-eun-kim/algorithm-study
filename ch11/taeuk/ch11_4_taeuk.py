'''
31. 상위 K 빈도 요소

k번 이상 등장하는 요소를 추출하라.
'''

# 내 풀이
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [i[0] for i in collections.Counter(nums).most_common(k)]
    
    # 92 ms
    
    
# 해시테이블, 우선순위 큐 사용
class Solution:
    def topKFrequent(self, nums: List[int] , k: int) -> List[int]:
        freqs = collections.Counter(nums)
        freqs_heap = []
        # 힙에 음수로 삽입
        for f in freqs:
            heapq.heappush(freqs_heap, (-freqs[f], f))

        topk = list()
    # k번 만큼 추출，최소 힙(Min Heap)이므로 가장 작은 음수 순으로 추출
        for _ in range(k):
            topk.append(heapq.heappop(freqs_heap)[1])
        return topk

    # 100 ms
    
# 파이썬 다운 방식
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return list(zip(*collections.Counter(nums).most_common(k)))[0]
    
    # 88 ms