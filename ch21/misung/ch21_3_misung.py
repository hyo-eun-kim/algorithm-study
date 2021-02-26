# 태스크 스케줄러
# A에 Z로 표현된 태스크가 있다.
# 각 간격마다 CPU는 한번의 태스크만 실행할수 있고, 
# n번의 간격 내에는 동일한 태스크를 실행할수 없다.
# 더 이상 태스크를 실행할수 없는 경우 아이들 상태가 된다.
# 모든 태스크를 실행하기 위한 최소 간격을 출력하라.
from collections import Counter
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        if n ==0:
            return len(tasks)

        
        task_dict = Counter(tasks)
        max_occ = max(task_dict.values())  # 가장 많이 등장하는 task
        num_max = sum((1 for task,occ in task_dict.items() if occ==max_occ)) # max번 등장한 애들의 개수

        interval_for_schedule = ( max_occ-1 )*( n+1 ) + num_max

        return max( len(tasks), interval_for_schedule)


