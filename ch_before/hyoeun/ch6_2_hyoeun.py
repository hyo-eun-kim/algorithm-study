# 문자열을 뒤집는 함수를 작성하라.
# 입력값은 문자 배열이고, 리턴없이 리트스 내부를 직접 조작하라


def solution_1(s: list):
    last_index = len(s)-1
    bound = last_index//2

    for i in range(bound+1):
        tmp = s[i]
        s[i] = s[last_index-i]
        s[last_index-i] = tmp

    return s


def solution_2(s: list):
    # 위와 logic은 거의 비슷하지만, 조금 더 pythonic한 code
    left, right = 0, len(s)-1
    while left < right:
        s[left], s[right] = s[right], s[left]  # 동시 할당 가능하다.
        left += 1
        right -= 1
    return s


def solution_3(s: list):
    s.reverse()
    return s


def solution_4(s: list):
    s = s[::-1]
    return s


if __name__ == "__main__":
    sample1 = ['h', 'e', 'l', 'l', 'o']
    print("sol1 > ", solution_1(sample1))

    sample1 = ['h', 'e', 'l', 'l', 'o']
    print("sol2 > ", solution_2(sample1))

    sample1 = ['h', 'e', 'l', 'l', 'o']
    print("sol3 > ", solution_3(sample1))

    sample1 = ['h', 'e', 'l', 'l', 'o']
    print("sol4 > ", solution_4(sample1))
