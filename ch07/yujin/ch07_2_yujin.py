class Solution:
    def trap(self, height: List[int]) -> int:
        """
        스택을 이용해서 풀이
        - 0이 아닌 애에서부터 전진
        - 스택 선언함. 시작값보다 큰 애를 만날 때까지 스택에 push
        - 큰 애를 만나면 얘가 끝값이자 다음 시작값이 되는 거임.
        - 시작값 기준으로 스택 길이만큼 곱해서 직사각형의 넓이를 구함.
        - 거기서 스택에서 push하면서 0이 아닌 애들의 개수를 다 빼줌.
        - 시작값과 넓이만 가지고 계속 전진함.

        --> 위를 배열의 끝까지 반복함.

        리스트로 충분히 구현 가능


        """
        """
        위에 풀이로 가면 start보다 end가 작은데도 물이 trapped될 수 있는 상황을 무시함.

        - code 예시
        start = height[0]
        stack = []
        res = 0
        for i in range(1, len(height)):
            if height[i] < start and i < len(height)-1:
                stack.append(height[i])
                continue
            res += start * (len(stack)) - sum(stack)
            print(i, res)
            start = height[i]
            stack = [] # 초기화

        return res

        """

        # 변곡점을 잡기

        stack = []
        res = 0

        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                # 반복 조건: stack가 empty가 아니고, 현재 값이 stack의 마지막 원소보다 작음
                top = stack.pop()

                if not len(stack): # 다시 한번 empty stack 처리
                    break

                w = i - stack[-1] -1
                h = min(height[i], height[stack[-1]]) - height[top] # 이 부분이 앞에서 내가 고려 못한 부분

                res += w*h

            stack.append(i)

        return res
                
