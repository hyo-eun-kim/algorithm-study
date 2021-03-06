'''
393. UTF-8 Validation
https://leetcode.com/problems/utf-8-validation/

A character in UTF8 can be from 1 to 4 bytes long, subjected to the following rules:

For 1-byte character, the first bit is a 0, followed by its unicode code.
For n-bytes character, the first n-bits are all one's, the n+1 bit is 0, followed by n-1 bytes with most significant 2 bits being 10.
This is how the UTF-8 encoding would work:

   Char. number range  |        UTF-8 octet sequence
      (hexadecimal)    |              (binary)
   --------------------+---------------------------------------------
   0000 0000-0000 007F | 0xxxxxxx
   0000 0080-0000 07FF | 110xxxxx 10xxxxxx
   0000 0800-0000 FFFF | 1110xxxx 10xxxxxx 10xxxxxx
   0001 0000-0010 FFFF | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
Given an array of integers representing the data, return whether it is a valid utf-8 encoding.

Note:
The input is an array of integers. Only the least significant 8 bits of each integer is used to store the data. This means each integer represents only 1 byte of data.

Example 1:

data = [197, 130, 1], which represents the octet sequence: 11000101 10000010 00000001.

Return true.
It is a valid utf-8 encoding for a 2-bytes character followed by a 1-byte character.

'''
from typing import List

class Solution:
    def validUtf8(self, data: List[int]) -> bool:

        left = 0
        for i in range(len(data)):
            binary = format(data[i], '08b')
            if left == 0:
                if binary[:5] == '11110':
                    left = 3
                elif binary[:4] == '1110':
                    left = 2
                elif binary[:3] == '110':
                    left = 1
                elif binary[0] == '0':
                    left = 0
                else:
                    return False
            else:
                if binary[:2] != '10':
                    return False
                else:
                    left -= 1
        return left == 0