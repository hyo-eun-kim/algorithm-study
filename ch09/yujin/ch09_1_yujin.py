class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {")": "(",
                "}": "{",
                "]": "["}
        stack = []

        for char in s:
            if char not in pairs: # 여는 괄호면 stack에 푸시함
                stack.append(char)
            # 닫는 괄호인 경우
            else:
                if not stack:
                    return False
                if pairs[char] != stack.pop(): # empty stack --> 여는 괄호가 등장하지 않은 경우 or pair가 아닌 경우
                    return False

        return len(stack) == 0
