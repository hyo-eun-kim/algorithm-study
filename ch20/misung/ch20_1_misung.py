# 최대 슬라이딩 윈도우
# 배열 nums가 주어졌을때, k 크기의 슬라이딩 윈도우를 오른쪽 끝까지 이동하면서 최대 슬라이딩 윈도우를 구하라.

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return nums
        
        r =[]
        for i in range(len(nums)-k+1):
            r.append(max(nums[i:i+k]))
        return r


    def maxSlidingWindow2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        q, res = collections.deque(), []
        for i in range(len(nums)):
            if i-k >= 0:  # k개 들어왔을때, 
                res.append(nums[q[0]]) # res에 현재 가장 큰 값이 들어있는 인덱스 값 추가
                while q and q[0]<=i-k:  # 
                    q.popleft()
            while q and nums[i] > nums[q[-1]]:  # 큐에 들어있는 인덱스의 값이랑, 다음 윈도우에 새롭게 들어온 데이터 비교
                q.pop()  #  윈도우에 새롭게 들어온 데이터 값이 더 크면 q에 있는  인덱스 꺼낸다! => q에는 max 값의 인덱스를 기록하기 위함
            q.append(i)
        res.append(nums[q[0]])
        return res

