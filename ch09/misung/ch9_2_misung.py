# 중복 문자 제거
# 중복된 문자를 제외하고 사전식 순서로 나열하라.

s = "bcabc"  # = > abc
s1= "cbacdcbc"  # => acdb

def removeDuplicateLetters(s):
    counter, seen, stack = collections.Counter(s), set(), []

    for char in s : 
        counter[char] -= 1 # 문자를 하나씩 보면서 들어온 문자의 빈도수 감소
        if char in seen :
            continue  # 이미 처리된 문자 skip

    
        while stack and char < stack[-1] and counter[stack[-1]]>0: # char 가 stack 보다 앞선 문자이고, stack 에 있는 문자가 뒤에 남아있고, 
            seen.remove(stack.pop())  # stack 에 있는 문자를 지워!
        stack.append(char)
        seen.add(char)
    return "".join(stack)
removeDuplicateLetters(s)