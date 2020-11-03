# 로그 파일의 재정렬
# 문자로 구성된 로그가 숫자 로그보다 앞에
# 숫자로그는 입력 순서대로
# 식별자는 순서에 영향을 끼치지는 않지만, 문자가 동일할 경우 식별자순으로 한다.

logs = ['dig1 8 1 5 1','let1 art can','dig2 3 6', 'let2 own kit dig','let3 art zero']
def reorderLogFile(logs):

    letters = []  # 문자로그
    digits = []  # 숫자로그

    for log in logs:
        if log.split()[1].isdigit():  # 숫자로그인지 확인
            digits.append(log)   # 숫자로그는 입력순서대로 하면 되니까 그대로
        else:
            letters.append(log) 

    # 문자로그는 문자를 가지고 sort + 문자동일하면 식별자순  (sort의 조건이 2가지다.)
    # sorted : 원본은 변하지 않고 sort 해준다.
    sort_letters = sorted(letters,key=lambda x: (x.split()[1] , x.split()[0]))

    # sort : 원본 list 값이 sort 된 값으로 변한다. 
    letters.sort(key=lambda x : (x.split()[1], x.split()[0]) )

    print(sort_letters)
    print(letters)
    
    return print(digits + letters)
                         
reorderLogFile(logs)