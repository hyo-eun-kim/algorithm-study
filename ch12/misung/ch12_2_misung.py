## 전화번호 문자 조합
## 2에서 9 까지 숫자가 주어졌을때, 전화번호로 조합 가능한 모든 문자를 출력하라.

def letterCombinations(self, digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    def dfs(digits, path,l):

        if len(path) == l:  # 이 길이는 재귀로 계속 호출이 되어도 고정되어야 한다.
            result.append(path)
            return

        for i , digit in enumerate(digits):
            for letter in d[digit]:
                dfs(digits[i+1:],path+letter,l)  # digits 가 계속 변하기 때문에! l 을 고정으로 둬야함.

    # 예외처리
    if not digits:
        return []

    d={
        '2':['a','b','c'],
        '3':['d','e','f'],
        '4':['g','h','i'],
        '5':['j','k','l'],
        '6':['m','n','o'],
        '7':['p','q','r','s'],
        '8':['t','u','v'],
        '9':['w','x','y','z']
    }


    result=[] 
    dfs(digits,'',len(digits))
    return result