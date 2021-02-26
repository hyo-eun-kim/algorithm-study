# 키에 따른 대기열 재구성
# 여러명의 사람들이 줄을 서있다.
# 각각의 사람은  (h,k) 의 두 정수 쌍을 갖는데, h는 그사람의 키
# k는 앞에 줄 서 있는 사람들 중 자신의 키 이상인 사람들의 수를 뜻한다.
# 이 값이 올바르도록 줄을 재정렬하는 알고리즘을 작성하라.
import heapq
class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        heap = []
        result =[]

        for person in people : 
            heapq.heappush(heap, (-person[0],person[1] ))  # 음수로 넣어서 최소힙을 => 최대힙으로 사용
        
        # 키가 큰 사람부터 person 에 들어간다.
        while heap:
            person = heapq.heappop(heap)
            result.insert(person[1],[-person[0],person[1]])  # person[1] 인덱스 자리에 삽입
        return result


    def reconstructQueue2(self, people):
        result = []
        for h, k in sorted(people, key=lambda x: (-x[0], x[1])):
            result.insert(k, [h, k])
        return result