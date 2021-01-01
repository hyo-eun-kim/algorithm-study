# 서로 다른 정수를 입력받아 가능한 모든 순열을 리턴하라.
import itertools

def permute(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    return list(itertools.permutations(nums))


## 순열을 DFS로 어떻게 풀수 있는가?!

def permute2(nums):

    results = []
    prev_element =[]

    def dfs(element):
        
        if len(element)==0:
            results.append(prev_element[:])

        for e in element:
            next_element = element[:]
            next_element.remove(e)

            prev_element.append(e)
            dfs(next_element)
            prev_element.pop()


    dfs(nums)
    return results

print(permute2([1,2,3]))


# First Iteration (Recursion):
# step 1: ([2, 3], [1] )
# step2: ( [3], [1, 2]) step4: ([2], [1, 3])
# step3: ( [], [1, 2, 3]) step5: ([], [1, 3, 2]

# Second Iteration (Recursion):
# step1: ([1, 3], [2])
# step2: ([3], [2, 1]) step4: ([1] , [2, 3])
# step3: ([], [2, 1, 3]) step5: ([], [2, 3, 1])

# Third Iteration (Recursion):
# step1: ([1, 2], [3])
# step2: ([2], [3, 1]) step4: ([1], [3, 2])
# step3: ([], [3, 1, 2]) step5: ([], [3, 2, 1])