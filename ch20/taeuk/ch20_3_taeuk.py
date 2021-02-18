'''
77. 가장 긴 반복 문자 대체

대문자로 구성된 문자열 s가 주어졌을 때 k번만큼의 변경으로 만들 수 있는, 
연속으로 반복된 문자열의 가장 긴 길이를 출력하라.

Example 1:

Input:
s = "ABAB", k = 2

Output:
4

Explanation:
Replace the two 'A's with two 'B's or vice versa.
 

Example 2:

Input:
s = "AABABBA", k = 1

Output:
4

Explanation:
Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.

'''

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = right = 0
        counts = collections.Counter()
        for right in range(1, len(s) + 1):
            counts[s[right - 1]] += 1
            max_count = counts.most_common(1)[0][1]

            if right - left - max_count > k:
                counts[s[left]] -= 1
                left += 1
        return right - left
    # 280 ms