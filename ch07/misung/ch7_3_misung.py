# 세수의 합
# 배열을 입력받아 합으로 0을 만들수 있는 3개의 엘리먼트를 출력하라

nums = [-1,0,1,2,-1,-4]
def threeSum(nums):
    nums.sort()  # [-4,-1,-1,0,1,2]
    result = []

    for i in range(len(nums)-2): 
        left , right = i+1 , len(nums)-1
        if i>0 and nums[i] == nums[i-1]:  # 중복을 방지하기 위함
            continue

        while left<right :
            sum = nums[i] + nums[left] + nums[right]

            if sum< 0 :
                left+=1
            elif sum > 0 :
                right -=1
            else :  #sum = 0인경우
                result.append((nums[i], nums[left], nums[right]))
                
                while left <right and nums[left] == nums[left+1] :   # 중복을 방지하기 위함
                    left += 1
                while left< right and nums[right] == nums[right-1]:  # 중복을 방지하기 위함
                    right -=1
                left +=1
                right -=1
            
    return result
    
threeSum(nums)