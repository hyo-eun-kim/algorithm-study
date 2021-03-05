class Solution:
    def fib(self, n: int) -> int:
        """
        f(0) = 0, f(1) = 1
        f(n) = f(n-1) + f(n-2)
        --> 앞에서부터 쌓아나가기 (tabulation) --> 메모리 44.82%
        조금 더 효율적으로 사용 가능할 듯?
        """
        arr = [0,1]

        for i in range(2,n+1):
            arr.append(arr[i-1]+arr[i-2])

        return arr[n]
