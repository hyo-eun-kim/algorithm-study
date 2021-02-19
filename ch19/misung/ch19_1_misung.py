# 싱글 넘버
# 딱 하나를 제외하고 모든 엘리먼트는 2개씩 있다.
# 1개인 엘리먼트를 찾아라.

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        res=0
        for n in nums:  
            res^=n  # xor 를 하게 되면 두번 등장한 엘리먼트는 0으로 초기화 되고, 한번 등장 엘리먼트 값만 남게될것이므로!!!
        return res   