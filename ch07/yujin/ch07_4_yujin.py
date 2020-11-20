class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        """
        # 내 풀이
        nums.sort() # 정렬
        return sum(nums[i] for i in range(0,len(nums),2))
        """
        # the most pythonic way
        return sum(sorted(nums)[::2])
