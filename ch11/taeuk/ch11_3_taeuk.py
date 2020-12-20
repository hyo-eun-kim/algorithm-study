'''
30. 중복 문자 없는 가장 긴 부분 문자열

중복 문자가 없는 가장 긴 부분 문자열의 길이를 리턴하라.
'''

# 내 풀이
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used_char = []
        temp_length = max_length = 0
        
        for i in s:
            if i not in used_char:
                used_char.append(i)
                temp_length += 1
            
            else:
                if max_length < temp_length:
                    max_length = temp_length
                
                used_char = used_char[used_char.index(i)+1:]
                used_char.append(i)
                temp_length = len(used_char)
                
        return max(max_length, temp_length)

    # 68 ms

# 슬라이딩 윈도우와 투 포인터로 사이즈 조절
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        max_length = start = 0
        for index, char in enumerate(s):
            # 이미 등장했던 문자라면 'start' 위치 갱신
            if char in used and start <= used[char]:
                start = used[char] + 1
            else: # 최대 부분 문자열 길이 갱신
                max_length = max(max_length, index - start + 1)
                
            # 현재 문자의 위치 삽입
            used[char] = index
            
        return max_length
    
    # 40 ms
