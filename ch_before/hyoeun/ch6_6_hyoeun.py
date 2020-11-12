# https://leetcode.com/problems/longest-palindromic-substring/

def solution_1(s):
    # time limit exceeded (비효율 코드)
    max_palindrom = ""
    for start_index in range(len(s)):
        for end_index in range(start_index+1, len(s)+1):
            if s[start_index:end_index] == s[start_index:end_index][::-1]:
                if len(max_palindrom) < end_index - start_index + 1:
                    max_palindrom = s[start_index:end_index]
    return max_palindrom


def solution_2(s):
    def expend(s, left, right):
        if right < len(s) and s[left] == s[right]:
            while (left-1 >= 0) and (right+1 < len(s)) and (s[left-1] == s[right+1]):
                left -= 1
                right += 1
            return s[left:right+1]
        return s[left]

    # max_len 이라는 변수를 둘 필요가 전혀 없다!
    max_palindrom = ""
    for i in range(len(s)):
        # 홀수 길이의 palindrom
        sub = expend(s, i, i)
        if len(sub) > len(max_palindrom):
            max_palindrom = sub
        # 짝수 길이의 palindrom
        sub = expend(s, i, i+1)
        if len(sub) > len(max_palindrom):
            max_palindrom = sub
    return max_palindrom


# best code!
# https://leetcode.com/problems/longest-palindromic-substring/discuss/2954/Python-easy-to-understand-solution-with-comments-(from-middle-to-two-ends).
def solution_3(s):
    def expend(s, left, right):
        while (0<=left) and (right<len(s)) and (s[left]==s[right]):
            left -= 1
            right += 1
        return s[left+1:right]

    max_palindrom = ""
    for i in range(len(s)):
        sub = expend(s, i, i)
        if len(sub) > len(max_palindrom):
            max_palindrom = sub

        sub = expend(s, i, i+1)
        if len(sub) > len(max_palindrom):
            max_palindrom = sub

    return max_palindrom


if __name__ == "__main__":
    s = "babad"
    print(solution_1(s))
    print(solution_2(s))
    print(solution_3(s))