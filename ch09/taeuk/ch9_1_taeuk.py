'''
20. 유효한 괄호

괄호로 된 입력값이 올바른지 판별하라.
'''

# 내 풀이
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {')': '(',
               '}': '{',
               ']': '['}
        for i in s:
            if i not in dic:
                stack.append(i)
            elif not stack or dic[i] != stack.pop():
                return False
        return True if not stack else False
    # 32 ms
    
# 다른 풀이
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        table = {')': '(',
                 '}': '{',
                 ']': '['}
        for char in s:
            if char not in table:
                stack.append(char)
            elif not stack or table[char] != stack.pop() :
                return False
        return len(stack) == 0
    # 52 ms