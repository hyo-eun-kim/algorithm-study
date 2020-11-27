'''
수열

매일 아침 9시에 학교에서 측정한 온도가 어떤 정수의 수열로 주어졌을 때, 연속적인 며칠 동안의 온도의 합이 가장 큰 값을 알아보고자 한다.

매일 측정한 온도가 정수의 수열로 주어졌을 때, 연속적인 며칠 동안의 온도의 합이 가장 큰 값을 계산하는 프로그램을 작성하시오. 
'''

# 내 풀이 
N, K = map(int, input().split())
temp = list(map(int, input().split()))

sum_lst = []
for i in range(N - K + 1):
    if i == 0:
        sum_lst.append(sum(temp[i:i+K]))
    else:
        sum_lst.append(sum_lst[i-1] - temp[i-1] + temp[i+K-1])
print(max(sum_lst))

# 132 ms