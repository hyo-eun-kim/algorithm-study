# 회전 정렬된 배열 검색
# 특정 피벗을 기준으로 회전하여 정렬된 배열에서 target 값의 인덱스를 출력하라.

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        left, right = 0, n - 1
        if n == 0: return -1
        
        while left <= right:
            mid = left + (right - left) // 2   # 버그가 없는 중간 값 찾기
            if nums[mid] == target: return mid  # 중간값이 target 이면 바로 mid(=index) 리턴
            
            # inflection point to the right. Left is strictly increasing
            if nums[mid] >= nums[left]:  # mid가 left 보다 크고, 
                if nums[left] <= target < nums[mid]:  # taget 이 left 보다 크면 
                    right = mid - 1  # right 을 이동
                else:
                    left = mid + 1  # 
                    
            # inflection point to the left of me. Right is strictly increasing
            else:  # mid가 left 보다 작으면 
                if nums[mid] < target <= nums[right]:  # target이 mid 보다 크면
                    left = mid + 1
                else:
                    right = mid - 1
            
        return -1