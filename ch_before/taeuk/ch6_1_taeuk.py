'''
01. 유효한 팰린드롬

주어진 문자열이 펠린드롬인지 확인하라. 대소문자를 구분하지 않으며，영문자와 숫자
만을 대상으로 한다.
'''

# 내 풀이
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 소문자로 바꿔주기
        s = s.lower()
        # 정규식으로 불필요한문자필터링
        s = re.sub('[^a-z0-9]','',s)
        for i in range(len(s)//2):
            if s[i] != s[-(i+1)]:
                return False
        return True

# 모범답안
'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        # 정규식으로 불필요한문자필터링
        s = re.sub( '[^a-z0-9]','', s)
        return s == s[::-1] # 슬라이싱
'''