"""
## 18-5. 2D 행렬 검색 II

mxn 행렬에서 값을 찾아내는 효율적인 알고리즘을 구현하라.
행렬은 왼쪽에서 오른쪽, 위에서 아래 오름차순으로 정렬되어 있다.
"""
from typing import *


class Solution:
    def searchMatrix(self, matrix, target):
        return any(target in row for row in matrix)


if __name__ == '__main__':
    sol = Solution()
    print(sol.searchMatrix([
        [1,4,7,11,15],
        [2,5,8,12,19],
        [3,6,9,16,22],
        [10,13,14,17,24],
        [18,21,23,26,30]], 5))