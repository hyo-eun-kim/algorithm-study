 # 부분집합
# 모든 부분집합을 리턴하라.

nums = [1,2,3]
def subsets(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
        
    def backtrack(start, end, tmp):
        result.append(tmp[:])  # 무조건 붙이고 시작

        for i in range(start,end):  # i = 0,1,2
            tmp.append(nums[i])  # tmp = [1]
            backtrack(i+1, end, tmp)
            tmp.pop()
    
    result = []
    backtrack(0, len(nums), [])  # (0,3,[])
    return result