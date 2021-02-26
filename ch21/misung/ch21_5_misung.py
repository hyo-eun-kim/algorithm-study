# 쿠키부여
# 아이들에게 1개씩 쿠키를 나누어주어야한다.
# 각 아이 child_i 마다 그리드 팩터를 갖고 있으며, 이는 아이가 만족하는 최소쿠키의 크리를 말한다.
# 각 쿠키는 크기 s를 갖고 있으며, s>=g 이어야 아이가 만족하며 쿠키를 받는다.
# 최대 몇명의 아이들에게 쿠키를 줄수 있는지 구하여라

class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        
        g.sort() # child
        s.sort() # cookie

        child , cookie = 0,0
        while child <len(g) and cookie<len(s):
            if s[cookie] >= g[child]:  # 아이들이 만족하는 경우
                child +=1   # 다음 아이로 넘어간다.
            cookie +=1 

        return child

