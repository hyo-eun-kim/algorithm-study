# 가장 긴 반복 문자 대체
# 대문자로 구성된 문자열 s가 주어졌을때, 
# k번 만큼의 변경으로 만들수 있는, 연속으로 반복된 문자열의 가장 긴 길이를 구하여라.

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=r =0
        counts = collections.Counter()
        for r in range(1,len(s)+1):  # right 포인터는 하나씩 이동
            counts[s[r-1]] +=1 
            max_count = counts.most_common(1)[0][1] # 가장 자주 등장하는 단어의 횟수 체크

            if r-l-max_count >k :  # k 초과시 포인터 이동
                counts[s[l]] -=1 # 이동하는 거 count 낮춰주기
                l+=1 
        return r-l
