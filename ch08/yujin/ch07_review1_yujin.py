"""
10,000 이하의 자연수로 이루어진 길이 N짜리 수열이 주어진다. 이 수열에서 연속된 수들의 부분합 중에 그 합이 S 이상이 되는 것 중, 가장 짧은 것의 길이를 구하는 프로그램을 작성하시오.
연속된 수의 합이라고 하면 자기 자신도 포함하는 듯?
O(n)으로 풀이해야 하는 듯. 내 풀이는 지금 O(n^2)인데 타임아웃 뜸.

n,s = map(int, input().split())
nums = list(map(int, input().split()))
res, p, min_length = 0, 0, float("inf")

for i in range(len(nums)-1):
    #print(i)
    res, p = nums[i], i # 값 변경 계속 해줘야하는 거 유의
    while p < len(nums):
        res += nums[p]
        if res >= s and ((p-i+1) < min_length):
            min_length = p-i+1
        p += 1
        #print(min_length)

if min_length == float("inf"): # 부분합 s가 구해지지 않는 경우
    print(0)
else:
    print(min_length)
"""
"""
    생각을 해보자.
    부분합 중에 그 합이 S 이상이 되는 것 중, 가장 짧은 것의 길이를 구한다고 하면
    하나씩 포인터를 증가시키면서 값을 더해나갈 때 의미가 없음. (배열의 원소가 자연수이므로)
    따라서 합이 S에 도달하면 바로 그냥 다음 i로 넘어가면 될 것임.
"""
n,s = map(int, input().split())
nums = list(map(int, input().split()))
res, start, min_length = 0,0,float("inf")

for end in range(len(nums)):
    res += nums[end] # i (end pointer) 증가하면서 res에 그 합 더 해나감.
    while res >= s: # res>=s일 때만 while loop에 들어감.
        # min_length 비교하고 min_length 업데이트하기
        if end-start+1 < min_length:
            min_length = end-start+1

        # start 포인터 하나 증가 시킴
        res -= nums[start]
        start += 1

if min_length == float("inf"):
    print(0)
else:
    print(min_length)
