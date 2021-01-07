"""
## 타겟 넘버

n개의 음이 아닌 정수가 있습니다. 이 수를 적절히 더하거나 빼서 타겟 넘버를 만들려고 합니다.
예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들려면 다음 다섯 방법을 쓸 수 있습니다.

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

사용할 수 있는 숫자가 담긴 배열 numbers, 타겟 넘버 target이 매개변수로 주어질 때
숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 return 하도록 solution 함수를 작성해주세요.
"""


def solution(numbers, target):
    answer = 0
    n = len(numbers)

    def dfs(index, value):
        nonlocal answer # 중첩 함수에서 UnboundLocalError 발생 방지
        if index == n:
            if value == target:
                answer += 1
            return
        else:
            dfs(index + 1, value + numbers[index])
            dfs(index + 1, value - numbers[index])

    dfs(0, 0)
    return answer


if __name__ == '__main__':
    print(solution([1, 1, 1, 1, 1], 3))
