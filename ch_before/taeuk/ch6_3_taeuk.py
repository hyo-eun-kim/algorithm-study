'''
03. 로그 파일 재정렬

로그를 재정렬하라. 기준은 다음과 같다.

1. 로그의 가장 앞 부분은 식별자다.
2. 문자로 구성된 로그가 숫자 로그보다 앞에 온다.
3. 식별자는 순서에 영향을 끼치지 않지만 문자가 동일할 경우 식별자 순으로 한다.
4. 숫자 로그는 입력 순서대로 한다.
'''

# 내 풀이
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        characters, numerics = [], []
        for log in logs:
            # 숫자일 경우
            if log.split(' ')[1].isdigit():
                numerics.append(log)
            # 문자일 경우
            else:
                characters.append(log)
        # 문자일 경우만 식별자를 2순위로 두고 정렬
        characters.sort(key=lambda x: (x.split(' ')[1:],x.split(' ')[0]))
        return characters+numerics
    
# 모범답안
'''
class Solution:
    def reorderLogF i.1es(se1f, 10gs : List[str]) -> List[str] :
        1etters, digits = [], []
        for log in logs:
            if log.split( )[1].isdigit():
                digits.append(log)
            e1se:
                1etters.append(log)
        # 2개의 키를 람다 표현식으로 정렬
        1etters.sort(key=lambda x: (x.sp1it()[1:] , x.sp1it()[0]))
        return 1etters + digits
'''