class Solution:
    def shortestPalindrome(self, s: str) -> str:
        """
        접근법
        : 가장 긴 palindrome인 부분 문자열을 앞에서부터 찾음. 그런 다음에 나머지 부분을 reverse해서 갖다 붙임
        """
        
        ## 가장 긴 palindrome 부터 찾는다
        if s != "":
            end = 2
            beg_s, sub_s = s[1:][::-1], s[0] # beg_s의 초기값 주의(palindrome이 발견되지 않았을 경우를 대비하여) 
            while end <= len(s):
                if s[:end] == s[:end][::-1]:
                    sub_s = s[:end]
                    beg_s = s[end:][::-1]
                end += 1
            return beg_s + s
        else:
            return s
                
        
        