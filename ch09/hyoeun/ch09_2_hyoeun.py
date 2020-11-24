'''
leetcode 316
https://leetcode.com/problems/remove-duplicate-letters/

Given a string s, remove duplicate letters so that every letter appears once and only once. (중복 X)
You must make sure your result is the smallest in lexicographical order among all possible results. (정렬)

Input: s = "bcabc"      Output: "abc"
Input: s = "cbacdcbc"   Output: "acdb"
'''


def removeDuplicateLetters(s: str) -> str:



if __name__ == "__main__":
    print(removeDuplicateLetters("bcabc"))
    print(removeDuplicateLetters("cbacdcbc"))
