# 문자열 s가 주어졌을때,
# 가장짧은 palindrome으로 convert 해라

s = 'aacecaaa' # a aacecaaa
s1= 'abb'   # bb abb
s2= 'aabba' # abb aabba
s3 = 'babbbabbaba'
# def shortestPalindrome(s):
    # def longestPalindrome(s):
    #     if len(s) < 2 or s[:] == s[::-1]:
    #         return s,0
        
    #     idx, l =0,0  # palindrome 이 시작되는 index와 palindrome 의 길이 
    #     for j in range(len(s)):
    #         if s[j-l :j+1] == s[j-l:j+1][::-1] : 
    #             idx,l = j-l, l+1
    #         elif j-l > 0 and s[j-l-1:j+1] ==s[j-l-1:j+1][::-1]:
    #             idx, l = j-l-1, l+2
    #     return s[idx:idx+l] , idx
    # #########################################################

    # long_s ,index= longestPalindrome(s)
    # reverse_s = s[::-1]

    # print('index',index)
    # print('long_s',long_s)
    # print('reverse_s', reverse_s)
    # return print(s[:index][::-1] +s)

def shortestPalindrome(s):
    r = s[::-1]
    sr = s + "+" + r

    pi = [0 for i in range(len(sr))]

    for i in range(1,len(pi)): # 전체 문자열의 비교할 인덱스
        t = pi[i-1]  # t는 찾을 문자열의 인덱스 

        while t > 0 and sr[i] != sr[t]:   # 중간단계 뛰어넘기. pi 배열을 이용하여 t인덱스를 변경 
            t = pi[t-1]
        if sr[i] == sr[t]:  # 일치하면 t를 증가시킨다.
            t += 1 
        pi[i] = t  

    return (r[0:len(s)-pi[-1]] + s)

shortestPalindrome(s3)