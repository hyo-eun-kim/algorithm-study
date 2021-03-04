# 괄호를 삽입하는 여러가지 방법
# 숫자와 연산자를 입력받아 가능한 모든 조합의 결과를 출력하라

class Solution:
    def diffWaysToCompute(self, input):
        def compute(left,right,opt):
            results=[]
            for l in left:
                for r in right:
                    results.append(eval(str(l) + opt + str(r)))  # 여기서 eval 함수로 계산해줌
            return results

        if input.isdigit():
            return [int(input)]

        results=[]
        for i, val in enumerate(input):
            if val in "+-*": # 연산자가 등장하면
                left = self.diffWaysToCompute(input[:i])  # left와 right를 쪼갠다.
                right = self.diffWaysToCompute(input[i+1:])

                results.extend(compute(left,right,val))
        return results
            

