# 배열을 입력받아 output가 자신을 제외한 나머지 모든 요소의 곱셈 결과가 되도록 출력
# 나눗셈을 하지말고 O(n) 안에 풀어라

# 왼쪽과 오른쪽 곱셈을 나눠서 계산하자. 
nums = [1,2,3,4]

def productExceptSelf(nums):
    result = []
   
    left =1
    for i in range(len(nums)):
        result.append(left)  # [1,1,2,6]
        left= left*nums[i]

    right =1
    for j in range(len(nums))[::-1]:
        result[j] = result[j]*right # right 곱한값을 result 에 업데이트
        right = right*nums[j]  
    #     print(right)
    # print(result)
    return result
productExceptSelf(nums)