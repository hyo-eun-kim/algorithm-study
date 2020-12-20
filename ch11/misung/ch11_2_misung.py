# 보석과 돌
# j는 보석이며, s 는 갖고있는돌이다.
# s 에는 보석이 몇개나 있을까?
# 대소문자는 구분한다.

class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        n= 0
        for i in stones : 
            if i in jewels :
                n +=1
        return n