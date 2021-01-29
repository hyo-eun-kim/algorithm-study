# 색 정렬
# 빨간색을 0, 흰색을 1, 파란색을 2 라 할때, 순서대로 인접하는
# 제자리 정렬을 수행하라.

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        ct_0, ct_1, ct_2 = 0, 0, 0
        for i in nums:
            if i == 0:
                ct_0 += 1
            elif i == 1:
                ct_1 += 1
            elif i == 2:
                ct_2 += 1
        nums[:] = [0]*ct_0 + [1] * ct_1 + [2] * ct_2


    def setColors2(self, nums):
        left, mid, right = 0,0,len(nums)

        while mid<right : 
            if nums[mid]<1 :# 1을 기준으로 작은 값은 왼쪽으로, 큰값은 오른쪽으로 
                nums[left], nums[mid]= nums[mid], nums[left]
                mid +=1    # mid 보다 작은 값을 옮기고 mid 포인터 증가
                left +=1  # 오른쪽으로 이동
            elif nums[mid]>1:
                right -=1  # 왼쪽으로 이동
                nums[mid], nums[right] = nums[right], nums[mid]
            else : # mid ==1 
                mid +=1 


            