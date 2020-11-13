# 배열 파티션
# n 개의 pair 를 이용한 min(a,b) 의 합으로 만들수 있는 가장 큰 수를 출력하라.

nums = [1,4,3,2]
def arrayPairSum(nums):
    nums.sort()
    result = sum(nums[::2])

    return result
arrayPairSum(nums)