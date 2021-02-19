# 부분 문자열이 포함된 최소 윈도우
# 문자열 S와 T를 입력받아서 T의 모든 문자가 포함된 S의 최소 윈도우를 찾아라.
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        need = collections.Counter(t)  # 필요한 문자 각각의 개수
        missing = len(t) # 필요한 문자 전체 개수
        left= start=end=0

        for right, char in enumerate(s,1):
            missing -= need[cahr]>0  # 현재 필요한 문자가 0보다 크면 missing 1 감소
            need[char] -= 1 #  need도 1감소

            # 필요한 문자의 개수가 0 이면, left를 이동해서 줄일수 있는지 확인
            if missing ==0 :
                while left < right and need[s[left]]<0:
                    need[s[left]] +=1 # 다시 1 씩 더해가면서 0으로 만들어간다
                    left +=1

                if end == 0  or right-left <=end-start:  # 더 작은 값을 찾으면, 업데이트
                    start, end = left, right
                need[s[left]] +=1  # 
                missing +=1
                left +=1
        return s[start:end]

