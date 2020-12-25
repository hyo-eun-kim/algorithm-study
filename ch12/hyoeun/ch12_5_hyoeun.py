'''
https://leetcode.com/problems/combination-sum/

'''
from typing import List

# my solution
# faster than 13% (156ms)
# less than 32% (14.4MB)
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(partial_list, remainder_list):
            if sum(partial_list) == target:
                ans.append(partial_list)
                return
            elif sum(partial_list) > target:
                return
            else:
                for i, value in enumerate(remainder_list):
                    dfs(partial_list+[value], remainder_list[i:])

        ans = []
        candidates.sort()
        dfs([], candidates)
        return ans


if __name__ == "__main__":

    solution = Solution()
    print(solution.combinationSum([2, 3, 6, 7], 7))
    print(solution.combinationSum([2, 3, 5], 8))


