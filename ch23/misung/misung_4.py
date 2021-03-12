# DP
# n으로 표현
# https://programmers.co.kr/learn/courses/30/lessons/42895

# 아래와 같이 5와 사칙연산만으로 12를 표현할 수 있습니다.
# 12 = 5 + 5 + (5 / 5) + (5 / 5)
# 12 = 55 / 5 + 5 / 5
# 12 = (55 + 5) / 5
# 5를 사용한 횟수는 각각 6,5,4 입니다. 그리고 이중 가장 작은 경우는 4입니다.
# 이처럼 숫자 N과 number가 주어질 때, N과 사칙연산만 사용해서 표현 할 수 있는 방법 중
# N 사용횟수의 최솟값을 return 하도록 solution 함수를 작성하세요.

def solution(N, number):
    if N == number:
        return 1
    s=[set() for x in range(8)] 
    for i , x in enumerate(s):
        x.add(int(str(N)*(i+1))) # 5, 55, 555.. 추가해줌
    
    for i in range(1,len(s)):
        for j in range(i):
            for op1 in s[j]: 
                for op2 in s[i-j-1]:
                    s[i].add(op1+op2)
                    s[i].add(op1-op2)
                    s[i].add(op1*op2)
                    #print(s)
                    if op2 !=0:
                        s[i].add(op1//op2)
                    
        if number in s[i]:
            return i+1
    return -1
