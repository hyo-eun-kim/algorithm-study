class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        def compute(left, right, op):
            res = []
            for l in left:
                for r in right:
                    res.append(eval(str(l)+op+str(r)))
            return res

        if len(input) == 0:
            return []

        if input.isdigit(): # length로 판단하기에는 숫자가 있어서 안된다.
            return [int(input)]

        ## 분할점 지정
        results = []
        for index, value in enumerate(input):
            if value in "-+*":
                left = self.diffWaysToCompute(input[:index]) # operator 이전까지
                right = self.diffWaysToCompute(input[index+1:])

                results.extend(compute(left, right, value))

        return results
        
