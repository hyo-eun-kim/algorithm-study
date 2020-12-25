'''
순열 (서로 다른 정수를 입력받아 가능한 순열을 리턴하라)
https://leetcode.com/problems/permutations/

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Input: nums = [0,1]
Output: [[0,1],[1,0]]

Input: nums = [1]
Output: [[1]]
'''
from typing import *

# 12-2 문제에서의 아이디어를 이용하여 풀이하였습니다. (재귀)
# faster than 65% (40ms)
# less than 9% (14.6MB)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(sub_list: List, remain_list: List):
            if len(nums) == len(sub_list):
                result.append(sub_list)
                return
            for i, value in enumerate(remain_list):
                dfs(sub_list+[value], remain_list[:i]+remain_list[i+1:])

        result = []
        for i, value in enumerate(nums):
            dfs([value], nums[:i]+nums[i+1:])
        return result


# itertools를 이용하여 풀이도 가능하다.
# 하지만 대면인터뷰에서는 언급하는 정도로만 하고, 이것을 main 풀이로 두면 XX
# faster than 65% (40ms)
# less than 48% (14.3MB)
class Solution2:
    def permute(self, nums):
        import itertools
        return list(itertools.permutations(nums))


if __name__ == "__main__":
    solution = Solution()
    solution2 = Solution2()

    _input = [1, 2, 3]
    print(solution.permute(_input))
    print(solution2.permute(_input))

