'''
461. Hamming Distance
https://leetcode.com/problems/hamming-distance/
Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

해밍 distance 구하는 문제 :)
'''

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # xor -> 동일하면 0, 다르면 1 인 것을 이용
        result = bin(x ^ y)
        return result.count('1')