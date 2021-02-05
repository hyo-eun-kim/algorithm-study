class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(left, right, target):
            mid = (left+right)//2

            if left > right: # 탐색 실패
                return -1

            else:
                if target == nums[mid]:
                    return mid
                elif target < nums[mid]:
                    print(f"left: {left}, right: {right}, mid: {mid}\ntarget < nums[mid]")
                    return binary_search(left, mid-1, target) # mid-1 주의
                else:
                    print(f"left: {left}, right: {right}, mid: {mid}\ntarget > nums[mid]")
                    print(mid)
                    return binary_search(mid+1, right, target) # mid+1 주의

        return binary_search(0,len(nums)-1,target)

class Solution2:
    def search(self, nums: List[int], target: int) -> int:
        index = bisect.bisect_left(nums, target) # bisect 모듈 사용하여 이진 검색
        print(index) # 배열의 최댓값보다 큰 값이 target일 시, len(nums)를 리턴하게 됨. -> 추후 out of range error 발생 (아래에서 예외처리 필수)
        if index < len(nums) and nums[index] == target:
            return index
        else:
            return -1
