"""
프렌즈4블록
"""
from typing import *


def solution(m: int, n: int, board: List[str]) -> int:
    board = list(map(lambda x: list(x), board))
    matched = True

    while matched:
        # 1. 일치 여부 판별
        matched = []
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] == board[i][j+1] == board[i+1][j] == board[i+1][j+1] != "0":
                    matched.append([i,j])

        # 2. 일치 위치 삭제
        for i, j in matched:
            board[i][j] = board[i][j+1] = board[i+1][j] = board[i+1][j+1] = "0"

        # 3. 빈공간 블록 아래로 내리기
        for k in range(m):
            for i in range(m - 1):
                for j in range(n):
                    if board[i+1][j] == "0":
                        board[i+1][j] = board[i][j]
                        board[i][j] = "0"

    return sum(i.count('0') for i in board)


if __name__ == '__main__':
    print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))