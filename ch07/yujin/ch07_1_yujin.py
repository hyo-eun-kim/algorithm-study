class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        nums_dict = {v:k for k,v in enumerate(nums)} # dict로 하면 값 중복 처리가 안되어서 문제가 발생함.
        nums.sort()

        left, right = 0, len(nums)-1
        while left != right:
            if nums[left] + nums[right] < target:
                left += 1
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                return [nums_dict[nums[left]], nums_dict[nums[right]]]
        """
        nums_dict = {v:k for k,v in enumerate(nums)}

        for i, num in enumerate(nums):
            if target - num in nums_dict and i != nums_dict[target - num]:
                return i, nums_dict[target-num]
