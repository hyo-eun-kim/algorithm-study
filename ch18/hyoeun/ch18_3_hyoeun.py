'''
67. 두 배열의 교집합 (leetcode 349)
두 배열의 교집합을 구하라
https://leetcode.com/problems/intersection-of-two-arrays/submissions/
'''
from typing import List

# Runtime: 68 ms, faster than 14.12% of Python3 online submissions for Intersection of Two Arrays.
# Memory Usage: 14.5 MB, less than 14.90% of Python3 online submissions for Intersection of Two Arrays.
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return set(nums1).intersection(set(nums2))


# Runtime: 56 ms, faster than 29.23% of Python3 online submissions for Intersection of Two Arrays.
# Memory Usage: 14.4 MB, less than 76.14% of Python3 online submissions for Intersection of Two Arrays.
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        nums1_left, nums1_right = 0, len(nums1)
        nums2_left, nums2_right = 0, len(nums2)

        ans = set()
        while (nums1_left != nums1_right) and (nums2_left != nums2_right):
            if nums1[nums1_left] == nums2[nums2_left]:
                ans.add(nums1[nums1_left])
                nums1_left += 1
                nums2_left += 1
            elif nums1[nums1_left] < nums2[nums2_left]:
                nums1_left += 1
            else:
                nums2_left += 1
        return ans

