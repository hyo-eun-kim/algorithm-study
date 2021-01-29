# 구간병합
# 겹치는 구간을 병합하라.

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()  # 일단 입력받은 리스트를 정렬하고,

        s = intervals[0][0]  # start 
        e = intervals[0][1]  # end 설정 
        result =[]

        for i in range(1,len(intervals)):
            if intervals[i][0] <=e:  # 겹치는지 확인
                if intervals[i][1] >e :
                    e =intervals[i][1]  # 겹치면 end를 업데이트
            
            else: # 겹치지 않는경우
                result.append([s,e])  
                s = intervals[i][0]
                e = intervals[i][1]
        result.append([s,e])
        return result 