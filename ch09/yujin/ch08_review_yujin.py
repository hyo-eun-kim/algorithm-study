#백준 2559
"""
n, k = map(int, input().split())
arr = list(map(int, input().split()))
tmp = max_s = sum(arr[:k])
# 연속적이라서 sort는 못함
for i in range(k,n):
    tmp -= arr[i-k]
    tmp += arr[i]
    if tmp > max_s:
        max_s = tmp

if n != k:
    print(max_s)
else:
    print(tmp)
"""
n, k = map(int, input().split())
arr = list(map(int, input().split()))
tmp = max_s = sum(arr[:k])
# 연속적이라서 sort는 못함
for i in range(1,n-k):
    tmp = tmp-arr[i-1]+arr[i+k-1]
    if tmp > max_s:
        max_s = tmp

if n != k:
    print(max_s)
else:
    print(tmp)
