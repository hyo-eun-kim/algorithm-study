# 두수의 합
# 덧셈하여 타겟을 만들수 있는 배열의 두 숫자 인덱스를 리턴하라.

## 시간초과
# def twoSum(nums, target):
#     for i in range(len(nums)-1):
#         for j in range(i+1,len(nums)):
#             if(nums[i]+nums[j]==target):
#                 return print(i,j)


# def twoSum(nums, target):
#     for i, num in enumerate(nums):
#         n = target - num

#         if n in nums[i+1:]:
#             return print(nums.index(num) , nums.index(n))

def twoSum(nums, target):
    num_dict={}
    for i ,num in enumerate(nums):
        num_dict[num]= i
    
    for i , num in enumerate(nums):
        if target-num in num_dict  and i !=num_dict[target-num] :  # [3,2,4], 6 인 경우 (0,0) 이 나오는것을 방지.
            return nums.index(num), num_dict[target-num]
            
twoSum([3,2,4],6)