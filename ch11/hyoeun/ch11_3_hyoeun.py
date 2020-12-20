'''
https://leetcode.com/problems/longest-substring-without-repeating-characters/

중복 문자가 없는 가장 긴 부분 문자열의 길이를 리턴하라

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
'''

# my solution
# (runtime 148ms) faster than 21% / (memory 14.3MB) less than 64%
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 1
        max_value = 0

        while right != len(s)+1:
            unique_alpha = set(s[left:right])
            if len(unique_alpha) == right-left:
               max_value = right-left if right-left > max_value else max_value
               right += 1
            else:
                left += 1
                right += 1
        return max_value


# (runtime 48ms) faster than 95% / (memory 14.5MB) less than 15%
class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        max_length = 0
        start = 0

        for index, char in enumerate(s):
            if char in used and start <= used[char]:
                # 기존에 나왔던 적이 있고 AND 이 글자가 현재 구간에 포함되면!
                start = used[char]+1 # ⭐ 이것이 성능향상의 포인트!! ⭐
            else:
                # 기존에 나왔던 적이 없거나 OR 이 글자가 현재 구간에 포함되지 않으면!
                max_length = max(max_length, index-start+1)
            used[char] = index  # 나온 위치를 기록
        return max_length

if __name__ == "__main__":
    solution = Solution()
    solution.lengthOfLongestSubstring("abcabcd")