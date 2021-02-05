class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        fin = []
        for mat in matrix:
            fin.extend(mat)

        fin.sort()

        index = bisect.bisect_left(fin, target)
        if index < len(fin) and fin[index] == target:
            return True
        else:
            return False
