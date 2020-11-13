class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        brute force 방법 --> O(n^3) time-out error

        nums.sort()
        tmp = 0
        res = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1,len(nums)-1):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                for k in range(j+1, len(nums)):
                    if k > j+1 and nums[k] == nums[k-1]:
                        continue
                    tmp = nums[i] + nums[j] + nums[k]
                    if tmp == 0 :
                        res.append([nums[i], nums[j], nums[k]])
        return res
        """

        # i를 고정하고, 투포인터 --> O(n^2)
        res = []
        nums.sort()

        for i in range(len(nums)-2):
            # 중복 처리
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left, right = i+1, len(nums)-1

            while left < right:
                tmp = nums[i] + nums[left] + nums[right]
                if tmp < 0:
                    left += 1
                elif tmp > 0:
                    right -= 1
                else:
                    res.append([nums[i],nums[left], nums[right]])

                    # 중복처리 해주는 부분
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1

                    left += 1
                    right -= 1

        return res
            
