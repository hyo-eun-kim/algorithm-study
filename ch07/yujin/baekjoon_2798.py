"""
백준 2798
n개의 자연수 중에서 3개를 골라 그 합이 m 이하가 되도록 할 때,
그 합의 최댓값을 구하여라.

Sol)
- 3개의 수의 합임. --> O(n^2)으로 문제를 풀을 수 있을 것.
- 하나를 고정하고, 투포인터로 나머지 두 개의 수의 합을 구하는 방식으로 해야함.
- 여기서는 인덱스가 중요하지 않기 때문에 정렬이 가능함.

- 다만 합의 최댓값을 구해야 하므로, max를 담을 변수를 하나 추가해줘야 한다.
"""
n,m = map(int, input().split())
nums = list(map(int, input().split()))
low, high, tmp_sum, max_sum = 0, 0, 0, 0 # 자연수이므로 0으로 초기화함.

nums.sort()
for i in range(len(nums)-2):
    low,high = i+1,len(nums)-1 # high도 계속 초기화해줘야함. (pivot인 i가 바뀔 때마다)
    while low < high and max_sum != m: # 투 포인터가 서로 교차하거나 혹은 max_sum이 m일 경우 while loop 탈출
        tmp_sum = nums[i] + nums[low] + nums[high] # 얘는 누적하는 게 아니라 계속 이렇게 값 바꿔줘야함.
        if tmp_sum < m:
            if tmp_sum > max_sum:
                max_sum = tmp_sum
            low += 1
        elif tmp_sum > m:
            high -= 1
        else:
            max_sum = tmp_sum
    if max_sum == m:
        break

print(max_sum)
