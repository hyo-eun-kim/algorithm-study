'''
02. 문자열 뒤집기

문자열을 뒤집는 함수를 작성하라 입력값은 문자배열이며，리턴 없이 리스트내부를
직접 조작하라.
'''

# 내 풀이, 모범답안
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()