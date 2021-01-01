class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(cumsum, idx, path):
            # 종료 조건
            if cumsum < 0:
                return
            if cumsum == 0:
                result.append(path)
                return

            # 재귀 호출
            for i in range(idx, len(candidates)):
                dfs(cumsum - candidates[i], i, path + [candidates[i]]) # 자기 자신부터 시작


        dfs(target, 0, [])
        return result
