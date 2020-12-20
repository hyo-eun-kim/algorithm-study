# 중복 문자 없는 가장 긴 부분 문자열
# 중복 문자가 없는 가장 긴 부분 문자열의 길이를 리턴하라.

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        used ={}
        start = 0
        max_len = 0

        for i , char in enumerate(s):
            if char in used and start <= used[char]: # 이미 등장했거나, 이미등장한 char의 위치가 더 크면
                start = used[char]+1
            else : # 처음 등장한 경우
                max_len = max(max_len, i-start+1)

            # 현재 문자 위치 삽입 
            used[char] = i

        return max_len
