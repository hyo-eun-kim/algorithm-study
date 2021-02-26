'''
82. 쿠키 부여

아이들에게 1개씩 쿠키를 나눠줘야 한다. 각 아이 child_i마다 그리드 팩터(Greed Factor)
g_i를 갖고 있으며，이는 아이가 만족히는 최소 쿠키의 크기를 말한다. 각 쿠키 cookie_j
는 크기 s_j를갖고 있으며，s_j>=g_i 이어야 아이가 만족하며 쿠키를 받는다. 최대 몇 명의
아이들에게 쿠키를 줄 수 있는지 출력하라.

Example 1:

Input: g = [1,2,3], s = [1,1]
Output: 1
Explanation: You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3. 
And even though you have 2 cookies, since their size is both 1, you could only make the child whose greed factor is 1 content.
You need to output 1.
Example 2:

Input: g = [1,2], s = [1,2,3]
Output: 2
Explanation: You have 2 children and 3 cookies. The greed factors of 2 children are 1, 2. 
You have 3 cookies and their sizes are big enough to gratify all of the children, 
You need to output 2.

'''
# 내 풀이
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        
        result = 0
        child_i = 0 
        
        for cookie_j in s:
            if child_i >= len(g):
                return result
            if cookie_j >= g[child_i]:
                result += 1
                child_i += 1
        
        return result
    # 144 ms