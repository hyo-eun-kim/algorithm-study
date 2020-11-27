# 일일 온도
# 매일 화씨 온도 리스트 T를 입력 받아서, 더 따뜻한 날씨를 위해서는 며칠을 더 기다려야 하는지 출력하라.
T = [73,74,75,71,69,72,76,73]
T2 = [55,38,53,81,61,93,97,32,43,78]

# 시간제한 걸려버림.......ㅎ....ㅎ
# def dailyTemperatures(T):

#     left = 0
#     right = 1
#     result = []

#     while left< right and left<= len(T)-2: 

#         if T[left] < T[right]:  # 오른쪽이 왼쪽보다 크면 
#             result.append(right-left)  # 인덱스 차이만큼 리스트에 저장
#             left += 1
#             right = left +1

#             if left<= len(T)-2 and T[left] >= T[right] and right ==len(T)-1:  # 오른쪽 포인터에 한계가 오면 0추가
#                 result.append(0)
#                 left+=1
#                 right = left +1

#         elif right == len(T)-1 : # 오른쪽 포인터가 한계에 왔으면,,
#             result.append(0)
#             left +=1
#             right = left +1


#         else :
#             right +=1 

#         # print(left, right)
#     result.append(0)
#     return (result)

def dailyTemperatures(T):
    answer = [0] * len(T)
    stack = []

    for i , cur in enumerate(T):
        # 현재 온도가 스택값보다 높으면 정답처리
        while stack and cur > T[stack[-1]]:   #stack 에는 index 저장.
            last = stack.pop()
            answer[last] = i-last # 인덱스의 차이만큼 저장.
        stack.append(i)

    return answer
dailyTemperatures(T)
