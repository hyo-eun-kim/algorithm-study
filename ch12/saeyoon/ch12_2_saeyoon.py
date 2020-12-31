"""
## 12-2. 전화 번호 문자 조합

2에서 9까지 숫자가 주어졌을 때 전화 번호로 조합 가능한 모든 문자를 출력하라.
"""
from typing import *


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # 28ms
        dic = {"2": "abc", "3": "def", "4": "ghi",
               "5": "jkl", "6": "mno", "7": "pqrs",
               "8": "tuv", "9": "wxyz"}
        if len(digits) == 0:
            return []

        result = ['']
        for d in digits:
            result = [i + j for i in result for j in dic[d]]
        return result

    def letterCombinations2(self, digits: str) -> List[str]:
        # 32ms
        def dfs(dic, digits, path):
            # 끝까지 탐색하면 백트래킹
            if not digits:
                result.append(path)
                return
            # 숫자에 해당하는 문자열 반복
            for c in dic[digits[0]]:
                dfs(dic, digits[1:], path + c)

        dic = {"2": "abc", "3": "def", "4": "ghi",
               "5": "jkl", "6": "mno", "7": "pqrs",
               "8": "tuv", "9": "wxyz"}
        if len(digits) == 0:
            return []

        result = []
        dfs(dic, digits, "")
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.letterCombinations("23"))
    print(sol.letterCombinations2("23"))