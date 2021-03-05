class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)

        return counter.most_common(1)[0][0]
