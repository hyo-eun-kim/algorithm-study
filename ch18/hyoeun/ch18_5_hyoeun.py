'''
69. 2D 행렬 탐색 2 (leetcode 240)
https://leetcode.com/problems/search-a-2d-matrix-ii/submissions/
m*n 행렬에서 값을 찾아내는 효율적인 알고리즘을 구현하라.
행렬은 왼쪽에서 오른쪽, 상단에서 하단으로 정렬되어 있다.
'''
from typing import *

# Runtime: 364 ms, faster than 5.25% of Python3 online submissions for Search a 2D Matrix II.
# Memory Usage: 18.8 MB, less than 99.97% of Python3 online submissions for Search a 2D Matrix II.
from collections import deque
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        queue = deque()
        queue.append((0, 0))
        while queue:
            i, j = queue.popleft()
            if matrix[i][j] is not None:  # 중복 체크
                value, matrix[i][j] = matrix[i][j], None
                if value == target:
                    return True
                elif value < target:
                    if j+1 < len(matrix[0]):
                        queue.append((i, j+1))
                    if i+1 < len(matrix):
                        queue.append((i+1, j))
        return False
