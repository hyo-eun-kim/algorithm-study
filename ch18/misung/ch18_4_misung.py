# 두수의 합
# 정렬된 배열을 받아 덧셈하여 타겟을 만들수 있는 배열의 두 숫자 인덱스를 리턴하라.
# 주의 : 이 문제에서 배열은 0이 아닌 1 부터 시작하는것으로 한다.
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        l = 0
        r = len(numbers) - 1
        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l+1, r+1]
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                r -= 1