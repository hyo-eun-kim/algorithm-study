# 이진검색
# 정렬된 nums를 입력받아 이진 검색으로 target에 해당하는 인덱스를 찾는다.

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def binary_search(l,r):
            if l<=r :
                mid=(l+r)//2
                
                if nums[mid]<target :
                    return binary_search(mid+1,r)
                elif nums[mid]>target :
                    return binary_search(l,mid-1)
                else:
                    return mid
            else:
                return -1

        return binary_search(0,len(nums)-1)