"""
## 20-3. 가장 긴 반복 문자 대체

대문자로 구성된 문자열 s가 주어졌을 때 k번 만큼의 변경으로 만들 수 있는,
연속으로 반복된 문자열의 가장 긴 길이를 출력하라.
"""
from collections import Counter


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        counts = Counter()
        for right in range(1, len(s) + 1):
            counts[s[right - 1]] += 1
            max_count = counts.most_common(1)[0][1]

            if right - left - max_count > k:
                counts[s[left]] -= 1
                left += 1
        return right - left


if __name__ == '__main__':
    sol = Solution()
    print(sol.characterReplacement("ABAB", 2))
    print(sol.characterReplacement("AABABBA", 1))