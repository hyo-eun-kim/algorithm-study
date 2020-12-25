'''
https://leetcode.com/problems/letter-combinations-of-a-phone-number/
2-9 사이의 digits를 포함한 문자열이 주어질 때, 가능한 문자의 조합을 리턴하라.
answer의 순서는 상관없다.
'''
from typing import *

# my solution
# faster than 94% (24ms)
# less than 20% (14.4MB)
class Solution:
    def iterate(self, digits: List, result: List, i):
        num_to_alpha = {
            '2': ["a", "b", "c"],
            '3': ["d", "e", "f"],
            '4': ["g", "h", "i"],
            '5': ["j", "k", "l"],
            '6': ["m", "n", "o"],
            '7': ["p", "q", "r", "s"],
            '8': ["t", "u", "v"],
            '9': ["w", "x", "y", "z"]
        }

        if i == len(digits):
            return result
        elif i == 0:
            return self.iterate(digits, num_to_alpha[digits[i]], i+1)
        else:
            alphas = num_to_alpha[digits[i]]
            length = len(result)
            for _ in range(length):
                tmp = result.pop()
                for alpha in alphas:
                    result.insert(0, tmp + alpha)
            return self.iterate(digits, result, i+1)

    def letterCombinations(self, digits: str) -> List[str]:
        if str == "":
            return []
        else:
            digits = list(digits)
            result = []
            return self.iterate(digits, result, 0)

# faster than 55% (32ms)
# less than 20% (14.3MB)
class Solution2:
    def letterCombinations(self, digits: str) -> List[str]:
        def dfs(index, path):
            if len(path) == len(digits):
                result.append(path)
                return

            ########## 여기가 포인트 ##########
            for i in range(index, len(digits)):
                for j in dic[digits[i]]:
                    dfs(i+1, path+j)
            #################################

        if not digits:
            return []

        dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
               "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        result = []
        dfs(0, "")
        return result


if __name__ == "__main__":
    digits = "234"
    solution = Solution()
    print(solution.letterCombinations(digits))
