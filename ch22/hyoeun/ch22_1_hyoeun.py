'''
leetcode 169. Majority Element
https://leetcode.com/problems/majority-element/
과반수를 차지하는 엘리먼트를 출력하라
'''

# Runtime: 140 ms, faster than 69.21% of Python online submissions for Majority Element.
# Memory Usage: 15 MB, less than 30.91% of Python online submissions for Majority Element.
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        mid = len(nums) // 2
        num_cnt = defaultdict(int)

        for num in nums:
            num_cnt[num] += 1

        return sorted(num_cnt.items(), key=lambda x: (x[1], x[0]), reverse=True)[0][0]


class Solution2(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]

        half = len(nums) // 2
        a = self.majorityElement(nums[:half])
        b = self.majorityElement(nums[half:])

        # a가 nums에서 과반수 차지한다면 a 리턴
        # 그렇지 않은 경우 b를 리턴
        # 이게 왜 ... ?
        print("b={}, a={}, nums.count(a)={}".format(b, a, nums.count(a)))
        return [b, a][nums.count(a) > len(nums) // 2]
