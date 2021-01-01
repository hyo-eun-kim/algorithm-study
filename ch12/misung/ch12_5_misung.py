# 조합의 합
# 숫자 집합 candidates 를 조합하여 합이 target이 되는 원소를 나열하라.
# 각 원소는 중복으로 나열 가능하다.

candinates =[2,3,6,7]
target = 7

def combinationSum(candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    def dfs(cur, cur_sum, idx):             
        if cur_sum > target:   # 합 이 target 보다 더 크면 넘겨버려
            return                  

        if cur_sum == target:  # 합이 target 과 같으면, 
            result.append(cur)  # result 에 cur 저장!
            return 

        for i in range(idx, n):  # i = 0,1,2,3
            dfs(cur + [candidates[i]], cur_sum + candidates[i], i) 
        
    result = []
    n = len(candidates)  # n=4
    dfs([], 0, 0)
    return result   