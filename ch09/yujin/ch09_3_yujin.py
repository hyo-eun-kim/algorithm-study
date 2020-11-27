class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        """
        O(n^2)

        days = [0 for i in range(len(T))]
        stack = []

        for i in range(len(T)):
            found = False
            for k in range(i,len(T)):
                if T[k] > T[i]:
                    found = True
                    break
                days[i] += 1
            if not found:
                days[i] = 0

        return days
        """

        # stack
        days = [0 for _ in range(len(T))]
        stack= []

        for i, cur in enumerate(T):
            while stack and cur > T[stack[-1]]:
                top = stack.pop()
                days[top] = i - top
            stack.append(i)

        return days
