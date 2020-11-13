# 빗물 트래핑
# 높이를 입력받아 비 온 후 얼마나 많은 물이 쌓일수 있는지 계산하라

height = [0,1,0,2,1,0,1,3,2,1,2,1]

def TrappingRainWater(height):
    if not height:
        return 0

    v = 0 # 부피 저장
    left ,right = 0, len(height)-1
    left_m , right_m = height[left], height[right]

    while left < right :
        left_m = max(height[left],left_m)
        right_m = max(height[right], right_m)

        if left_m <= right_m : # 현재높이와 최대 높이의 차이만큼 
            v += left_m - height[left]
            left += 1
        else :
            v += right_m - height[right]
            right -= 1
    return v

TrappingRainWater(height)