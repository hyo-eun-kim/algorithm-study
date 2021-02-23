'''
191. Number of 1 Bits
https://leetcode.com/problems/number-of-1-bits/submissions/

Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).
Input: n = 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.
'''


class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')