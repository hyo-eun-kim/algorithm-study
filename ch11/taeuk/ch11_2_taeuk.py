'''
29. 보석과 돌

J는 보석이며, S는 갖고 있는 돌이다. S에는 보석이 몇 개나 있을까? 대소문자는 구분한다.
'''

# 내 풀이(해시 테이블 이용)
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        dic = {}
        
        for stone in stones:
            if stone not in dic:
                dic[stone] = 1
            else:
                dic[stone] += 1
                
        cnt = 0
        for jewel in jewels:
            if jewel in dic:
                cnt += dic[jewel]
                
        return cnt
    # 32 ms
    

# 파이썬 다운 방식
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(s in jewels for s in stones)
    
    # 32 ms