'''
08. 빗물 트래핑

높이를 입력받아 비 온 후 얼마나 많은 물이 쌓일 수 있는지 계산하라.
'''

# 내 풀이
class Solution:
    def trap(self, height: List[int]) -> int:
        # height가 없으면 런타임 에러가 남
        if not height:
            return 0
        
        # 투포인터를 사용해 양쪽에서 가장 높은 높이까지 좁혀오는 방식 사용
        ans = 0
        left, right = 0, len(height)-1
        left_max, right_max = height[left], height[right]
        while left < right:
            left_max, right_max = max(height[left],left_max), max(height[right],right_max)
            
            if left_max <= right_max:
                ans += left_max - height[left]
                left += 1
            else:
                ans += right_max - height[right]
                right -= 1
        return ans
        
# 스택쌓기
class Solution:
    def trap(self , height: List[int]) -> int:
        stack = []
        volume = 0
        for i in range(len(height)):
            # 변곡접을 만나는 경우
            while stack and height[i] > height[stack[-1]]:
                # 스택에서꺼낸다
                top = stack .pop()
                 
                if not len(stack) :
                    break
                 
                # 이전과의 차이만큼 물 높이 처리
                distance = i - stack[-1] - 1
                waters = min(height[i], height[stack[-1]]) - height[top]
                                                                     
                volume += distance * waters
                                                                     
            stack.append(i)
        return volume
                                                                     
                                                                     
                                                                     