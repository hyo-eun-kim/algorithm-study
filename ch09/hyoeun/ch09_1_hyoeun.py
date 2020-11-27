'''
leetcode20 유효한 괄호
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.
괄호로 된 입력값이 올바른지 판별하라.

Input: s = "()[]{}"     Output: true
Input: s = "{[]}"       963
    oOutput: true
'''


# my solution
# 24ms, faster than 94.03%
def isValid(s: str) -> bool:
    # 길이가 1인 입력에 대비하여 "*"라는 dummy 개념을 사용하였다.
    # 굳이 사용하지 않아도 될 것 같긴하다 ..
    bracket_pair = {"*": "*", "(": ")", "[": "]", "{": "}"}
    stack = ["*"]
    for bracket in s:
        if bracket in ['(', '[', '{']:
            stack.append(bracket)
        else:
            if bracket_pair[stack.pop()] != bracket:
                return False

    if stack.pop() != '*':
        return False
    return True


if __name__ == "__main__":
    print(isValid("]"))
    print(isValid("()[]{}"))
