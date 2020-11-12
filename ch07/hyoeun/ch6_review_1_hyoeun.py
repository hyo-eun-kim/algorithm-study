# https://leetcode.com/problems/shortest-palindrome/
# given a string s, you can convert it to a palindrome by adding characters in front of it
# Find and return the shortest padlindrome you can find by performing this transformation.

def shortest_palindrome(s: str) -> str:
    if s == s[::-1]:
        return s
    else:
        index = 1
        # find palindrome
        for i in range(len(s), 0, -1):
            if s[:i] == s[:i][::-1]:
                index = i
                break
        s = s[index:][::-1]+s
        return s


if __name__ == "__main__":
    print(shortest_palindrome("aacecaaa"))
    print(shortest_palindrome("abcd"))