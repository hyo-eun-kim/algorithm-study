class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        """
        역순 정렬 (첫번째 자리부터 마지막 자리까지 순차적으로)
        --> 이 풀이는 안되는 걸로..
        nums_s = sorted(map(str, nums), reverse = True)
        return "".join(nums_s)
        """
        i = 1
        while i < len(nums):
            j = i
            while j > 0 and (str(nums[j-1])+str(nums[j]) < str(nums[j])+str(nums[j-1])):
                nums[j], nums[j-1] = nums[j-1], nums[j]
                j -= 1
            i += 1

        return (str(int("".join(map(str, nums)))))


        
