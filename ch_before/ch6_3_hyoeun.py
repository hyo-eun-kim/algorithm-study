# leetcode.com/problems/reorder-data-in-log-files/﻿


def solution_1(logs: list):
    digits_logs = []
    alpha_logs = []
    for log in logs:
        # 식별자 이후 문자만 혹은 숫자만 나오므로 다음과 같은 조건식 괜찮다
        if log.split()[1].isdigit():
            digits_logs.append(log)
        else:
            alpha_logs.append(log)

    alpha_logs = sorted(alpha_logs, key=lambda x:(x.split()[1:], x.split()[0]))
    return alpha_logs + digits_logs


if __name__ == "__main__":
    logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
    print(solution_1(logs))