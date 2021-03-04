'''
84. 괄호를 삽입하는 여러 가지 방법

숫자와 연산자를 입력받아 가능한 모든 조합의 결과를 출력하라.

Example 1:

Input: "2-1-1"
Output: [0, 2]
Explanation: 
((2-1)-1) = 0 
(2-(1-1)) = 2

Example 2:

Input: "2*3-4*5"
Output: [-34, -14, -10, -10, 10]
Explanation: 
(2*(3-(4*5))) = -34 
((2*3)-(4*5)) = -14 
((2*(3-4))*5) = -10 
(2*((3-4)*5)) = -10 
(((2*3)-4)*5) = 10

'''

class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        if input.isdigit():
            return [int(input)]

        def compute(left, right, op):
            result = []
            for l in left:
                for r in right:
                    result.append(eval(str(l) + op + str(r)))
            return result        
        
        results = []
        for i, value in enumerate(input):
            if value in "-+*":
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[i+1:])
                
                results.extend(compute(left, right, value))
        return results
    
    # 64 ms