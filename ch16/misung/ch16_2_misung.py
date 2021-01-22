# 팰린드롬 페어
# 단어 리스트에서 words[i] + words[j] 이 팰린드롬이 되는 모든 인덱스 조합 (i,j) 를 구하라
# 팰린드롬 : 앞 뒤가 똑같은 단어나 문장으로 뒤집어도 같은 말이 되는 문장

class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        def is_palindrome(check):
            return check == check[::-1]

        words = {word: i for i, word in enumerate(words)}
        valid_pals = []

        for word,k in words.items():
            n = len(word)
            for j in range(n+1):
                pref = word[:j]   # 접두사
                suf = word[j:]    # 접미사

                if is_palindrome(pref):  # 접두사가 palidrom 이면, 
                    back = suf[::-1]
                    if back != word and back in words : # 접미사를 뒤집은게 words 에 존재하면,  ( + 접미사가 현재 단어가 아니면 )
                        valid_pals.append([words[back], k])   # right[::-1] + left + right = right[::-1] + word 는 palindrome
                
                if j != n and is_palindrome(suf):   # 접미사가 palidrom 이면, 
                    back = pref[::-1] 
                    if back != word and back in words:
                        valid_pals.append([k, words[back]])  # left + right + left[::-1] = word + left[::-1] 이 palindrome
        return valid_pals
        