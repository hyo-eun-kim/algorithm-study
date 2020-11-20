class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        전략: 싸게 사고 비싸게 판다.
        싸게 사고 비싸게 판다는 것의 정의: 일단 마지막 원소를 제외하고 배열의 최솟값을 찾는다. 그 이후의 인덱스에서 배열 최댓값을 찾는다.
        (이렇게 되는 경우 그 이후 인덱스에서 배열 최댓값을 찾는다고 해도 차이의 최댓값을 보장할 수 없음)
        차이를 구하는 수밖에 없나? --> brute force는 tle 발생
        """

        # brute force: O(n^2) 풀이 --> time out
        res = 0

        for i in range(len(prices)-1): # O(n^2)
            for j in range(i+1,len(prices)):
                res = max(res, prices[j] - prices[i])
        return res


        # stack이랑 비슷하게 풀이? (O(n)에 풀 수 있을 듯) --> 굳이 pop을 안할 뿐
        stack = [] # stack에 prices 첫번째 원소 push
        res = 0
        if not prices: # prices empty
            return res
        for i in range(len(prices)):
            if i == 0:
                stack.append(prices[0])
            #print(f"Loop {i}: top of the stack: {stack[-1]}, max_price: {res}")
            if stack[-1] > prices[i]:
                stack.append(prices[i])
            else:
                res = max(res, prices[i] - stack[-1]) # 큰 값을 res로 업데이트함.
        return res


        # 책 풀이
        profit = 0
        min_price = sys.maxsize # system에서 최댓값

        for price in prices:
            min_price = min(min_price, price) # 현재 가격과 현재까지의 최소 가격을 비교해서 저점을 갱신함
            profit = max(profit, price - min_price) # 현재 가격과 최소 가격의 차이만큼과 지금까지의 최대 profit을 비교해서 max값으로 업뎃
            """
            why price - min_price?
            min_price는 지금까지의 저점임.
            price - min_price과 profit 간의 max를 구하는 건 고점 갱신과 저점 갱신을 한꺼번에 고려한다고 볼 수 있겠음.
            (물론 고점 갱신과 저점 갱신이 같은 iteration 내에 갱신되지는 않지만,
            min_price가 갱신됨으로써 profit이 최적화될 수도 있고 price가 바뀜으로써 profit이 최적화될 수도 있음.)
            --> 근데 이 부분이 나한테 직관적으로 와닿지는 않음.
            """
        return profit
        
