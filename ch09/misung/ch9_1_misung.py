# 유효한 괄호
# 괄호로 된 입력값이 올바른지 판별하라.
def isValid(s):

    stack = []
    table = {
        '}':'{',
        ']':'[',
        ')':'('
    }
    
    for i in s :
        if i not in table:
            stack.append(i)
        elif not stack or table[i] != stack.pop():   # stack 이 비어있거나, (stack 이 비어있으면 pop 할수 없으므로, 조건을 걸어줘야한다.)
                                                    #pop 한것과 동일하지 않으면 return false
            return print(False)
        print(stack)
    return print(len(stack)==0)

s = '([]{)}'
isValid(s)
