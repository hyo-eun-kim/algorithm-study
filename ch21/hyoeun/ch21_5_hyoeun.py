'''
455. Assign Cookies
https://leetcode.com/problems/assign-cookies/
아이에게 쿠키 나눠주기
'''

# Runtime: 132 ms, faster than 85.76% of Python online submissions for Assign Cookies.
# Memory Usage: 15.4 MB, less than 7.74% of Python online submissions for Assign Cookies.
class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int] - 아이들의 greed factor
        :type s: List[int] - 쿠키의 양
        :rtype: int
        """
        ret = 0
        g = list(sorted(g))  # 정렬
        s = list(sorted(s))  # 정렬

        while g and s:
            if g[-1] <= s[-1]:
                # 이 아이는 쿠기를 받을 수 있다.
                ret += 1
                g.pop()
                s.pop()
            else:
                # 이 아이는 쿠키를 받지 못 한다.
                g.pop()
        return ret