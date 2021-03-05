'''
241. Different Ways to Add Parentheses
https://leetcode.com/problems/different-ways-to-add-parentheses/
괄호를 삽입하는 여러가지 방법
'''
class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:

        def compute(left, right, op):
            return [eval(str(l) + op + str(r)) for l in left for r in right]

        if input.isdigit():
            return [int(input)]

        results = []
        for idx, val in enumerate(input):
            if val in "+-*":
                left = self.diffWaysToCompute(input[:idx])
                right = self.diffWaysToCompute(input[idx+1:])
                print(left, right, val)
                results.extend(compute(left, right, val))
                print(results)
        return results