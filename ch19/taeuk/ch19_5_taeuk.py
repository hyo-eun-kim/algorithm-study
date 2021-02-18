'''
74. 1비트의 개수

부호없는 정수형을 입력받아 1비트의 개수를 출력하라.

Example 1:

Input: n = 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.
Example 2:

Input: n = 00000000000000000000000010000000
Output: 1
Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.
Example 3:

Input: n = 11111111111111111111111111111101
Output: 31
Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.

'''
# 내 풀이
class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')
    # 28 ms
    
# 비트 연산 풀이
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n &= n - 1
            count += 1
        return count
    # 32 ms