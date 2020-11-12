# https://leetcode.com/problems/trapping-rain-water/
# 높이를 입력받아 비 온 후 얼마나 많은 물이 쌓일 수 있는 지 계산하라
from typing import List


# two pointer를 이용하는 문제
# 단방향으로만 가서는 풀 수 없다. 최대 높이를 향해 양쪽에서 채워나가야 한다 ...
# 풀이 방법을 생각하는 능력을 기르자 :(
def solution1(height: List[int]) -> int:
    if height == []:
        return 0
    else:
        water = 0
        left_pointer = 0
        right_pointer = len(height)-1
        left_max, right_max = height[left_pointer], height[right_pointer]

        # index가 check해야 "할" 위치를 가리키므로
        # left_pointer와 right_pointer가 같아도 실행해야 한다.
        while left_pointer <= right_pointer:
            if left_max <= right_max:
                # 왼쪽에서 오른쪽으로
                if height[left_pointer] > left_max:
                    left_max = height[left_pointer]
                else:
                    water += (left_max - height[left_pointer])
                left_pointer += 1 # 왼쪽에서 오른쪽으로 이동
            else:
                # 오른쪽에서 왼쪽으로
                if height[right_pointer] > right_max:
                    right_max = height[right_pointer]
                else:
                    water += (right_max - height[right_pointer])
                right_pointer -= 1 # 오른쪽에서 왼쪽으로 이동
        return water


if __name__ == "__main__":
    height = [5, 5, 1, 7, 1, 1, 5, 2, 7, 6]
    print(solution1(height))
