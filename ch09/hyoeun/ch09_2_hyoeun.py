'''
leetcode 316
https://leetcode.com/problems/remove-duplicate-letters/

Given a string s, remove duplicate letters so that every letter appears once and only once. (중복 X)
You must make sure your result is the smallest in lexicographical order among all possible results. (정렬)

Input: s = "bcabc"      Output: "abc"
Input: s = "cbacdcbc"   Output: "acdb"
'''

def removeDuplicateLetters(s: str) -> str:
    d = {char: index for index, char in enumerate(s)}
    final_s = []

    for index, char in enumerate(s):
        if char not in final_s:
            # final_s가 비어있지 X AND
            # 마지막의 요소보다 char의 우선순위가 높고 AND
            # 마지막의 요소는 뒤에서 한 번 더 나타난다는 보장 있는 경우
            # -> 마지막 요소 pop
            while final_s and final_s[-1] > char and d[final_s[-1]] > index:
                final_s.pop()
            final_s.append(char)
    return "".join(final_s)


if __name__ == "__main__":

    removeDuplicateLetters("bcabc")     # abc
    removeDuplicateLetters("cbacdcbc")  # acdb
