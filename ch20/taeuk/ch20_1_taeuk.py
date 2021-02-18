'''
75. 최대 슬라이딩 윈도우

배열 nums가 주어졌을 때 k 크기의 슬라이딩 윈도우를 오른쪽 끝까지 이동하면서 최대 슬라이딩 윈도우를 구하라.

'''

# 내 풀이

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return nums
        
        r = []
        for i in range(len(nums) - k + 1):
            r.append(max(nums[i:i+k]))
        return r
    # Time Limit Exceeded

# 추가 풀이
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return nums
        
        r = []
        a = max(nums[0:0+k])
        for i in range(len(nums) - k + 1):
  
            if (nums[i:i+k][-1] > a) and (nums[i-1] != a):
                a = nums[i:i+k][-1]
                r.append(nums[i:i+k][-1])
            elif nums[i-1] == a:
                a = max(nums[i:i+k])
                r.append(a)
            else:
                r.append(a)
        return r
    # 전보다 빨라졌으나 여전히 Time Limit Exceeded

# 데크를 사용한 풀이
class Solution:
    def maxSlidingWindow(self, nums, k):
        d = collections.deque()
        out = []
        for i, n in enumerate(nums):
            while d and nums[d[-1]] < n:
                d.pop()
            d += i,
            if d[0] == i - k:
                d.popleft()
            if i >= k - 1:
                out += nums[d[0]],
        return out
    # 1552 ms