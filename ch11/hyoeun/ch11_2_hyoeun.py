'''
https://leetcode.com/problems/jewels-and-stones/

J는 보석이고, S는 갖고있는 돌이다. S에 보석이 몇 개나 있을까? 대소문자를 구분한다.

Input: jewels = "aA", stones = "aAAbbbb"
Output: 3

Input: jewels = "z", stones = "ZZ"
Output: 0
'''

import collections

# 1. 나의 솔루션 (파이썬 기본 dictionary 이용한 풀이)
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:

        stone_to_num = {}
        total_jewels = 0

        for stone in stones:
            if stone in stone_to_num:
                stone_to_num[stone] += 1
            else:
                stone_to_num[stone] = 1

        for jewel in jewels:
            if jewel in stone_to_num:
                total_jewels += stone_to_num[jewel]
        return total_jewels


# 2. defaultdict를 사용한 풀이 -> 코드라인을 줄일 수 있다.
class Solution2:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:

        stone_to_num = collections.defaultdict(int) # int의 기본값을 딕셔너리의 초기값으로 지정
        total_jewels = 0

        for stone in stones:
            stone_to_num[stone] += 1
        for jewel in jewels:
            total_jewels += stone_to_num[jewel]
        return total_jewels


# 3. Counter 이용한 풀이
class Solution3:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:

        stone_to_num = collections.Counter(stones)
        total_jewels = 0

        for jewel in jewels:
            total_jewels += stone_to_num[jewel]
        return total_jewels


# 4. pythonic solution
class Solution4:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(stone in jewels for stone in stones)

if __name__ == "__main__":
    jewels = "aA"
    stones = "aAAbbbb"

    solution = Solution4()
    print(solution.numJewelsInStones(jewels, stones))