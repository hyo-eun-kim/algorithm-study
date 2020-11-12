# https://leetcode.com/problems/shortest-palindrome/
# given a string s, you can convert it to a palindrome by adding characters in front of it
# Find and return the shortest padlindrome you can find by performing this transformation.

def shortest_palindrome(s: str) -> str:
    if s == s[::-1]:
        return s
    else:
        


if __name__ == "__main__":
    s = "aacecaaa"
    print(shortest_palindrome("aaa"))
    print(shortest_palindrome(s))
