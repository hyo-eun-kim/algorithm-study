class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        문제 접근
        1) 교집합이라는 건 포함되는 요소를 찾는 것
        2) 만약에 배열이 정렬이 되어있다면 이진탐색을 할 수도 있을 것임
        3) 교집합을 구하는 것이므로 set으로 변형을 시켜야함 (set으로 변형이 되면 자동으로 정렬이 안됨)
        """
        set1 = sorted(list(set(nums1)))
        set2 = sorted(list(set(nums2)))
        intersect = []
        print(set1, set2)

        for target in set1:
            left, right = 0, len(set2)-1

            while left <= right:
                mid = left + (right-left)//2
                print(target, set2[mid])
                if target == set2[mid]:
                    intersect.append(target)
                    break
                elif target < set2[mid]:
                    right = mid-1
                else:
                    left = mid+1
            print("뿅")
        return intersect




        
