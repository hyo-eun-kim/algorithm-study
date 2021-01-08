'''
[BFS]
https://programmers.co.kr/learn/courses/30/lessons/43165
'''

'''
[] [1, 2, 3]
[1] [2, 3]
[1, 2] [3]
[1, 2, 3] []
[1, 2, -3] []
[1, -2] [3]
[1, -2, 3] []
[1, -2, -3] []
[-1] [2, 3]
[-1, 2] [3]
[-1, 2, 3] []
[-1, 2, -3] []
[-1, -2] [3]
[-1, -2, 3] []
[-1, -2, -3] []
...

'''
def solution(numbers, target):
    def dfs(index, include, not_include):
        print(include, not_include)
        if not not_include and sum(include) == target:
            nonlocal answer
            answer += 1
        if not not_include:
            # not_include가 비어있는 경우
            return

        value = numbers[index]
        dfs(index+1, include+[value], numbers[index+1:])    # + 부호
        dfs(index+1, include+[-value], numbers[index+1:])   # - 부호

    answer = 0
    dfs(0, [], numbers)
    return answer


if __name__ == "__main__":
    numbers = [1, 2, 3]
    print(numbers)
    target = 0
    print(solution(numbers, target))
