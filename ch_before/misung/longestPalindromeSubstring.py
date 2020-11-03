# 가장 긴 팰린드롬 부문 문자열을 출력하라!!

strs = 'babad'
strs1 = 'cbbd'
def longestPanlindromeSubstring(s):

    def expand(left, right) : 
        while(left >=0 and right<= len(s) and s[left]==s[right-1]):
            left -=1
            right +=1
        return s[left+1 :right-1]  
  
    # 예외처리
    if len(s) <2 or s[:]==s[::-1] :
        return s

    result = ''
    for i in range(len(s)-1) :
        result = max(result, expand(i,i+1), expand(i,i+2), key=len)
    return print(result)

longestPanlindromeSubstring(strs)
longestPanlindromeSubstring(strs1)