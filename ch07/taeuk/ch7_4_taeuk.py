'''
10. 배열 파티션1

n개의 페어를 이용한 min(a, b)의 합으로 만들 수 있는 가장 큰 수를 출력하라.
'''

# 내 풀이
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # 정렬을 했을 때 순서대로 두개씩 묶어 min값을 뽑게 되면 그 합이 최대가 된다.
        nums.sort()
        s = 0
        # 짝수번째 index일때 항상 작은 값이 위치.
        for i, num in enumerate(nums):
            if i % 2 == 0:
                # 작은 값끼리 더해준다.
                s += num
        return s

# 파이썬다운 방식(모범답안)
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])
    # 아주 간단하다....