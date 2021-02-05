# 2D 행렬검색2
# mXn  행렬에서 값을 찾아내는 효율적인 알고리즘을 구현하라.
# 행렬은 왼쪽에서 오른쪽, 위에서 아래 오름차순으로 정렬되어있다.

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        return any(target in row for row in matrix)