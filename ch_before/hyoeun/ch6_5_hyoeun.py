# https://leetcode.com/problems/group-anagrams/
from collections import defaultdict


def solution_1(strs: list):
    anagrams = defaultdict(list)
    for str in strs:
        # "abc", "bca" 모두 동일한 단어로 구성 -> 문자열을 정렬하여 key로 사용하자는 아이디어
        list_str = "".join(sorted(list(str)))
        anagrams[list_str].append(str) # key에 value 추가

    return list(anagrams.values())


if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(solution_1(strs))