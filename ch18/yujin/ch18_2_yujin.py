class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        문제해결
        1) 원래 배열과 회전된 배열을 비교하여 어느 정도 회전이 되었는지 확인
        2) 그 후, 정렬된 배열에서 이진 검색을 통하여 target의 위치 확인
        3) 2)에서 구한 위치에 회전된 정도를 더하여 회전된 배열에서의 위치 확인
        """

        # 1)
        pivot = 0 # 원래 시작점
        for i in range(1,len(nums)):
            if nums[i] < nums[i-1]:
                pivot = i

        # 2)
        nums_s = sorted(nums)
        index = bisect.bisect_left(nums_s, target)
        print(index)
        if index < len(nums_s) and nums_s[index] == target: # index 체크부터 먼저 해줘야 index out of range error 안뜸
            return (pivot+index)%len(nums)
        else:
            return -1

class Solution2:
    def search(self, nums: List[int], target: int) -> int:
        """
        재귀 버전
        """
        def binary_search(left, right):
            mid = left + (right-left)//2
            if left > right:
                return -1
            else:
                if target == nums_s[mid]:
                    return mid
                elif target < nums_s[mid]:
                    return binary_search(left, mid-1)
                else:
                    return binary_search(mid+1, right)

        # 1)
        pivot = 0 # 원래 시작점
        for i in range(1,len(nums)):
            if nums[i] < nums[i-1]:
                pivot = i

        # 2)
        nums_s = sorted(nums)
        index = binary_search(0, len(nums_s)-1)

        if index != -1:
            return (pivot+index)%len(nums_s)
        else:
            return index
