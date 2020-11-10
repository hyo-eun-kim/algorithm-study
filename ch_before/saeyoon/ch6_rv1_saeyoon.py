"""
## 복습 6-1. Shortest Palindrome

# leetcode 214
Given a string s, you can convert it to a palindrome by adding characters in front of it.
Find and return the shortest palindrome you can find by performing this transformation.
"""


def shortestPalindrome(s: str) -> str:
    # Runtime: 696 ms
    if s == s[::-1]:
        return s
    else:
        for i in range(len(s)):
            new_s = s[-1 - i:][::-1] + s
            if new_s == new_s[::-1]:
                break
    return new_s


def shortestPalindrome2(s: str) -> str:
    # KMP Algorithm
    # s + rev_s
    # find prefix(s) which is longest suffix(rev_s)
    # remove the longest suffix from rev_s
    # [rev_s - Lsuffix(rev_s)] + s
    # https://www.youtube.com/watch?v=c4akpqTwE5g

    # Runtime: 56 ms
    new_s = s + "#" + s[::-1]
    p = [0] * len(new_s)
    for i in range(1, len(new_s)):
        j = p[i - 1]
        while (j > 0) & (new_s[i] != new_s[j]):
            j = p[j - 1]
        if new_s[i] == new_s[j]:
            p[i] = j + 1
    return s[::-1][:len(s) - p[len(new_s) - 1]] + s


if __name__ == '__main__':
    input1 = "aacecaaa"
    input2 = "abcd"
    print(shortestPalindrome(input1))
    print(shortestPalindrome(input2))
    print(shortestPalindrome2(input1))
    print(shortestPalindrome2(input2))
