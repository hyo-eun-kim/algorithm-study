# 상위 K 빈도 요소
# k 번 이상 등장하는 요소를 추출하라.
import collections
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq = collections.Counter(nums).most_common(k)  # 빈도수를 저장

        return list(zip(*freq))[0]  # *로 unpacking 해 주어야 튜플의 값을 풀어헤칠수 있다!?!
        #return [i for i,j in freq]




    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq = collections.Counter(nums)  # 빈도수를 저장
        freq_heap = []
        top_k =[]

        for val, n  in freq.items() :
            heapq.heappush(freq_heap,(-n, val))  # 빈도수(n)를 key 로 한다. 왜? 힙은 key 로 정렬되기 때문에 . 최소힙을 제공하니까 값을 음수로 저장!
        
        # K 개의 원소만 pop
        for i in range(k):
            top_k.append(heapq.heappop(freq_heap)[1])

        return top_k
