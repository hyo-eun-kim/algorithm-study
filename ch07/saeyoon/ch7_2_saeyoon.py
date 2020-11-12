"""
## 7-2. 빗물 트래핑

높이를 입력받아 비 온 후 얼마나 많은 물이 쌓일 수 있는지 계산하라.
"""


def trap(height):
    # Dynamic Programming
    if not height:
        return 0

    volume = 0
    left_max = [0] * len(height)
    right_max = [0] * len(height)

    left_max[0] = height[0]
    for i in range(1, len(height)):
        left_max[i] = max(left_max[i-1], height[i])

    right_max[len(height) - 1] = height[len(height) - 1]
    for i in range(len(height)-2, -1, -1):
        right_max[i] = max(right_max[i+1], height[i])

    for i in range(1, len(height)-1):
        volume += min(left_max[i], right_max[i]) - height[i]

    return volume


def trap2(height):
    # Two pointers
    if not height:
        return 0

    volume = 0
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]

    while left < right:
        left_max = max(height[left], left_max)
        right_max = max(height[right], right_max)

        if left_max <= right_max:
            volume += left_max - height[left]
            left += 1
        else:
            volume += right_max - height[right]
            right -= 1

    return volume


def trap3(height):
    # Stack
    stack = []
    volume = 0

    for i in range(len(height)):
        while stack and height[i] > height[stack[-1]]:
            top = stack.pop()

            if not stack:
                break

            distance = i - stack[-1] - 1
            waters = min(height[i], height[stack[-1]]) - height[top]

            volume += distance * waters

        stack.append(i)

    return volume


if __name__ == '__main__':
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(trap(height))
    print(trap2(height))
    print(trap3(height))