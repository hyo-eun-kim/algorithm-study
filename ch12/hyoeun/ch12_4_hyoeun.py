'''
https://leetcode.com/problems/combinations/

Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
You may return the answer in any order.

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
'''
from typing import List

# my solution
# faster than 90% (84ms)
# less than 18% (15.8MB)
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(level: int, partial_list: List):
            if len(partial_list) == k:
                answer.append(partial_list)
                return
            for i in range(partial_list[-1]+1, n-k+level+1):
                dfs(level+1, partial_list + [i])

        answer = []
        level = 1
        for i in range(1, n-k+level+1):
            dfs(level+1, [i])
        return answer


# 위의 코드를 조금 더 다듬은 결과
# faster than 88% (87ms)
# less than 36% (15.8MB)
class Solution2:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(level: int, partial_list: List, remainder: int):
            if len(partial_list) == k:
                answer.append(partial_list)
                return
            for i in range(remainder, n-k+level+1):
                dfs(level+1, partial_list + [i], i+1)

        answer = []
        dfs(1, [], 1)
        return answer

# faster than 96% (76ms)
# less than 52% (15.7MB)
class Solution3:
    def combine(self, n: int, k: int):
        import itertools
        return list(itertools.combinations(range(1, n+1), k))


if __name__ == "__main__":
    solution = Solution()
    solution2 = Solution2()
    solution3 = Solution3()

    print(solution.combine(n=4, k=2))
    print(solution2.combine(n=4, k=2))
    print(solution3.combine(n=4, k=2))

