'''
09. 세 수의 합

배열을 입력받아 합으로 0을 만들 수 있는 3개의 엘리먼트를 출력하라.
'''

# 투 포인터를 활용
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer = []
        
        for i in range(len(nums)-2):
            # 중복된 값은 건너뛴다.
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # 양쪽에서 점점 좁혀갈 예정이다.
            left, right = i+1, len(nums) - 1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
            
                if s < 0:
                    left += 1
                elif s > 0:
                    right -= 1
                else:
                    answer.append([nums[i], nums[left], nums[right]])
                    
                    # [-2,0,0,2,2]와 같이 left, right 양 옆으로 동일한 값이 있을 경우
                    # 중복된 아웃풋이 나오게 되는데 이것을 방지하기 위해 한칸씩 더 이동시킨다.
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    
                    # 시작점을 가운데로 점점 좁혀가며 진행한다.
                    left += 1
                    right -= 1
        return answer
