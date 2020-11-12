'''
11. 자신을 제외한 배열의 곱

배열을 입력받아 output[i]가 자신을 제외한 나머지 모든 요소의 곱셈 결과가 되도록 출력하라.
'''

# 내 풀이
# 시간초과가 나온다. 전부 돌릴게 아니라 양 옆을 나눠서 곱하는게 더 빨랐다.
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mul = []
        for i in range(len(nums)):
            p = 1
            for j in range(len(nums)):
                if j != i:
                    p = p * nums[j]
            mul.append(p)
        return mul

# 모범답안
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        p = 1
        #왼쪽곱셈
        for i in range(0, len(nums)):
            out.append(p)
            p = p * nums[i]
        p = 1
        # 왼쪽 곱셈 걸과에 오른쪽 강을 차례대로 곱생
        for i in range(len(nums) - 1, 0 - 1, -1):
            out[i] = out[i] * p
            p = p * nums[i]
        return out