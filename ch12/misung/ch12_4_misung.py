# 조합
# 전체 수 n 을 입력받아 K개의 조합을 리턴하라

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def backtrack(start, end, tmp):
            if len(tmp) == k:  # 원소의 수가 k 개가 되면
                result.append(tmp[:]) # 결과에 추가
            else:
                for i in range(start, end):  
                    tmp.append(nums[i])    # tmp = [1]
                    backtrack(i+1,end, tmp)  # backtrack(1,4, [1])
                    tmp.pop()  # tmp = []
        
        result = []
        nums = [i for i in range(1,n+1)]  # nums = 1부터 n 까지의 배열  nums = [1,2,3,4]
        backtrack(0, n, []) # n = 4
        return result