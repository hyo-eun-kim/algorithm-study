"""
## 6-2. 문자열 뒤집기

문자열을 뒤집는 함수를 작성하라.
입력값은 문자 배열이며, 리턴 없이 리스트 내부를 직접 조작하라.
"""

def solution(input):
    input.reverse()

if __name__ == '__main__':
    input1 = ["h", "e", "l", "l", "o"]
    input2 = ["H", "a", "n", "n", "a", "h"]
    solution(input1)
    print(input1)
    solution(input2)
    print(input2)