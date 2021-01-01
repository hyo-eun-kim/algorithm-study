'''
복습문제2번 : 전화번호 목록
https://programmers.co.kr/learn/courses/30/lessons/42577
'''

# 통과는 했지만 음 ..
def solution(phone_book):
    phone_book.sort()  # "10101", "101" 이런 테스트 케이스가 있어서 필요
    phone_passed = []
    for phone in phone_book:
        for key in phone_passed:
            if phone.startswith(key):
                return False
        phone_passed.append(phone)
    return True


# 다른 사람의 hashmap 이용한 풀이
def solution2(phone_book):
    hash_map = {}
    for phone in phone_book:
        hash_map[phone] = 1
    for phone in phone_book:
        phone_temp = ""
        for num in phone:
            phone_temp += num
            if phone_temp in hash_map and phone_temp != phone:
                return False
    return True


# 다른 사람의 풀이
def solution3(phoneBook):
    phoneBook = sorted(phoneBook)
    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True