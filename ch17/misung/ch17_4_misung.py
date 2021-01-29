# 가장 큰 수
# 항목들을 조합하여 만들수 있는 가장 큰 수를 출력하라.

class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
    if not nums:
        return 0
        
    def compare(n1, n2):
        if int(n1+n2)>int(n2+n1):
            return -1
        else:
            return 1
        
    nums = map(str, nums)
    nums.sort(cmp = compare)
    return str(int(''.join(nums)))