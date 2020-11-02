import collections

def answer_1(s: str):
    # 이러한 답안은 알고리즘이라고 할 것이 없다...!
    new_s = ""
    for x in s.lower():
        if x.isalnum():
            new_s += x

    return (new_s == new_s[::-1])


def answer_2(s: str):
    # 리스트에서 뒤에서 pop하는 것은 O(1)
    # 리스트에서 앞에서 pop(0)하는 것은 O(n) -> 비효율적
    new_s = []
    for x in s.lower():
        if x.isalnum():
            new_s.append(x)
    while len(new_s) > 1:
        if new_s.pop(0) != new_s.pop():
            return False
    return True


def answer_3(s: str):
    # deque에서 뒤에서 pop하는 것은 O(1)
    # deque에서 앞에서 popleft하는 것은 O(1) -> list가 아닌 deque 자료구조를 사용하여 성능 개선
    deque: Deque = collections.deque()
    for x in s.lower():
        if x.isalnum():
            deque.append(x)

    while len(deque) > 1:
        if deque.popleft() != deque.pop():
            return False
    return True

if __name__ == '__main__':
    s = "A man, a plan, a canal: Panama"
    print(answer_1(s))
    print(answer_2(s))
    print(answer_3(s))