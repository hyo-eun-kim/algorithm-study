class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        map_dict = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        result = []

        def dfs(idx, path):
            if len(path) == len(digits):
                result.append(path)
                return

            for i in range(idx, len(digits)):
                for j in map_dict[digits[i]]:
                    dfs(i+1, path+j)

        if not digits: # empty input
            return []

        dfs(0,"") # dfs 호출

        return result
        
