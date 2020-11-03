# def isPalindrome(s):
#     strs = []

#     for i in s :
#         if i.isalnum():   # i가 알파벳이나 숫자면,
#             strs.append(i.lower())
#     #print(strs)
#     while len(strs)>1 :
#         if strs.pop(0) != strs.pop():
#             return False
#     return True

# isPalindrome('A man, a plan, a canal: Panama')

import re
def isPalindrome1(s):
    s=s.lower()   # 소문자로 바꾸고
    s=re.sub('[^a-z0-9]','',s)  # 소문자 숫자 빼고 없애기

    # return print(s==s.reverse())       #이거는 안됨. 왜냐? reverse는 문자열에서 사용불가! list 에서만 가능함.
    return print(s == s[::-1])

isPalindrome1('A man, a plan, a canal: Panama')