'''
https://leetcode.com/problems/subsets/
'''
from typing import *

# faster than 79% (32ms)
# less than 54% (14.4MB)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(sub_list, remain_list):
            result.append(sub_list)
            # 종료조건
            if remain_list:
                for i, value in enumerate(remain_list):
                    dfs(sub_list+[value], remain_list[i+1:])

        result = []
        dfs([], nums)
        return result


# 책의 solution
class Solution2:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def dfs(index, path):
            result.append(path)
            for i in range(index, len(nums)):
                dfs(i+1, path+[nums[i]])
        dfs(0, [])
        return result


if __name__ == "__main__":
    solution = Solution()
    solution2 = Solution2()

    print(solution.subsets([1, 2, 3]))
    print(solution2.subsets([1, 2, 3]))
