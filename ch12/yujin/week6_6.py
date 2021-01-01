class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(index, path):
            # path를 결과에 추가함 --> path가 결국엔 부분집합이므로
            result.append(path)

            for i in range(index, len(nums)):
                dfs(i+1, path+[nums[i]]) # i+1 넘겨주는 거

        dfs(0,[])
        return result
