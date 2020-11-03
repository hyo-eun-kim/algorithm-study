"""
## 6-3. 로그 파일 재정렬

1. 로그의 가장 앞 부분은 식별자다.
2. 문자로 구성된 로그가 숫자 로그보다 앞에 온다.
3. 식별자는 순서에 영향을 끼치지 않지만 문자가 동일할 경우 식별자 순으로한다.
4. 숫자 로그는 입력 순서대로 한다.
"""

def solution(logs):
    nums = []
    chars = []

    for log in logs:
        if log.split()[1].isdigit():
            nums.append(log)
        else:
            chars.append(log)

    chars.sort(key = lambda x: (x.split()[1:], x.split()[0]))
    chars.extend(nums)
    return chars

def solution_ans(logs):
    nums = []
    chars = []

    for log in logs:
        if log.split()[1].isdigit():
            nums.append(log)
        else:
            chars.append(log)

    chars.sort(key = lambda x: (x.split()[1:], x.split()[0]))
    return chars + nums


if __name__ == '__main__':
    logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
    print(solution(logs))
    print(solution_ans(logs))