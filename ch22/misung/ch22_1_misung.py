# 과반수 엘리먼트
# 과반수를 차지하는 엘리먼트를 출력하라
import collections
class Solution:
    def majorityElement(self, nums):
        counts = collections.defaultdict(int)

        for num in nums:
            if counts[num] ==0:
                counts[num] = nums.count(num)
            if counts[num] > len(nums)//2:
                return num



    def majorityElement2(self,nums):
        d = collections.Counter(nums)
        for i in d:
            if d[i] >len(nums)//2:
                return i