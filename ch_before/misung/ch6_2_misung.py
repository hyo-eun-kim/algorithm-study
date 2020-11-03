# 문자열을 뒤집는 함수를 작성. 
# 입력값은 문자 배열, 리턴없이 내부를 조작하라

# def reverseString(s) :
#     left = 0
#     right = len(s) -1 

#     while(left < right):
#         s[left], s[right] = s[right], s[left]   # swap 할때 temp 가 당연히 필요할거라 생각했는데,,, 
#                                             # python 에서 swap 을 할때는 그냥 이렇게 바꿀수 있다.
#         left +=1
#         right -=1
#     print(s)

# reverseString(['h','e','l','l','o'])

def reverseString1(s):
    s.reverse()
    print(s)
reverseString1(['h','e','l','l','o'])